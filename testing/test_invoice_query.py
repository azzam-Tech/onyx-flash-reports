import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def test_query():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT column_name 
                FROM all_tab_columns 
                WHERE table_name = 'IAS_BILL_MST'
            """)
            cols = [r[0] for r in cur.fetchall()]
            print("TIME cols:", [c for c in cols if 'TIME' in c or 'DOC' in c or 'DATE' in c])

if __name__ == '__main__':
    test_query()
