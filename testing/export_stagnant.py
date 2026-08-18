import sys
import os
import openpyxl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def export_stagnant_fridges():
    query = """
        SELECT I_CODE, I_NAME, I_E_NAME, INACTIVE 
        FROM IAS_ITM_MST 
        WHERE G_CODE = '003' 
        AND I_CODE NOT IN (
            SELECT DISTINCT I_CODE FROM ITEM_MOVEMENT WHERE I_CODE IS NOT NULL
        )
        ORDER BY I_CODE
    """
    
    file_path = os.path.join(os.path.dirname(__file__), "fridges_to_delete.xlsx")
    
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            
            # Create a new Excel workbook
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "الثلاجات الراكدة"
            
            # Add Headers
            ws.append(["رقم الصنف (I_CODE)", "اسم الصنف (I_NAME)", "الاسم الانجليزي (I_E_NAME)", "حالة الإيقاف (INACTIVE)"])
            
            # Add Data
            for row in rows:
                ws.append(row)
                
            wb.save(file_path)
            print(f"Exported {len(rows)} items to {file_path}")

if __name__ == '__main__':
    export_stagnant_fridges()
