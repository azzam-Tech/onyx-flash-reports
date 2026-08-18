import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def inspect_customer(c_code):
    with get_conn() as con:
        with con.cursor() as cur:
            sql = """
                SELECT DOC_DATE, DOC_NO, DOC_SER, DOC_TYPE, DR_AMT, CR_AMT, REF_NO, DOC_POST
                FROM IAS_POST_DTL
                WHERE TO_CHAR(C_CODE) = :c_code
                AND NVL(DOC_POST,0) = 0
                ORDER BY DOC_DATE, DOC_TYPE, DOC_NO
            """
            cur.execute(sql, {'c_code': c_code})
            rows = cur.fetchall()
            
            print(f"Unposted Transactions for customer {c_code}:")
            for r in rows:
                print(r)

if __name__ == '__main__':
    inspect_customer('1911')
