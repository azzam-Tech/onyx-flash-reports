import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def test_sitype():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT BILL_NO, SI_TYPE
                FROM IAS20261.IAS_BILL_MST 
                WHERE BILL_NO IN ('26314600476', '26314600409')
            """)
            print("SI_TYPE:", cur.fetchall())

if __name__ == '__main__':
    test_sitype()
