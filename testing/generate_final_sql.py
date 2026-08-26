import openpyxl
import sys

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
    
    updates = []
    
    for row_idx, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
        if len(row) > 8 and safe_str(row[8]):
            i_code = safe_str(row[8])
            mng_code = safe_str(row[2])
            subg_code = safe_str(row[5])
            
            # The user requested us to handle the missing zeros in subg_code
            if subg_code != "":
                subg_code = subg_code.zfill(3)
                
            if i_code and mng_code and subg_code:
                # G_CODE is always '003' for Refrigerators
                sql = f"UPDATE IAS20261.IAS_ITM_MST SET G_CODE = '003', MNG_CODE = '{mng_code}', SUBG_CODE = '{subg_code}' WHERE I_CODE = '{i_code}';"
                updates.append(sql)
                
    sql_path = 'testing/migrate_refrigerators_final.sql'
    with open(sql_path, 'w', encoding='utf-8') as f:
        f.write("-- سكربت ربط أصناف الثلاجات النهائي\n")
        f.write("SET DEFINE OFF;\n\n")
        for u in updates:
            f.write(u + "\n")
            
    print(f"Generated {len(updates)} SQL UPDATE statements.")
    print(f"Saved to {sql_path}")
    
except Exception as e:
    print(f"Error: {e}")
