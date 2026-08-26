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
                    m.TAX_BILL_TYP,
                    m.E_INVC_MTHD_NO,
                    c.C_TAX_CODE,
                    c.C_A_NAME
                FROM IAS20261.IAS_BILL_MST m
                LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = m.C_CODE
                WHERE ROWNUM <= 20
            """)
            print("BILL_NO | TAX_BILL_TYP | C_TAX_CODE | C_A_NAME")
            for r in cur.fetchall():
                print(r)

if __name__ == '__main__':
    test()
