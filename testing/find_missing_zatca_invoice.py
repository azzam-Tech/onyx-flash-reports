import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def find_missing_zatca():
    with get_conn() as con:
        with con.cursor() as cur:
            query = """
                SELECT BILL_NO, BILL_DATE
                FROM IAS_BILL_MST
                WHERE BILL_DOC_TYPE = 1 
                  AND (DOC_HASH IS NULL OR DOC_HASH = ' ' OR DOC_HASH = '')
            """
            cur.execute(query)
            res = cur.fetchall()
            
            if res:
                for row in res:
                    bill_no, bill_date = row
                    print(f"Bill No: {bill_no}, Date: {bill_date}")
            else:
                print("No missing ZATCA invoices found.")

if __name__ == '__main__':
    find_missing_zatca()
