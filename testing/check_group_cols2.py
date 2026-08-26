import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_cols():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT * FROM IAS_ITM_MST FETCH FIRST 1 ROWS ONLY")
            cols = [desc[0] for desc in cur.description]
            print("Group Columns in IAS_ITM_MST:")
            for c in cols:
                if 'GRP' in c or 'G_' in c or 'CODE' in c:
                    print(c)

if __name__ == '__main__':
    check_cols()
