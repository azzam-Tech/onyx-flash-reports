import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def find_zatca_column():
    with get_conn() as con:
        with con.cursor() as cur:
            # We need to get columns ordered by COLUMN_ID to map them correctly to fetchall()!
            cur.execute("""
                SELECT column_name 
                FROM all_tab_columns 
                WHERE table_name = 'IAS_BILL_MST' 
                ORDER BY column_id
            """)
            cols = [c[0] for c in cur.fetchall()]
            
            cur.execute("SELECT * FROM IAS_BILL_MST WHERE BILL_NO = '26314600409'")
            row = cur.fetchone()
            
            if row:
                print("--- Correct mapping for 26314600409 ---")
                for c, v in zip(cols, row):
                    if str(v) == '3' or 'ZATCA' in c or 'SYNC' in c or 'E_INV' in c or 'HASH' in c or 'UUID' in c:
                        print(f"{c}: {v}")
            else:
                print("Not found")

if __name__ == '__main__':
    find_zatca_column()
