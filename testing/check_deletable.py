import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_deletable_items():
    with get_conn() as con:
        with con.cursor() as cur:
            # Total items
            cur.execute("SELECT COUNT(*) FROM IAS_ITM_MST")
            total = cur.fetchone()[0]
            
            # Items with no movement
            cur.execute("""
                SELECT COUNT(I_CODE) 
                FROM IAS_ITM_MST 
                WHERE I_CODE NOT IN (
                    SELECT DISTINCT I_CODE FROM ITEM_MOVEMENT WHERE I_CODE IS NOT NULL
                )
            """)
            no_mov = cur.fetchone()[0]
            
            # Check fridges specifically
            cur.execute("""
                SELECT COUNT(I_CODE) 
                FROM IAS_ITM_MST 
                WHERE G_CODE = '003' AND I_CODE NOT IN (
                    SELECT DISTINCT I_CODE FROM ITEM_MOVEMENT WHERE I_CODE IS NOT NULL
                )
            """)
            no_mov_fridges = cur.fetchone()[0]
            
            print(f"Total items in DB: {total}")
            print(f"Items with NO MOVEMENT (Safe to delete candidates): {no_mov}")
            print(f"Fridges (G_CODE='003') with NO MOVEMENT: {no_mov_fridges}")

if __name__ == '__main__':
    check_deletable_items()
