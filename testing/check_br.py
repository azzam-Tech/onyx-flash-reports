import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_br():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT table_name 
                FROM all_tables 
                WHERE owner = 'IAS20261' AND UPPER(table_name) LIKE '%BR_MST%'
            """)
            print("Tables:")
            for r in cur.fetchall():
                t = r[0]
                print(t)
                try:
                    cur.execute(f"SELECT * FROM IAS20261.{t} FETCH FIRST 1 ROWS ONLY")
                    cols = [desc[0] for desc in cur.description]
                    print("Cols: " + ", ".join(cols))
                except Exception as e:
                    pass

if __name__ == '__main__':
    check_br()
