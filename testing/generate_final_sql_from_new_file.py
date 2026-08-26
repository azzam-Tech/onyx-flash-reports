import openpyxl
from collections import Counter
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

def safe_str(val):
    if val is None:
        return ""
    if isinstance(val, float) and val.is_integer():
        return str(int(val)).strip()
    return str(val).strip()

try:
    file_path = r"C:\Users\amarn\Downloads\الثلاجات_تصنيف_اونكس_برو_مرتب (1).xlsx"
    wb = openpyxl.load_workbook(file_path, data_only=True)
    ws = wb.active
    
    i_codes = []
    updates = []
    mng_codes_in_excel = set()
    subg_codes_in_excel = set()
    
    for row_idx, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
        if len(row) > 8 and safe_str(row[8]):
            i_code = safe_str(row[8])
            mng_code = safe_str(row[2])
            subg_code = safe_str(row[5])
            
            if subg_code != "":
                subg_code = subg_code.zfill(3)
                
            if i_code:
                i_codes.append(i_code)
                if mng_code: mng_codes_in_excel.add(mng_code)
                if subg_code: subg_codes_in_excel.add(subg_code)
                
                # generate sql statement
                sql = f"UPDATE IAS20261.IAS_ITM_MST SET G_CODE = '003', MNG_CODE = '{mng_code}', SUBG_CODE = '{subg_code}' WHERE I_CODE = '{i_code}';"
                updates.append(sql)
                
    counts = Counter(i_codes)
    duplicates = {k: v for k, v in counts.items() if v > 1}
    
    print(f"--- Validation Report for (الثلاجات_تصنيف_اونكس_برو_مرتب (1).xlsx) ---")
    print(f"Total Rows with Items: {len(i_codes)}")
    print(f"Unique Items: {len(counts)}")
    
    if duplicates:
        print(f"WARNING: Found {len(duplicates)} duplicate item codes!")
    else:
        print("SUCCESS: No duplicate items found in the Excel file.")
        
    # Validate against DB
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            # 1. Check I_CODEs
            i_codes_list = list(counts.keys())
            binds = [f":{i+1}" for i in range(len(i_codes_list))]
            query = f"SELECT I_CODE FROM IAS20261.IAS_ITM_MST WHERE I_CODE IN ({','.join(binds)})"
            cur.execute(query, i_codes_list)
            db_codes = set(r[0] for r in cur.fetchall())
            missing_codes = set(i_codes_list) - db_codes
            
            if missing_codes:
                print(f"WARNING: {len(missing_codes)} items NOT found in the database!")
            else:
                print("SUCCESS: All items exist in the database.")
                
            # 2. Check MNG_CODEs
            cur.execute("SELECT MNG_CODE FROM IAS20261.IAS_MAINSUB_GRP_DTL WHERE G_CODE IN ('003', '3')")
            valid_mng = set(r[0] for r in cur.fetchall())
            invalid_mng = mng_codes_in_excel - valid_mng
            if invalid_mng:
                print(f"WARNING: These MNG_CODEs (فرعية) from Excel do NOT exist in DB: {invalid_mng}")
            else:
                print("SUCCESS: All MNG_CODEs exist in DB.")
                
            # 3. Check SUBG_CODEs
            cur.execute("SELECT SUBG_CODE FROM IAS20261.IAS_SUB_GRP_DTL")
            valid_subg = set(r[0] for r in cur.fetchall())
            invalid_subg = subg_codes_in_excel - valid_subg
            if invalid_subg:
                print(f"WARNING: These SUBG_CODEs (تحت فرعية) from Excel do NOT exist in DB: {invalid_subg}")
            else:
                print("SUCCESS: All SUBG_CODEs exist in DB.")
                
    # Save SQL
    if not invalid_mng and not invalid_subg and not duplicates and not missing_codes:
        sql_path = 'testing/migrate_refrigerators_final.sql'
        with open(sql_path, 'w', encoding='utf-8') as f:
            f.write("-- سكربت ربط أصناف الثلاجات النهائي\n")
            f.write("SET DEFINE OFF;\n\n")
            for u in updates:
                f.write(u + "\n")
        print(f"\nSUCCESS: Generated {len(updates)} SQL UPDATE statements.")
        print(f"Saved to {sql_path}")
    else:
        print("\nNotice: Validation warnings found. SQL script was NOT generated to prevent errors. Please fix the warnings first.")
        
except Exception as e:
    print(f"Error: {e}")
