import os
import sys
import openpyxl

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def analyze_ac_movement_examples():
    file_path = r"C:\Users\amarn\Downloads\مكيفات_مصنفة_نهائي_v2.xlsx"
    
    try:
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        
        excel_data = set()
        for i, row in enumerate(sheet.iter_rows(values_only=True)):
            if i > 0:
                icode = str(row[0]).strip() if row[0] else None
                if icode:
                    excel_data.add(icode)
                    
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute("SELECT I_CODE FROM IAS_ITM_MST WHERE G_CODE = '002'")
                db_icodes = {str(r[0]).strip() for r in cur.fetchall()}
                
                missing_items = list(db_icodes - excel_data)
                
                if not missing_items:
                    print("No missing items to check.")
                    return
                
                bind_vars = ','.join(f':{i+1}' for i in range(len(missing_items)))
                query = f"""
                    SELECT m.I_CODE, t.I_NAME, MAX(m.I_DATE) as last_mov
                    FROM ITEM_MOVEMENT m
                    JOIN IAS_ITM_MST t ON m.I_CODE = t.I_CODE
                    WHERE m.I_CODE IN ({bind_vars})
                    GROUP BY m.I_CODE, t.I_NAME
                    ORDER BY last_mov DESC
                """
                cur.execute(query, missing_items)
                items_with_movement = cur.fetchmany(20)
                
                print("--- 20 Examples of Missing ACs with Movement This Year ---")
                for i, r in enumerate(items_with_movement):
                    code = r[0]
                    name = r[1]
                    last_mov = r[2].strftime('%Y-%m-%d') if r[2] else 'Unknown'
                    print(f"{i+1}. {code} : {name}  | آخر حركة: {last_mov}")
                        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    analyze_ac_movement_examples()
