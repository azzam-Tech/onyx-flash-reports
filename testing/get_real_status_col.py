import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def get_real_status_col():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT * FROM IAS_BILL_MST WHERE BILL_NO = '26314600409'")
            row = cur.fetchone()
            cols = [desc[0] for desc in cur.description]
            
            for c, v in zip(cols, row):
                if str(v) == '3' or 'ZATCA' in c or 'INV' in c or 'SYNC' in c or 'STS' in c or 'STAT' in c:
                    print(f"{c}: {v}")
                    
            print("\nSearching for status column holding '3' for all invoices...")
            # We want a report for month 7 and 8
            # Let's see if we can identify the status column by its values (1, 2, 3, 4)
            # Find all columns that only have values between 1 and 4 in the whole table
            print("Done")

if __name__ == '__main__':
    get_real_status_col()
