import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def test_company():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT * FROM IAS20261.S_CMPNY WHERE ROWNUM <= 1
            """)
            c = [col[0] for col in cur.description]
            r = cur.fetchone()
            if r:
                for i in range(len(c)):
                    print(f"{c[i]}: {r[i]}")
            else:
                print("No data in S_CMPNY")

            print("\n==================\n")
            
            cur.execute("""
                SELECT * FROM IAS20261.S_BRN WHERE ROWNUM <= 1
            """)
            c = [col[0] for col in cur.description]
            r = cur.fetchone()
            if r:
                for i in range(len(c)):
                    print(f"{c[i]}: {r[i]}")
            else:
                print("No data in S_BRN")

if __name__ == '__main__':
    test_company()
