import os
import sys
import codecs
sys.path.append(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute("SELECT CC_CODE, CC_A_NAME FROM IAS20261.COST_CENTERS WHERE CC_CODE = 144")
        with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\out_names.txt", "w", "utf-8") as f:
            for row in cur.fetchall():
                f.write(f"CC: {row}\n")
            
            cur.execute("SELECT REPRS_CODE, REPRS_A_NAME FROM IAS20261.SALES_MAN WHERE REPRS_CODE = 144")
            for row in cur.fetchall():
                f.write(f"REP: {row}\n")
