import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_doc_types():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT BILL_DOC_TYPE, MAX(BILL_DATE), COUNT(*) 
                FROM IAS_BILL_MST 
                WHERE BILL_DATE >= TO_DATE('2026-08-01', 'YYYY-MM-DD')
                GROUP BY BILL_DOC_TYPE
            """)
            print("--- Max Date by DOC_TYPE in August ---")
            for r in cur.fetchall():
                print(f"Doc Type {r[0]}: Max Date = {r[1]}, Total in Aug = {r[2]}")

if __name__ == '__main__':
    check_doc_types()
