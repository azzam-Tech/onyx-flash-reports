import sys
import os
import openpyxl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_w_bal():
    file_path = r"C:\Users\amarn\Downloads\الثلاجات_تصنيف_اونكس_برو_مرتب.xlsx"
    try:
        # Read Manager's Excel
        wb_mgr = openpyxl.load_workbook(file_path)
        sheet_mgr = wb_mgr.active
        manager_icodes = set()
        for i, row in enumerate(sheet_mgr.iter_rows(values_only=True)):
            if i == 0: continue
            icode = str(row[8]).strip() if row[8] else None
            if icode:
                manager_icodes.add(icode)
                
        with get_conn() as con:
            with con.cursor() as cur:
                # Stagnant Items (Not in ITEM_MOVEMENT)
                cur.execute("""
                    SELECT I_CODE 
                    FROM IAS_ITM_MST 
                    WHERE G_CODE = '003' 
                    AND I_CODE NOT IN (
                        SELECT DISTINCT I_CODE FROM ITEM_MOVEMENT WHERE I_CODE IS NOT NULL
                    )
                """)
                stagnant_icodes = {r[0] for r in cur.fetchall()}
                manager_stagnant = manager_icodes.intersection(stagnant_icodes)
                
                format_strings = ','.join([f"'{c}'" for c in manager_stagnant])
                
                # Try reading from IAS_ITM_BAL (some Onyx versions use this)
                try:
                    cur.execute(f"SELECT COUNT(DISTINCT I_CODE) FROM IAS_ITM_BAL WHERE I_CODE IN ({format_strings})")
                    print(f"Items in IAS_ITM_BAL: {cur.fetchone()[0]}")
                except Exception as e:
                    print("Error reading IAS_ITM_BAL:", e)
                    
                # Try reading W_BAL with exact column names if W_BAL exists
                try:
                    cur.execute(f"SELECT COUNT(DISTINCT I_CODE) FROM IAS_W_BAL WHERE I_CODE IN ({format_strings})")
                    print(f"Items in IAS_W_BAL: {cur.fetchone()[0]}")
                except Exception as e:
                    pass

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    check_w_bal()
