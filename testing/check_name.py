import os
import sys
sys.path.append(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        # Check COST_CENTERS
        cur.execute("SELECT CC_CODE, CC_A_NAME FROM IAS20261.COST_CENTERS WHERE CC_A_NAME LIKE '%الرياض العزيزية%' OR CC_A_NAME LIKE '%معاذ بن جبل%'")
        print("COST_CENTERS matches:")
        for row in cur.fetchall():
            print(row)
            
        # Check BRANCHES if table exists
        try:
            cur.execute("SELECT BRN_NO, BRN_A_NAME FROM IAS20261.BRANCHES WHERE BRN_A_NAME LIKE '%الرياض العزيزية%' OR BRN_A_NAME LIKE '%معاذ بن جبل%'")
            print("BRANCHES matches:")
            for row in cur.fetchall():
                print(row)
        except Exception as e:
            print("BRANCHES query failed:", e)
