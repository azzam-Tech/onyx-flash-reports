import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def test_cust():
    with get_conn() as con:
        with con.cursor() as cur:
            try:
                cur.execute("""
                    SELECT column_name 
                    FROM all_tab_columns 
                    WHERE table_name = 'CUSTOMER'
                """)
                cols = [r[0] for r in cur.fetchall()]
                print("Cols:", cols)
                
                cur.execute("""
                    SELECT * FROM IAS20261.CUSTOMER WHERE ROWNUM <= 1
                """)
                c = [col[0] for col in cur.description]
                r = cur.fetchone()
                for i in range(len(c)):
                    print(f"{c[i]}: {r[i]}")
            except Exception as e:
                print("Error:", e)

if __name__ == '__main__':
    test_cust()
