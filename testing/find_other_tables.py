import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def find_other_tables():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT table_name FROM all_tables WHERE table_name LIKE '%BILL_MST%' AND table_name NOT LIKE '%V_%'")
            tables = [r[0] for r in cur.fetchall()]
            for t in tables:
                try:
                    cur.execute(f"SELECT MAX(BILL_DATE), COUNT(*) FROM {t}")
                    res = cur.fetchone()
                    print(f"Table {t}: Max Date = {res[0]}, Count = {res[1]}")
                except Exception as e:
                    print(f"Error querying {t}: {e}")

if __name__ == '__main__':
    find_other_tables()
