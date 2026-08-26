import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def find_doc_no():
    with get_conn() as con:
        with con.cursor() as cur:
            # Show a few records from GNR_EXTRNL_DOC_SYNC to see the format of DOC_NO
            cur.execute("SELECT DOC_NO, SYNC_FLG, SYNC_DATE, DOC_TYPE FROM GNR_EXTRNL_DOC_SYNC FETCH FIRST 5 ROWS ONLY")
            res = cur.fetchall()
            print("--- GNR_EXTRNL_DOC_SYNC samples ---")
            for r in res:
                print(r)
                
            # Count rows in GNR_EXTRNL_DOC_SYNC
            cur.execute("SELECT COUNT(*) FROM GNR_EXTRNL_DOC_SYNC")
            print(f"Total rows in GNR_EXTRNL_DOC_SYNC: {cur.fetchone()[0]}")

if __name__ == '__main__':
    find_doc_no()
