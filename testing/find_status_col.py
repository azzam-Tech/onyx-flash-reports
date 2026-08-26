import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def find_status_col():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT * FROM IAS_BILL_MST WHERE BILL_NO = '26314600409'")
            row = cur.fetchone()
            cols = [desc[0] for desc in cur.description]
            
            print("Columns with value 3 for this invoice:")
            for c, v in zip(cols, row):
                if str(v) == '3' or str(v) == '3.0':
                    print(f"{c}: {v}")

if __name__ == '__main__':
    find_status_col()
