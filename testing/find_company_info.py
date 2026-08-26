import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def find_company_info():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT table_name 
                FROM all_tables 
                WHERE owner LIKE '%2026%' 
                  AND (UPPER(table_name) LIKE '%COM_MST%' OR UPPER(table_name) LIKE '%BR_MST%' OR UPPER(table_name) LIKE '%COMPANY%')
            """)
            print("--- Possible Company Tables ---")
            for r in cur.fetchall():
                t = r[0]
                try:
                    cur.execute(f"SELECT * FROM {t} FETCH FIRST 1 ROWS ONLY")
                    cols = [desc[0] for desc in cur.description]
                    print(f"\n{t} columns:")
                    print(", ".join(cols))
                except Exception as e:
                    pass

if __name__ == '__main__':
    find_company_info()
