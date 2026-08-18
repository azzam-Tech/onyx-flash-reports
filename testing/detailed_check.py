import sys
import os
import openpyxl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def detailed_check():
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
                # Get the 163 active items
                cur.execute("""
                    SELECT DISTINCT I_CODE 
                    FROM ITEM_MOVEMENT 
                    WHERE I_CODE IN (SELECT I_CODE FROM IAS_ITM_MST WHERE G_CODE = '003')
                """)
                active_icodes = {r[0] for r in cur.fetchall()}
                
                # Get the 196 stagnant items
                cur.execute("""
                    SELECT I_CODE 
                    FROM IAS_ITM_MST 
                    WHERE G_CODE = '003' 
                    AND I_CODE NOT IN (
                        SELECT DISTINCT I_CODE FROM ITEM_MOVEMENT WHERE I_CODE IS NOT NULL
                    )
                """)
                stagnant_icodes = {r[0] for r in cur.fetchall()}
                
                manager_active = manager_icodes.intersection(active_icodes)
                manager_stagnant = manager_icodes.intersection(stagnant_icodes)
                missed_active = active_icodes - manager_icodes
                
                print(f"Manager Total Unique Items: {len(manager_icodes)}")
                print(f"1. Active items included by Manager: {len(manager_active)} (out of 163)")
                print(f"2. Stagnant items included by Manager: {len(manager_stagnant)} (out of 196)")
                print(f"3. Active items MISSED by Manager: {len(missed_active)}")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    detailed_check()
