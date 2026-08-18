import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_groups():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS 
                WHERE TABLE_NAME = 'GROUP_DETAILS' 
            """)
            print("Columns in GROUP_DETAILS:")
            for r in cur.fetchall():
                print(r[0])
            
            print("-" * 30)
            cur.execute("""
                SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS 
                WHERE TABLE_NAME = 'IAS_DETAIL_GROUP' 
            """)
            print("Columns in IAS_DETAIL_GROUP:")
            for r in cur.fetchall():
                print(r[0])
                
            print("-" * 30)
            cur.execute("""
                SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS 
                WHERE TABLE_NAME = 'IAS_ITM_MST' AND COLUMN_NAME LIKE '%GROUP%'
            """)
            print("Group columns in IAS_ITM_MST:")
            for r in cur.fetchall():
                print(r[0])

if __name__ == '__main__':
    check_groups()
