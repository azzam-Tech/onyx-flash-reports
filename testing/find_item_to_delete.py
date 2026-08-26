import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def find_candidate():
    with get_conn() as con:
        with con.cursor() as cur:
            # List tables
            cur.execute("SELECT table_name FROM all_tables WHERE table_name LIKE 'IAS_ITM%'")
            tables = [r[0] for r in cur.fetchall()]
            print("IAS_ITM tables:")
            print(tables)
            
            # Find an item in group 005 that does NOT have any movement
            query = """
            SELECT I_CODE, I_NAME
            FROM IAS_ITM_MST 
            WHERE G_CODE = '005' 
              AND NVL(INACTIVE, 0) = 0
              AND I_CODE NOT IN (SELECT I_CODE FROM ITEM_MOVEMENT)
            FETCH FIRST 1 ROWS ONLY
            """
            cur.execute(query)
            row = cur.fetchone()
            
            if row:
                print(f"\nCandidate Item found:")
                print(f"I_CODE: {row[0]}")
                print(f"I_NAME: {row[1]}")
                
if __name__ == '__main__':
    find_candidate()
