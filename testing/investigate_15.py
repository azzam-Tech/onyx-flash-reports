import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def find_ref():
    with get_conn() as con:
        with con.cursor() as cur:
            sql = """
                SELECT RT_BILL_NO, BILL_NO, BILL_SER, BILL_DOC_TYPE 
                FROM IAS_RT_BILL_DTL 
                WHERE RT_BILL_NO = 2621120116
            """
            cur.execute(sql)
            for r in cur.fetchall():
                print("IAS_RT_BILL_DTL:", r)
                
            sql2 = """
                SELECT DOC_NO, DOC_NO_REF, REF_NO FROM IAS_POST_DTL WHERE DOC_TYPE = 5 AND C_CODE = '2051'
            """
            cur.execute(sql2)
            for r in cur.fetchall():
                print("IAS_POST_DTL TYPE 5:", r)

if __name__ == '__main__':
    find_ref()
