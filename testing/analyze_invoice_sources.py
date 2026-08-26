import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def analyze_sources():
    with get_conn() as con:
        with con.cursor() as cur:
            # Query for DOC_TYPE = 4
            cur.execute("""
                SELECT ADD_USER, COUNT(*) 
                FROM IAS_BILL_MST 
                WHERE BILL_DOC_TYPE = 4 
                GROUP BY ADD_USER 
                ORDER BY COUNT(*) DESC FETCH FIRST 5 ROWS ONLY
            """)
            type_4_users = cur.fetchall()
            
            # Query for DOC_TYPE = 1
            cur.execute("""
                SELECT ADD_USER, COUNT(*) 
                FROM IAS_BILL_MST 
                WHERE BILL_DOC_TYPE = 1 
                GROUP BY ADD_USER 
                ORDER BY COUNT(*) DESC FETCH FIRST 5 ROWS ONLY
            """)
            type_1_users = cur.fetchall()

            print("--- Users creating DOC_TYPE 4 (9898 invoices) ---")
            for u in type_4_users:
                print(f"User: {u[0]}, Count: {u[1]}")
                
            print("\n--- Users creating DOC_TYPE 1 (2858 invoices) ---")
            for u in type_1_users:
                print(f"User: {u[0]}, Count: {u[1]}")

if __name__ == '__main__':
    analyze_sources()
