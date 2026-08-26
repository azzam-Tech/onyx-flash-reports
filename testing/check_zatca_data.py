import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_zatca_data():
    with get_conn() as con:
        with con.cursor() as cur:
            # Check how many invoices have DOC_HASH populated
            query = """
                SELECT BILL_DOC_TYPE, 
                       COUNT(*) as total_bills,
                       SUM(CASE WHEN DOC_HASH IS NOT NULL AND DOC_HASH != ' ' THEN 1 ELSE 0 END) as has_hash,
                       SUM(CASE WHEN WEB_SRVC_UUID IS NOT NULL AND WEB_SRVC_UUID != ' ' THEN 1 ELSE 0 END) as has_uuid
                FROM IAS_BILL_MST
                GROUP BY BILL_DOC_TYPE
            """
            cur.execute(query)
            res = cur.fetchall()
            
            print("--- ZATCA Data Population in IAS_BILL_MST ---")
            for row in res:
                doc_type, total, has_hash, has_uuid = row
                print(f"Doc Type: {doc_type} | Total Invoices: {total} | Has Hash: {has_hash} | Has UUID: {has_uuid}")
                
            # If we want to check an example
            print("\n--- Examples of ZATCA fields (Doc Type 1) ---")
            cur.execute("""
                SELECT BILL_NO, DOC_HASH, WEB_SRVC_UUID 
                FROM IAS_BILL_MST 
                WHERE BILL_DOC_TYPE = 1 AND DOC_HASH IS NOT NULL AND DOC_HASH != ' '
                FETCH FIRST 2 ROWS ONLY
            """)
            examples = cur.fetchall()
            for r in examples:
                print(f"Bill No: {r[0]} \nHash: {r[1]} \nUUID: {r[2]}\n")

if __name__ == '__main__':
    check_zatca_data()
