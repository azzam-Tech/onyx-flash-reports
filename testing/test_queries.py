import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def test_queries():
    with get_conn() as con:
        with con.cursor() as cur:
            # Check IAS_BILL_DTL
            cur.execute("""
                SELECT column_name 
                FROM all_tab_columns 
                WHERE table_name = 'IAS_BILL_DTL'
            """)
            cols = [r[0] for r in cur.fetchall()]
            print("IAS_BILL_DTL columns:", [c for c in cols if 'ITEM' in c or 'QTY' in c or 'PRICE' in c or 'AMT' in c or 'TAX' in c])
            
            # Check customer table
            cur.execute("""
                SELECT table_name FROM all_tables WHERE UPPER(table_name) LIKE '%CST_MST%' AND owner LIKE '%2026%'
            """)
            cst_tables = [r[0] for r in cur.fetchall()]
            print("Customer tables:", cst_tables)

if __name__ == '__main__':
    test_queries()
