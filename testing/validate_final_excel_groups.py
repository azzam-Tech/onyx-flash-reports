import openpyxl
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
    file_path = r"C:\Users\amarn\Downloads\الثلاجات_تصنيف_اونكس_برو_محدث3.xlsx"
    wb = openpyxl.load_workbook(file_path, data_only=True)
    ws = wb.active
    
    mng_codes_in_excel = set()
    subg_codes_in_excel = set()
    
    for row_idx, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
        if len(row) > 8 and safe_str(row[8]):
            mng_code = safe_str(row[2])
            subg_code = safe_str(row[5])
            
            # Since user previously told us NOT to use zfill, we take exact string
            # But just in case, let's see if 25 vs 025 is an issue.
            # We will pad it IF the length is 1 or 2 and the original was number? 
            # We will just test both raw and zfill(3) in the DB
            
            if mng_code: mng_codes_in_excel.add(mng_code)
            if subg_code: subg_codes_in_excel.add(subg_code)
            
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            # Get valid MNG_CODEs
            cur.execute("SELECT MNG_CODE FROM IAS20261.IAS_MAINSUB_GRP_DTL WHERE G_CODE IN ('003', '3')")
            valid_mng = set(r[0] for r in cur.fetchall())
            
            # Get valid SUBG_CODEs
            cur.execute("SELECT SUBG_CODE FROM IAS20261.IAS_SUB_GRP_DTL")
            valid_subg = set(r[0] for r in cur.fetchall())
            
            print("--- MNG_CODE Validation ---")
            invalid_mng = mng_codes_in_excel - valid_mng
            if invalid_mng:
                print(f"WARNING: These MNG_CODEs from Excel do NOT exist in DB: {invalid_mng}")
                # Check if padded version exists
                padded = {x.zfill(3) for x in invalid_mng}
                valid_padded = padded.intersection(valid_mng)
                if valid_padded:
                    print(f"  BUT their padded versions DO exist: {valid_padded}")
            else:
                print("All MNG_CODEs exist in DB.")
                
            print("\n--- SUBG_CODE Validation ---")
            invalid_subg = subg_codes_in_excel - valid_subg
            if invalid_subg:
                print(f"WARNING: These SUBG_CODEs from Excel do NOT exist in DB: {invalid_subg}")
                padded = {x.zfill(3) for x in invalid_subg}
                valid_padded = padded.intersection(valid_subg)
                if valid_padded:
                    print(f"  BUT their padded versions DO exist: {valid_padded}")
            else:
                print("All SUBG_CODEs exist in DB.")
                
except Exception as e:
    print(f"Error: {e}")
