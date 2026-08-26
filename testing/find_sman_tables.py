import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def find_sman_tables():
    with get_conn() as con:
        with con.cursor() as cur:
            # Look for ANY table with SMAN and BILL or INV
            cur.execute("""
                SELECT table_name 
                FROM all_tables 
                WHERE owner LIKE '%2026%' 
                  AND (UPPER(table_name) LIKE '%SMAN%' OR UPPER(table_name) LIKE '%DTS%' OR UPPER(table_name) LIKE '%VAN%')
                  AND UPPER(table_name) LIKE '%MST%'
            """)
            print("--- Distribution/Salesman Tables ---")
            for r in cur.fetchall():
                t = r[0]
                try:
                    cur.execute(f"SELECT COUNT(*) FROM {t}")
                    cnt = cur.fetchone()[0]
                    if cnt > 0:
                        print(f"{t}: {cnt} rows")
                except:
                    pass

if __name__ == '__main__':
    find_sman_tables()
