import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def find_schemas():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT DISTINCT owner FROM all_tables WHERE owner LIKE '%2026%'")
            print("Schemas:")
            for r in cur.fetchall():
                print(r[0])

if __name__ == '__main__':
    find_schemas()
