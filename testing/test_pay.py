import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def test_pay():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT column_name 
                FROM all_tab_columns 
                WHERE table_name = 'IAS_BILL_MST'
            """)
            cols = [r[0] for r in cur.fetchall()]
            
            # Print columns containing terms like TYPE, PAY, TERM, MTHD, CSH, CRDT
            matches = [c for c in cols if 'PAY' in c or 'TYPE' in c or 'TERM' in c or 'BILL_TYP' in c or 'FLG' in c or 'MTHD' in c]
            print("Possible Payment Columns:", matches)

if __name__ == '__main__':
    test_pay()
