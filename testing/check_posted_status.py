import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_posted_status():
    with get_conn() as con:
        with con.cursor() as cur:
            # Check BILL_POST status for invoices > Aug 11
            cur.execute("""
                SELECT NVL(BILL_POST, 0), COUNT(*) 
                FROM IAS_BILL_MST 
                WHERE BILL_DATE > TO_DATE('2026-08-11', 'YYYY-MM-DD')
                GROUP BY NVL(BILL_POST, 0)
            """)
            print("--- Post Status for Invoices after Aug 11 ---")
            for r in cur.fetchall():
                print(f"BILL_POST {r[0]}: {r[1]} invoices")
                
            # Check BILL_POST status for invoices <= Aug 11
            cur.execute("""
                SELECT NVL(BILL_POST, 0), COUNT(*) 
                FROM IAS_BILL_MST 
                WHERE BILL_DATE <= TO_DATE('2026-08-11', 'YYYY-MM-DD')
                  AND BILL_DATE >= TO_DATE('2026-08-01', 'YYYY-MM-DD')
                GROUP BY NVL(BILL_POST, 0)
            """)
            print("\n--- Post Status for Invoices Aug 1 - Aug 11 ---")
            for r in cur.fetchall():
                print(f"BILL_POST {r[0]}: {r[1]} invoices")

if __name__ == '__main__':
    check_posted_status()
