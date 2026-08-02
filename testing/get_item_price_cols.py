import sys
sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute("SELECT * FROM IAS20261.IAS_ITEM_PRICE WHERE ROWNUM <= 1")
        cols = [d[0] for d in cur.description]
        print("IAS_ITEM_PRICE COLUMNS:", cols)
        row = cur.fetchone()
        print("Sample row:", row)
