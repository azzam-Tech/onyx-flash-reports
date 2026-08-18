import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_stock():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                WITH item_stock AS (
                    SELECT 
                        m.I_CODE,
                        SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) as stock
                    FROM IAS_ITM_MST m
                    LEFT JOIN ITEM_MOVEMENT mv ON mv.I_CODE = m.I_CODE
                    WHERE m.G_CODE = '003'
                    GROUP BY m.I_CODE
                )
                SELECT 
                    COUNT(*) as total_items,
                    SUM(CASE WHEN stock > 0 THEN 1 ELSE 0 END) as items_with_positive_stock,
                    SUM(CASE WHEN stock = 0 OR stock IS NULL THEN 1 ELSE 0 END) as items_with_zero_stock,
                    SUM(CASE WHEN stock < 0 THEN 1 ELSE 0 END) as items_with_negative_stock
                FROM item_stock
            """)
            row = cur.fetchone()
            print(f"Total fridges (G_CODE='003'): {row[0]}")
            print(f"Fridges with Positive Stock (> 0): {row[1]}")
            print(f"Fridges with Zero Stock (0 or None): {row[2]}")
            print(f"Fridges with Negative Stock (< 0): {row[3]}")

if __name__ == '__main__':
    check_stock()
