import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def show_zatca_cols():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT column_name FROM all_tab_columns WHERE table_name = 'IAS_BILL_MST'")
            cols = [c[0] for c in cur.fetchall()]
            
            query = "SELECT * FROM IAS_BILL_MST WHERE BILL_NO = '26314600409'"
            cur.execute(query)
            row = cur.fetchone()
            
            if row:
                print("--- ALL DATA for 26314600409 ---")
                for c, v in zip(cols, row):
                    if v is not None and str(v).strip():
                        print(f"{c}: {v}")
            else:
                print("Not found")

if __name__ == '__main__':
    show_zatca_cols()
