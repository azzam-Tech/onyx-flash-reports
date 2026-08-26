import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def show_aug23_invoices():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT BILL_NO, TO_CHAR(BILL_DATE, 'YYYY-MM-DD'), BILL_AMT 
                FROM IAS_BILL_MST 
                WHERE BILL_DATE = TO_DATE('2026-08-23', 'YYYY-MM-DD')
                FETCH FIRST 5 ROWS ONLY
            """)
            print("--- Invoices from 2026-08-23 ---")
            for r in cur.fetchall():
                print(r)

if __name__ == '__main__':
    show_aug23_invoices()
