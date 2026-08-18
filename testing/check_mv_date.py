import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_mv_date():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS 
                WHERE TABLE_NAME = 'ITEM_MOVEMENT' 
                AND COLUMN_NAME LIKE '%DATE%'
            """)
            print("Date columns in ITEM_MOVEMENT:")
            for r in cur.fetchall():
                print(r[0])
                
            cur.execute("""
                SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS 
                WHERE TABLE_NAME = 'IAS_BILL_MST' 
                AND COLUMN_NAME LIKE '%DATE%'
            """)
            print("\nDate columns in IAS_BILL_MST:")
            for r in cur.fetchall():
                print(r[0])

if __name__ == '__main__':
    check_mv_date()
