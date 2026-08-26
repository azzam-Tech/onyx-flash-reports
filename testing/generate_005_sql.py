import os
import sys
import openpyxl

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def generate_sql():
    file_path = r"C:\Users\amarn\Downloads\غسالات_مصنفة_بالاكواد_1.xlsx"
    out_path = os.path.join(os.path.dirname(__file__), '..', 'migration_plan', 'update_group_005.sql')
    
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    
    excel_data = {}
    for i, row in enumerate(sheet.iter_rows(values_only=True)):
        if i > 0:
            icode = str(row[8]).strip() if row[8] else None
            sg_code = str(row[3]).strip().zfill(3) if row[3] else None
            ssg_code = str(row[5]).strip().zfill(3) if row[5] else None
            if icode and sg_code and ssg_code:
                excel_data[icode] = (sg_code, ssg_code)
                
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT I_CODE FROM IAS_ITM_MST WHERE G_CODE = '005'")
            db_items = [str(r[0]).strip() for r in cur.fetchall()]
            
            missing_items = [icode for icode in db_items if icode not in excel_data]
            
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write("-- ==================================================\n")
                f.write("-- تحديث المجموعات الفرعية وتحت الفرعية للأصناف المعتمدة\n")
                f.write("-- ==================================================\n")
                
                for icode, (sg, ssg) in excel_data.items():
                    f.write(f"UPDATE IAS_ITM_MST SET SG_CODE = '{sg}', SSG_CODE = '{ssg}', INACTIVE = 0 WHERE I_CODE = '{icode}';\n")
                    
                f.write("\n-- ==================================================\n")
                f.write("-- تجميد الأصناف المتبقية (التي لم ترد في ملف الإكسيل)\n")
                f.write("-- ==================================================\n")
                
                for icode in missing_items:
                    f.write(f"UPDATE IAS_ITM_MST SET INACTIVE = 1 WHERE I_CODE = '{icode}';\n")
                    
                f.write("\nCOMMIT;\n")
                
            print(f"SQL script generated successfully at: {out_path}")
            print(f"Total active items updated: {len(excel_data)}")
            print(f"Total items deactivated: {len(missing_items)}")

if __name__ == '__main__':
    generate_sql()
