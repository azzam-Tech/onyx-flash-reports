import os
import sys
import json
from dotenv import load_dotenv
import oracledb

sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer')
from database import get_conn

with get_conn() as conn:
    with conn.cursor() as cur:
        # Check balance for posted only
        cur.execute("""
            SELECT SUM(NVL(DR_AMT,0)) - SUM(NVL(CR_AMT,0)) as BALANCE
            FROM IAS_POST_DTL
            WHERE A_CODE = '111010101' AND AC_CODE_DTL = '144' AND NVL(DOC_POST,0) = 1
        """)
        bal_posted = cur.fetchone()[0]

        # Check balance for all (posted and unposted)
        cur.execute("""
            SELECT SUM(NVL(DR_AMT,0)) - SUM(NVL(CR_AMT,0)) as BALANCE
            FROM IAS_POST_DTL
            WHERE A_CODE = '111010101' AND AC_CODE_DTL = '144'
        """)
        bal_all = cur.fetchone()[0]

        # Check balance specifically up to 2026-08-30
        cur.execute("""
            SELECT SUM(NVL(DR_AMT,0)) - SUM(NVL(CR_AMT,0)) as BALANCE
            FROM IAS_POST_DTL
            WHERE A_CODE = '111010101' AND AC_CODE_DTL = '144' AND NVL(DOC_POST,0) = 1
              AND DOC_DATE <= TO_DATE('2026-08-30', 'YYYY-MM-DD')
        """)
        bal_posted_date = cur.fetchone()[0]

        # Check balance all up to 2026-08-30
        cur.execute("""
            SELECT SUM(NVL(DR_AMT,0)) - SUM(NVL(CR_AMT,0)) as BALANCE
            FROM IAS_POST_DTL
            WHERE A_CODE = '111010101' AND AC_CODE_DTL = '144'
              AND DOC_DATE <= TO_DATE('2026-08-30', 'YYYY-MM-DD')
        """)
        bal_all_date = cur.fetchone()[0]

        print(f"Posted Balance: {bal_posted}")
        print(f"All Balance (incl unposted): {bal_all}")
        print(f"Posted Balance up to 30/08: {bal_posted_date}")
        print(f"All Balance up to 30/08: {bal_all_date}")

        # Let's get the sum of DR and CR for August (month 8)
        cur.execute("""
            SELECT SUM(NVL(DR_AMT,0)), SUM(NVL(CR_AMT,0))
            FROM IAS_POST_DTL
            WHERE A_CODE = '111010101' AND AC_CODE_DTL = '144'
              AND EXTRACT(MONTH FROM DOC_DATE) = 8
        """)
        dr_aug, cr_aug = cur.fetchone()
        print(f"August DR: {dr_aug}, CR: {cr_aug}, Net Aug: {(dr_aug or 0) - (cr_aug or 0)}")
