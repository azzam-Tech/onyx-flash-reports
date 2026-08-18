import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_inactive():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT NVL(INACTIVE, 0), COUNT(*) FROM IAS_ITM_MST WHERE G_CODE = '003' GROUP BY NVL(INACTIVE, 0)")
            for r in cur.fetchall():
                status = "Active" if r[0] == 0 else "Inactive (Suspended)"
                print(f"{status}: {r[1]}")

if __name__ == '__main__':
    check_inactive()
