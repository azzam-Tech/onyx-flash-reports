import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def test_time():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT 
                    AD_DATE_CLK,
                    TO_CHAR(POST_DATE, 'HH:MI:SS AM'),
                    TO_CHAR(AD_DATE, 'HH:MI:SS AM')
                FROM IAS20261.IAS_BILL_MST 
                WHERE BILL_NO = '26314600476'
            """)
            print("Time Data 476:", cur.fetchone())

if __name__ == '__main__':
    test_time()
