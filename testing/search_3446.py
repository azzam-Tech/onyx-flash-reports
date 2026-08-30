import os
import sys
import json
from dotenv import load_dotenv
import oracledb

sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer')
from database import get_conn

results = []
with get_conn() as conn:
    with conn.cursor() as cur:
        # Search in IAS_POST_DTL for close matches
        cur.execute("""
            SELECT DOC_DATE, DOC_NO, DOC_TYPE, DR_AMT, CR_AMT, DOC_DESC 
            FROM IAS_POST_DTL
            WHERE ( (DR_AMT >= 3445 AND DR_AMT <= 3447) OR (CR_AMT >= 3445 AND CR_AMT <= 3447) )
              AND (AC_CODE_DTL = '144' OR TO_CHAR(REP_CODE) = '144' OR A_CODE = '111010101')
        """)
        rows = cur.fetchall()
        print("--- Close matches in IAS_POST_DTL (3445 to 3447) ---")
        for r in rows: print(r)

        # Search in IAS_BILL_MST
        cur.execute("""
            SELECT BILL_DATE, BILL_NO, BILL_AMT
            FROM IAS_BILL_MST
            WHERE (BILL_AMT >= 3445 AND BILL_AMT <= 3447)
              AND TO_CHAR(REP_CODE) = '144'
        """)
        rows = cur.fetchall()
        print("\n--- Close matches in IAS_BILL_MST ---")
        for r in rows: print(r)
        
        # Are there any unposted receipts?
        cur.execute("""
            SELECT DOC_DATE, DOC_NO, DOC_TYPE, DR_AMT, CR_AMT, DOC_DESC 
            FROM IAS_POST_DTL
            WHERE DOC_POST = 0
              AND (AC_CODE_DTL = '144' OR TO_CHAR(REP_CODE) = '144' OR A_CODE = '111010101')
        """)
        rows = cur.fetchall()
        print("\n--- All Unposted Transactions for 144 ---")
        for r in rows: print(r)

