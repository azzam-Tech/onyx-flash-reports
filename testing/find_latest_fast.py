import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def find_latest_fast():
    with get_conn() as con:
        with con.cursor() as cur:
            # First, double check IAS_BILL_MST
            cur.execute("SELECT MAX(BILL_DATE), COUNT(*) FROM IAS_BILL_MST")
            res = cur.fetchone()
            print(f"IAS_BILL_MST: Max Date = {res[0]}, Total Rows = {res[1]}")
            
            # Check POS_BILL_MST
            try:
                cur.execute("SELECT MAX(BILL_DATE), COUNT(*) FROM POS_BILL_MST")
                res = cur.fetchone()
                print(f"POS_BILL_MST: Max Date = {res[0]}, Total Rows = {res[1]}")
            except:
                print("POS_BILL_MST not found")
                
            # Check IAS_SMAN_BILL_MST
            try:
                cur.execute("SELECT MAX(BILL_DATE), COUNT(*) FROM IAS_SMAN_BILL_MST")
                res = cur.fetchone()
                print(f"IAS_SMAN_BILL_MST: Max Date = {res[0]}, Total Rows = {res[1]}")
            except:
                print("IAS_SMAN_BILL_MST not found")
                
            # Count invoices after Aug 11 in IAS_BILL_MST
            cur.execute("SELECT COUNT(*) FROM IAS_BILL_MST WHERE BILL_DATE > TO_DATE('2026-08-11', 'YYYY-MM-DD')")
            print(f"Count > Aug 11 in IAS_BILL_MST: {cur.fetchone()[0]}")

if __name__ == '__main__':
    find_latest_fast()
