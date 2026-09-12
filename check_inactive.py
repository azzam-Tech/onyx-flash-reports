import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'privet', 'onyx_reports'))
from database import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute("SELECT NVL(INACTIVE, 0), NVL(INACTIVE_SALES, 0), COUNT(*) FROM CUSTOMER GROUP BY NVL(INACTIVE, 0), NVL(INACTIVE_SALES, 0)")
        print("INACTIVE, INACTIVE_SALES, COUNT")
        for row in cur.fetchall():
            print(row)
