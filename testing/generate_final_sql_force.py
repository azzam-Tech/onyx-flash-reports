import openpyxl
import sys
import os

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
    
    updates = []
    
    for row_idx, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
        if len(row) > 8 and safe_str(row[8]):
            i_code = safe_str(row[8])
            mng_code = safe_str(row[2])
            subg_code = safe_str(row[5])
            
            if subg_code != "":
                subg_code = subg_code.zfill(3)
                
            if i_code:
                # G_CODE is always '003' for Refrigerators
                sql = f"    UPDATE IAS20261.IAS_ITM_MST SET G_CODE = '003', MNG_CODE = '{mng_code}', SUBG_CODE = '{subg_code}' WHERE I_CODE = '{i_code}';"
                updates.append(sql)
                
    sql_path = 'testing/migrate_refrigerators_final.sql'
    with open(sql_path, 'w', encoding='utf-8') as f:
        f.write("-- سكربت ربط أصناف الثلاجات النهائي (محدث ككتلة واحدة آمنة)\n")
        f.write("SET DEFINE OFF;\n\n")
        f.write("BEGIN\n")
        
        for u in updates:
            f.write(u + "\n")
            
        f.write("\n    -- إذا تم تنفيذ كل شيء بنجاح، يتم الحفظ النهائي\n")
        f.write("    COMMIT;\n")
        f.write("    DBMS_OUTPUT.PUT_LINE('تم تحديث جميع الأصناف بنجاح وتم الحفظ.');\n\n")
        f.write("EXCEPTION\n")
        f.write("    WHEN OTHERS THEN\n")
        f.write("        -- في حال حدوث أي خطأ في أي سطر، يتم التراجع عن كل التحديثات السابقة\n")
        f.write("        ROLLBACK;\n")
        f.write("        DBMS_OUTPUT.PUT_LINE('حدث خطأ! تم التراجع عن جميع التحديثات.');\n")
        f.write("        RAISE;\n")
        f.write("END;\n/\n")
            
    print(f"SUCCESS: Generated {len(updates)} SQL UPDATE statements inside a PL/SQL block.")
    print(f"Saved to {sql_path}")
    
except Exception as e:
    print(f"Error: {e}")
