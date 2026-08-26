import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def find_invoice_details():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT BILL_NO, TO_CHAR(BILL_DATE, 'YYYY-MM-DD'), BILL_TIME, BILL_AMT, BILL_TAX_AMT 
                FROM IAS_BILL_MST 
                WHERE BILL_DATE = TO_DATE('2026-08-08', 'YYYY-MM-DD')
                  AND BILL_AMT = 11500
            """)
            print("--- Invoice Details ---")
            for r in cur.fetchall():
                print(r)

if __name__ == '__main__':
    find_invoice_details()
