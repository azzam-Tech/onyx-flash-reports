import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def export_unclassified():
    import openpyxl
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "غسالات_غير_مصنفة"
    
    headers = [
        "رقم الصنف", "اسم الصنف", "المجموعة الرئيسية", 
        "المجموعة الفرعية", "تحت الفرعية", 
        "الكمية المتوفرة", "تاريخ آخر حركة"
    ]
    ws.append(headers)
    
    with get_conn() as con:
        with con.cursor() as cur:
            query = """
                SELECT 
                    t.I_CODE,
                    MAX(t.I_NAME),
                    MAX(t.G_CODE),
                    MAX(t.MNG_CODE),
                    MAX(t.SUBG_CODE),
                    SUM(m.I_QTY * m.IN_OUT),
                    MAX(m.I_DATE)
                FROM IAS_ITM_MST t
                LEFT JOIN ITEM_MOVEMENT m ON m.I_CODE = t.I_CODE
                WHERE t.G_CODE = '005'
                  AND (t.MNG_CODE IS NULL OR t.SUBG_CODE IS NULL)
                GROUP BY t.I_CODE
                HAVING (
                    SUM(m.I_QTY * m.IN_OUT) > 0 
                    OR 
                    MAX(CASE WHEN EXTRACT(YEAR FROM m.I_DATE) IN (2025, 2026) THEN 1 ELSE 0 END) = 1
                )
                ORDER BY SUM(m.I_QTY * m.IN_OUT) DESC
            """
            try:
                cur.execute(query)
                rows = cur.fetchall()
                for row in rows:
                    ws.append(row)
                    
                out_path = os.path.join(os.path.dirname(__file__), '..', 'Results', 'غسالات_غير_مصنفة.xlsx')
                wb.save(out_path)
                print(f"Success! Exported {len(rows)} items to {out_path}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == '__main__':
    export_unclassified()
