import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def test_cust():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT 
                    C_CODE,
                    C_A_NAME,
                    BUILDING_NO,
                    STREET,
                    DSTRCT_NM,
                    C_ADDRESS,
                    C_BOX_CODE,
                    ADD_NO,
                    C_TAX_CODE,
                    CR_NO,
                    CSTMR_IDNTFR
                FROM IAS20261.CUSTOMER 
                WHERE C_CODE IN (1640, 2270)
            """)
            cols = [col[0] for col in cur.description]
            for r in cur.fetchall():
                print(dict(zip(cols, r)))

if __name__ == '__main__':
    test_cust()
