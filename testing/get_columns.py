import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def get_columns():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT column_name FROM all_tab_columns WHERE table_name = 'IAS_BILL_MST'")
            cols = [r[0] for r in cur.fetchall()]
            for c in cols:
                if 'TAX' in c or 'VAT' in c or 'VAL' in c or 'AMT' in c:
                    print(c)

if __name__ == '__main__':
    get_columns()
