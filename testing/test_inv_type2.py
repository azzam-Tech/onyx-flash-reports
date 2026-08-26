import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def test():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT DISTINCT TAX_BILL_TYP, COUNT(*) 
                FROM IAS20261.IAS_BILL_MST 
                GROUP BY TAX_BILL_TYP
            """)
            print("TAX_BILL_TYP distribution:")
            for r in cur.fetchall():
                print(r)
                
            cur.execute("""
                SELECT DISTINCT E_INVC_MTHD_NO, COUNT(*) 
                FROM IAS20261.IAS_BILL_MST 
                GROUP BY E_INVC_MTHD_NO
            """)
            print("\nE_INVC_MTHD_NO distribution:")
            for r in cur.fetchall():
                print(r)

if __name__ == '__main__':
    test()
