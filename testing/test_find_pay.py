import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def test_find_pay():
    with get_conn() as con:
        with con.cursor() as cur:
            # Check for any columns with value 2 (since 1 is often cash, 2 is credit)
            # Or just fetch diff between the two bills
            cur.execute("""
                SELECT * FROM IAS20261.IAS_BILL_MST WHERE BILL_NO = '26314600476'
            """)
            cols = [col[0] for col in cur.description]
            row_476 = cur.fetchone()
            
            cur.execute("""
                SELECT * FROM IAS20261.IAS_BILL_MST WHERE BILL_NO = '26314600409'
            """)
            row_409 = cur.fetchone()
            
            # Print columns that are different between the two invoices
            if row_476 and row_409:
                for i in range(len(cols)):
                    if row_476[i] != row_409[i]:
                        print(f"Diff - {cols[i]}: 476={row_476[i]} vs 409={row_409[i]}")

if __name__ == '__main__':
    test_find_pay()
