import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def test_dtl():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT column_name 
                FROM all_tab_columns 
                WHERE table_name = 'IAS_BILL_DTL'
            """)
            cols = [r[0] for r in cur.fetchall()]
            print("DTL cols:", cols)

if __name__ == '__main__':
    test_dtl()
