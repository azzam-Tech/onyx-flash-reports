import os
import sys
import openpyxl

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def analyze_final_excel():
    file_path = r"C:\Users\amarn\Downloads\غسالات_مصنفة_نهائي.xlsx"
    out_path = os.path.join(os.path.dirname(__file__), '..', 'migration_plan', 'update_group_005_final.sql')
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    try:
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        
        excel_data = {}
        for i, row in enumerate(sheet.iter_rows(values_only=True)):
            if i > 0:
                icode = str(row[0]).strip() if row[0] else None
                sg_code = str(row[2]).strip().zfill(3) if row[2] else None
                ssg_code = str(row[3]).strip().zfill(3) if row[3] else None
                if icode and sg_code and ssg_code:
                    excel_data[icode] = (sg_code, ssg_code)
                    
        print(f"Total valid items in Final Excel: {len(excel_data)}")
        
        with get_conn() as con:
            with con.cursor() as cur:
                # Get all active items in G_CODE '005'
                cur.execute("SELECT I_CODE, NVL(INACTIVE, 0) FROM IAS_ITM_MST WHERE G_CODE = '005'")
                db_items = cur.fetchall()
                
                db_icodes = {str(r[0]).strip(): r[1] for r in db_items}
                
                matched = sum(1 for icode in excel_data if icode in db_icodes)
                missing = sum(1 for icode in db_icodes if icode not in excel_data)
                
                print(f"Total items in DB for G_CODE '005': {len(db_icodes)}")
                print(f"Matched items (will be updated): {matched}")
                print(f"Missing items (will be deactivated): {missing}")
                
                # Generate SQL
                with open(out_path, 'w', encoding='utf-8') as f:
                    f.write("-- ==================================================\n")
                    f.write("-- تحديث المجموعات الفرعية وتحت الفرعية للغسالات المعتمدة\n")
                    f.write("-- ==================================================\n")
                    
                    for icode, (sg, ssg) in excel_data.items():
                        if icode in db_icodes:
                            f.write(f"UPDATE IAS_ITM_MST SET MNG_CODE = '{sg}', SUBG_CODE = '{ssg}', INACTIVE = 0 WHERE I_CODE = '{icode}';\n")
                        
                    f.write("\n-- ==================================================\n")
                    f.write("-- تجميد الغسالات المتبقية (التي لم ترد في الملف النهائي)\n")
                    f.write("-- ==================================================\n")
                    
                    for icode in db_icodes:
                        if icode not in excel_data:
                            # Only write update if it's not already inactive to save time
                            # Actually better to just force inactive on all missing
                            f.write(f"UPDATE IAS_ITM_MST SET INACTIVE = 1 WHERE I_CODE = '{icode}';\n")
                            
                    f.write("\nCOMMIT;\n")
                    
                print(f"\nFinal SQL script generated at: {out_path}")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    analyze_final_excel()
