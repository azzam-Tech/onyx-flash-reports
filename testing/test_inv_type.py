import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def test():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT column_name 
                FROM all_tab_columns 
                WHERE table_name = 'IAS_BILL_MST' 
                AND (column_name LIKE '%INV%' OR column_name LIKE '%TAX%' OR column_name LIKE '%TYPE%' OR column_name LIKE '%ZATCA%' OR column_name LIKE '%B2%')
            """)
            cols = [r[0] for r in cur.fetchall()]
            print("Columns:", cols)
            
            # Now let's fetch a row to see what values these columns have
            query_cols = ", ".join(cols[:40]) # limit just in case
            cur.execute(f"SELECT {query_cols} FROM IAS20261.IAS_BILL_MST WHERE ROWNUM <= 1")
            row = cur.fetchone()
            if row:
                for col, val in zip(cols, row):
                    print(f"{col}: {val}")

if __name__ == '__main__':
    test()
