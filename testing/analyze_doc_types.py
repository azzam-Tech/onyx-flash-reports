import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_bill_types():
    with get_conn() as con:
        with con.cursor() as cur:
            query = """
                SELECT BILL_DOC_TYPE, 
                       COUNT(*) as cnt,
                       SUM(NET_AMT) as total_amount
                FROM IAS_BILL_MST
                GROUP BY BILL_DOC_TYPE
            """
            cur.execute(query)
            res = cur.fetchall()
            
            for row in res:
                print(f"Doc Type: {row[0]}, Count: {row[1]}, Total Net Amount: {row[2]:,.2f}")

if __name__ == '__main__':
    check_bill_types()
