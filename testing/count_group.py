import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def count_group():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM IAS_ITM_MST WHERE G_CODE = '003'")
            print("Items with G_CODE '003':", cur.fetchone()[0])

if __name__ == '__main__':
    count_group()
