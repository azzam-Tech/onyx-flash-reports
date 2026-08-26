import os
import sys
import openpyxl

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def export_no_movement():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "بدون حركة"
    
    ws.append(["رقم الصنف (I_CODE)", "اسم الصنف (I_NAME)"])
    
    with get_conn() as con:
        with con.cursor() as cur:
            query = """
                SELECT t.I_CODE, t.I_NAME
                FROM IAS_ITM_MST t
                WHERE t.G_CODE = '005'
                  AND NOT EXISTS (
                      SELECT 1 FROM ITEM_MOVEMENT m WHERE m.I_CODE = t.I_CODE
                  )
            """
            cur.execute(query)
            no_movement_items = cur.fetchall()
            
            for row in no_movement_items:
                ws.append([row[0], row[1]])
                
    out_path = os.path.join(os.path.dirname(__file__), '..', 'Results', 'غسالات_بدون_حركة.xlsx')
    wb.save(out_path)
    print(f"Exported {len(no_movement_items)} items to {out_path}")

if __name__ == '__main__':
    export_no_movement()
