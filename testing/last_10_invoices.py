import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'zatca_printer')))
from dotenv import load_dotenv
load_dotenv(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'zatca_printer', '.env')))
from app.database import get_conn

def get_last_10_invoices():
    print("Connecting to the database...")
    try:
        # Using read-only connection via RPT_USER
        conn = get_conn(readonly=True)
        cur = conn.cursor()
        
        # Query to fetch the last 10 invoices ordered by BILL_NO
        sql = """
            SELECT * FROM (
                SELECT BILL_NO, DOC_SER_EXTRNL, BILL_DOC_TYPE, BILL_DATE, BILL_AMT, C_CODE 
                FROM IAS20261.IAS_BILL_MST 
                ORDER BY AD_DATE DESC
            ) WHERE ROWNUM <= 10
        """
        
        cur.execute(sql)
        rows = cur.fetchall()
        
        print("\n--- Last 10 Invoices ---")
        print(f"{'BILL_NO':<10} | {'DOC_SER':<15} | {'DOC_TYPE':<10} | {'DATE':<20} | {'AMOUNT':<10} | {'C_CODE':<10}")
        print("-" * 85)
        
        for r in rows:
            bill_no = r[0]
            bill_ser = r[1]
            doc_type = "Cash (1)" if r[2] == 1 else "Credit (4)" if r[2] == 4 else r[2]
            doc_date = r[3].strftime('%Y-%m-%d') if r[3] else 'N/A'
            bill_amt = r[4]
            c_code = r[5] or 'N/A'
            
            print(f"{bill_no:<10} | {bill_ser:<15} | {doc_type:<10} | {doc_date:<20} | {bill_amt:<10} | {c_code:<10}")
            
    except Exception as e:
        print(f"Error fetching invoices: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    get_last_10_invoices()
