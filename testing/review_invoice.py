import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def review_invoice(bill_no):
    with get_conn() as con:
        with con.cursor() as cur:
            # Get main info
            query = """
                SELECT BILL_NO, BILL_DATE, BILL_DOC_TYPE, DOC_HASH, WEB_SRVC_UUID, C_CODE
                FROM IAS_BILL_MST
                WHERE BILL_NO = :1
            """
            cur.execute(query, [bill_no])
            res = cur.fetchall()
            
            if not res:
                print(f"Invoice {bill_no} not found in IAS_BILL_MST.")
                return
                
            for row in res:
                print("--- Invoice Details ---")
                print(f"Bill No:      {row[0]}")
                print(f"Date:         {row[1]}")
                print(f"Doc Type:     {row[2]}")
                print(f"Customer:     {row[5]}")
                print(f"ZATCA Hash:   {row[3]}")
                print(f"ZATCA UUID:   {row[4]}")
                print("-----------------------\n")
                
            # Get details count
            cur.execute("SELECT COUNT(*), SUM(I_QTY) FROM IAS_BILL_DTL WHERE BILL_NO = :1", [bill_no])
            dtl_res = cur.fetchone()
            print(f"Total items in invoice: {dtl_res[0]}")
            print(f"Total quantity: {dtl_res[1]}")

if __name__ == '__main__':
    review_invoice('26314600409')
