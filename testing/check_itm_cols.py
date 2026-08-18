import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_itm_cols():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS 
                WHERE TABLE_NAME = 'IAS_ITM_MST' 
                AND COLUMN_NAME IN ('G_CODE', 'MNG_CODE', 'SUBG_CODE', 'ASSISTANT_NO', 'DETAIL_NO', 'GROUP_NO')
            """)
            print("Group columns in IAS_ITM_MST:")
            for r in cur.fetchall():
                print(r[0])

if __name__ == '__main__':
    check_itm_cols()
