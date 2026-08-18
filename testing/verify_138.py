import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def verify_138():
    with get_conn() as con:
        with con.cursor() as cur:
            # Check distinct items with movements in 2026
            cur.execute("""
                SELECT COUNT(DISTINCT m.I_CODE) 
                FROM IAS_ITM_MST m 
                JOIN ITEM_MOVEMENT mv ON m.I_CODE = mv.I_CODE 
                WHERE m.G_CODE = '003' 
                  AND mv.I_DATE >= TO_DATE('2026-01-01', 'YYYY-MM-DD') 
                  AND mv.I_DATE <= TO_DATE('2026-12-31', 'YYYY-MM-DD')
            """)
            moved_items = cur.fetchone()[0]
            print(f"Items with movements in 2026 (ITEM_MOVEMENT): {moved_items}")
            
            # Check items with sales in 2026
            cur.execute("""
                SELECT COUNT(DISTINCT m.I_CODE) 
                FROM IAS_ITM_MST m 
                JOIN IAS_BILL_DTL bd ON m.I_CODE = bd.I_CODE 
                JOIN IAS_BILL_MST bm ON bm.BILL_DOC_TYPE = bd.BILL_DOC_TYPE AND bm.BILL_NO = bd.BILL_NO AND bm.BILL_SER = bd.BILL_SER
                WHERE m.G_CODE = '003' 
                  AND bm.BILL_DATE >= TO_DATE('2026-01-01', 'YYYY-MM-DD') 
                  AND bm.BILL_DATE <= TO_DATE('2026-12-31', 'YYYY-MM-DD')
            """)
            sold_items = cur.fetchone()[0]
            print(f"Items with sales in 2026 (IAS_BILL_MST): {sold_items}")
            
            # Count in ITEM_MOVEMENT with positive stock at some point maybe?
            # Or just breakdown by DOC_TYPE
            cur.execute("""
                SELECT DOC_TYPE, COUNT(DISTINCT m.I_CODE)
                FROM IAS_ITM_MST m 
                JOIN ITEM_MOVEMENT mv ON m.I_CODE = mv.I_CODE 
                WHERE m.G_CODE = '003' 
                  AND mv.I_DATE >= TO_DATE('2026-01-01', 'YYYY-MM-DD') 
                  AND mv.I_DATE <= TO_DATE('2026-12-31', 'YYYY-MM-DD')
                GROUP BY DOC_TYPE
            """)
            print("\nBreakdown by DOC_TYPE in ITEM_MOVEMENT:")
            for r in cur.fetchall():
                print(r)

if __name__ == '__main__':
    verify_138()
