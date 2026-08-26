import os
import sys
import datetime

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def build_zatca_report():
    with get_conn() as con:
        with con.cursor() as cur:
            # First verify the WEB_SRVC_TRNSFR_DATA_FLG values
            cur.execute("""
                SELECT WEB_SRVC_TRNSFR_DATA_FLG, COUNT(*) 
                FROM IAS_BILL_MST 
                WHERE BILL_DATE >= TO_DATE('2026-07-01', 'YYYY-MM-DD') 
                GROUP BY WEB_SRVC_TRNSFR_DATA_FLG
            """)
            counts = cur.fetchall()
            print("WEB_SRVC_TRNSFR_DATA_FLG distribution for M7 and M8:")
            for c in counts:
                print(c)
                
            cur.execute("SELECT WEB_SRVC_TRNSFR_DATA_FLG FROM IAS_BILL_MST WHERE BILL_NO = '26314600409'")
            print("Status for 26314600409:", cur.fetchone()[0])
            
            # Now build a clean markdown table of all invoices grouped by this status
            # Wait, the user wants the list of invoices. Since there are thousands, I will group them by day and status, or create a detailed CSV.
            # I will create an artifact with the summary.

if __name__ == '__main__':
    build_zatca_report()
