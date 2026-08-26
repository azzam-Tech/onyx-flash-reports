import openpyxl

def safe_str(val):
    if val is None:
        return ""
    # We must treat floats like 2.0 (if any) carefully, but the user typed 2. 
    # openpyxl might read it as int 2. We convert to str.
    if isinstance(val, float) and val.is_integer():
        return str(int(val)).strip()
    return str(val).strip()

try:
    file_path = r"C:\Users\amarn\Downloads\الثلاجات_تصنيف_اونكس_برو.xlsx"
    wb = openpyxl.load_workbook(file_path, data_only=True)
    ws = wb.active
    
    items_update = []
    
    for row in ws.iter_rows(min_row=2, values_only=True):
        # Only zfill G_CODE because we know it's always '003'
        g_code = safe_str(row[0]).zfill(3) if row[0] else '003'
        
        # DO NOT zfill mng_code and subg_code. Treat them EXACTLY as written in Excel.
        mng_code = safe_str(row[2])
        subg_code = safe_str(row[3])
        i_code = safe_str(row[5])
        
        if i_code and g_code and mng_code:
            items_update.append((i_code, g_code, mng_code, subg_code))
            
    sql_lines = [
        "-- سكربت ربط أصناف الثلاجات بالمجموعات الجاهزة",
        "SET DEFINE OFF;",
        "",
    ]
    
    for i_code, g, m, s in items_update:
        s_val = f"'{s}'" if s else "NULL"
        sql_lines.append(f"UPDATE IAS20261.IAS_ITM_MST SET G_CODE = '{g}', MNG_CODE = '{m}', SUBG_CODE = {s_val} WHERE I_CODE = '{i_code}';")
        
    sql_lines.append("")
    sql_lines.append("COMMIT;")
    sql_lines.append("")
    
    out_path = 'testing/migrate_refrigerators.sql'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(sql_lines))
        
    print(f"Generated {len(items_update)} Item Updates.")
    print(f"File saved to {out_path}")
    
except Exception as e:
    print(f"Error: {e}")
