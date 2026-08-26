import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def get_wm_no_movement():
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
            
            print(f"Total washing machines with NO movement: {len(no_movement_items)}")
            
            if no_movement_items:
                print("--- List of Items ---")
                for i, r in enumerate(no_movement_items):
                    print(f"{r[0]} : {r[1]}")

if __name__ == '__main__':
    get_wm_no_movement()
