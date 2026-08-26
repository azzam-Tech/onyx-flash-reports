import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def test():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT 
                    m.BILL_NO, 
                    m.C_NAME,
                    c.C_A_NAME,
                    c.C_ADDRESS
                FROM IAS20261.IAS_BILL_MST m
                LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = m.C_CODE
                WHERE m.BILL_NO = '2614201611'
            """)
            print(cur.fetchone())

if __name__ == '__main__':
    test()
