import os
import sys
import openpyxl

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def detailed_analysis():
    file_path = r"C:\Users\amarn\Downloads\غسالات_مصنفة_بالاكواد_1.xlsx"
    
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    
    excel_icodes = set()
    for i, row in enumerate(sheet.iter_rows(values_only=True)):
        if i > 0:
            icode = str(row[8]).strip() if row[8] else None
            if icode:
                excel_icodes.add(icode)
                
    with get_conn() as con:
        with con.cursor() as cur:
            # All items in 005
            cur.execute("SELECT I_CODE, I_NAME, NVL(INACTIVE, 0) FROM IAS_ITM_MST WHERE G_CODE = '005'")
            db_items = cur.fetchall()
            
            missing_items = [r for r in db_items if str(r[0]).strip() not in excel_icodes]
            
            print(f"Total items in DB for 005: {len(db_items)}")
            print(f"Items in Excel: {len(excel_icodes)}")
            print(f"Items in DB but NOT in Excel: {len(missing_items)}")
            
            inactive_missing = sum(1 for r in missing_items if r[2] == 1)
            active_missing = sum(1 for r in missing_items if r[2] == 0)
            
            print(f"  - Active missing items: {active_missing}")
            print(f"  - Inactive missing items: {inactive_missing}")
            
            # Let's check if the active missing items have stock or movement
            active_missing_icodes = [str(r[0]).strip() for r in missing_items if r[2] == 0]
            
            if active_missing_icodes:
                # Chunk the list for IN clause
                placeholders = ','.join([f":{i}" for i in range(len(active_missing_icodes))])
                query = f"""
                SELECT I_CODE, COUNT(*)
                FROM ITEM_MOVEMENT
                WHERE I_CODE IN ({placeholders})
                GROUP BY I_CODE
                """
                cur.execute(query, active_missing_icodes)
                mov_data = cur.fetchall()
                mov_dict = {str(r[0]).strip(): r[1] for r in mov_data}
                
                with_mov = sum(1 for icode in active_missing_icodes if icode in mov_dict)
                without_mov = len(active_missing_icodes) - with_mov
                
                print(f"  - Active missing WITH movement/stock: {with_mov}")
                print(f"  - Active missing WITHOUT movement/stock: {without_mov}")
                
            print("\nSample of Active missing items WITH movement:")
            sample = [r for r in missing_items if r[2] == 0 and str(r[0]).strip() in mov_dict][:10]
            for s in sample:
                print(f"   I_CODE: {s[0]} - {s[1]} (Movements: {mov_dict.get(str(s[0]).strip(), 0)})")

if __name__ == '__main__':
    detailed_analysis()
