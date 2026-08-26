import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_cols():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT column_name FROM all_tab_columns WHERE table_name = 'IAS_ITM_MST' AND column_name LIKE '%GRP%' OR column_name LIKE '%CODE%'")
            cols = cur.fetchall()
            print("Columns in IAS_ITM_MST:")
            for c in cols:
                print(c[0])

if __name__ == '__main__':
    check_cols()
