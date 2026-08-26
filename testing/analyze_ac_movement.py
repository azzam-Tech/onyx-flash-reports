import os
import sys
import openpyxl

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def analyze_ac_movement():
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
                print(f"Total missing items to check for movement: {len(missing_items)}")
                
                if not missing_items:
                    print("No missing items to check.")
                    return
                
                # Check movement dates
                bind_vars = ','.join(f':{i+1}' for i in range(len(missing_items)))
                query = f"""
                    SELECT 
                        MIN(m.I_DATE) as first_mov,
                        MAX(m.I_DATE) as last_mov,
                        COUNT(DISTINCT m.I_CODE) as items_with_mov
                    FROM ITEM_MOVEMENT m
                    WHERE m.I_CODE IN ({bind_vars})
                """
                cur.execute(query, missing_items)
                res = cur.fetchone()
                
                first_mov = res[0]
                last_mov = res[1]
                items_with_mov = res[2]
                
                print(f"Out of {len(missing_items)} missing items, {items_with_mov} have movement in the database!")
                if items_with_mov > 0:
                    print(f"Earliest movement recorded on: {first_mov.strftime('%Y-%m-%d') if first_mov else 'Unknown'}")
                    print(f"Latest movement recorded on:   {last_mov.strftime('%Y-%m-%d') if last_mov else 'Unknown'}")
                    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    analyze_ac_movement()
