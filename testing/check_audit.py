import os
import sys
import json
from dotenv import load_dotenv
import oracledb

sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer')
from database import get_conn

with get_conn() as conn:
    with conn.cursor() as cur:
        # Check if audit table exists and has 3446
        try:
            cur.execute("""
                SELECT DOC_DATE, DOC_NO, DR_AMT, CR_AMT, DEL_DATE 
                FROM IAS_POST_DTL_AUDIT 
                WHERE (DR_AMT = 3446 OR CR_AMT = 3446)
            """)
            print("Audit:", cur.fetchall())
        except Exception as e:
            print("No IAS_POST_DTL_AUDIT:", e)

        # Let's search for 3446 in ALL tables just in case
        # Or look at unposted transactions in August for rep 144 to see if there's a sum close to 3446
        cur.execute("""
            SELECT SUM(NVL(DR_AMT,0)) - SUM(NVL(CR_AMT,0))
            FROM IAS_POST_DTL
            WHERE AC_CODE_DTL = '144' AND DOC_POST = 0
        """)
        net_unposted = cur.fetchone()[0]
        print(f"Net unposted for 144: {net_unposted}")
