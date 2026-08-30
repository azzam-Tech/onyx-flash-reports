import sys
from dotenv import load_dotenv
import oracledb

sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer')
from database import get_conn

with get_conn() as conn:
    with conn.cursor() as cur:
        # Check any transaction anywhere with 3446
        cur.execute("""
            SELECT DOC_DATE, DOC_NO, DOC_TYPE, AC_CODE_DTL, REP_CODE, CC_CODE, A_CODE, DOC_DESC 
            FROM IAS_POST_DTL
            WHERE DR_AMT = 3446 OR CR_AMT = 3446 OR DR_AMT = 3446.01 OR CR_AMT = 3446.01 OR DR_AMT = 3445.99 OR CR_AMT = 3445.99
        """)
        rows = cur.fetchall()
        print("Any transaction with 3446:")
        for r in rows:
            print(r)
            
        cur.execute("""
            SELECT BILL_DATE, BILL_NO, REP_CODE, BILL_AMT
            FROM IAS_BILL_MST
            WHERE BILL_AMT = 3446 OR BILL_AMT = 3446.01 OR BILL_AMT = 3445.99
        """)
        rows = cur.fetchall()
        print("\nAny invoice with 3446:")
        for r in rows:
            print(r)
