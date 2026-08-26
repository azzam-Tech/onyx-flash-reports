import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def test_items():
    with get_conn() as con:
        with con.cursor() as cur:
            try:
                cur.execute("""
                    SELECT column_name 
                    FROM all_tab_columns 
                    WHERE table_name = 'IAS_ITM_MST'
                """)
                cols = [r[0] for r in cur.fetchall()]
                print("IAS_ITM_MST cols:", [c for c in cols if 'NAME' in c or 'DESC' in c])
            except Exception as e:
                print("Error:", e)

if __name__ == '__main__':
    test_items()
