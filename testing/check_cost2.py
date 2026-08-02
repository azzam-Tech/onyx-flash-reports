import os
import sys
sys.path.append(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute("SELECT I_CODE, I_NAME, PRIMARY_COST, INIT_PRIMARY_COST FROM IAS20261.IAS_ITM_MST WHERE ROWNUM <= 5")
        for row in cur.fetchall():
            print(row)
