import os
import sys
sys.path.append(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute("SELECT DISTINCT CC_CODE FROM IAS20261.IAS_POST_DTL WHERE SUBSTR(A_CODE, 1, 5) = '41101'")
        print("CC_CODEs for revenue:")
        for row in cur.fetchall():
            print(row)
