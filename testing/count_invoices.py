import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def count_invoices():
    with get_conn() as con:
        with con.cursor() as cur:
            # Group by BILL_DOC_TYPE to see types of bills
            query = """
                SELECT BILL_DOC_TYPE, COUNT(*)
                FROM IAS_BILL_MST
                GROUP BY BILL_DOC_TYPE
                ORDER BY COUNT(*) DESC
            """
            cur.execute(query)
            res = cur.fetchall()
            
            print("--- Bill Counts by Type ---")
            total = 0
            for row in res:
                doc_type, count = row
                print(f"Doc Type {doc_type}: {count} invoices")
                total += count
            print(f"Total bills: {total}")
            
            # Check maximum date to verify up to when it's counted
            cur.execute("SELECT MAX(BILL_DATE) FROM IAS_BILL_MST")
            max_date = cur.fetchone()[0]
            print(f"Latest invoice date: {max_date.strftime('%Y-%m-%d') if max_date else 'Unknown'}")

if __name__ == '__main__':
    count_invoices()
