import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def find_gnr_tables():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT owner, table_name 
                FROM all_tables 
                WHERE UPPER(table_name) LIKE '%COM_MST%' 
                   OR UPPER(table_name) LIKE '%BR_MST%'
                   OR UPPER(table_name) LIKE '%CMPNY%'
            """)
            print("--- Possible Company Tables ---")
            for r in cur.fetchall():
                owner, t = r
                print(f"{owner}.{t}")

if __name__ == '__main__':
    find_gnr_tables()
