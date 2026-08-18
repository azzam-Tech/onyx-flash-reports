import sys
import os
import openpyxl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_manager_excess():
    file_path = r"C:\Users\amarn\Downloads\الثلاجات_تصنيف_اونكس_برو_مرتب.xlsx"
    try:
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        
        manager_icodes = set()
        for i, row in enumerate(sheet.iter_rows(values_only=True)):
            if i == 0: continue
            icode = str(row[8]).strip() if row[8] else None
            if icode:
                manager_icodes.add(icode)
                
        with get_conn() as con:
            with con.cursor() as cur:
                # Get the 163 active items (items with movement)
                cur.execute("""
                    SELECT DISTINCT I_CODE 
                    FROM ITEM_MOVEMENT 
                    WHERE I_CODE IN (SELECT I_CODE FROM IAS_ITM_MST WHERE G_CODE = '003')
                """)
                active_icodes = {r[0] for r in cur.fetchall()}
                
                # The excess items
                excess_icodes = manager_icodes - active_icodes
                
                print(f"Manager total items: {len(manager_icodes)}")
                print(f"Active items (with movement): {len(active_icodes)}")
                print(f"Excess items (in manager file but NO movement): {len(excess_icodes)}")
                
                if excess_icodes:
                    # Let's get their names to show the user
                    format_strings = ','.join([f"'{c}'" for c in excess_icodes])
                    cur.execute(f"SELECT I_CODE, I_NAME, AD_DATE FROM IAS_ITM_MST WHERE I_CODE IN ({format_strings})")
                    print("\nSample of the excess items:")
                    for i, r in enumerate(cur.fetchall()):
                        print(f" - Code: {r[0]}, Name: {r[1]}, Created At: {r[2]}")
                        if i >= 10: 
                            print("   ... (showing only first 10)")
                            break

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    check_manager_excess()
