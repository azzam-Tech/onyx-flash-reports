import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def find_dist_tables():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT table_name 
                FROM all_tables 
                WHERE owner LIKE '%2026%'
                  AND (
                      UPPER(table_name) LIKE '%DTS%' OR 
                      UPPER(table_name) LIKE '%SMAN%' OR 
                      UPPER(table_name) LIKE '%VAN%' OR 
                      UPPER(table_name) LIKE '%PDA%' OR 
                      UPPER(table_name) LIKE '%SFA%' OR
                      UPPER(table_name) LIKE '%MOB%'
                  )
            """)
            print("--- Possible Distribution Tables ---")
            for r in cur.fetchall():
                t = r[0]
                if 'BILL' in t or 'INV' in t or 'SLS' in t or 'SALES' in t or 'DOC' in t:
                    try:
                        cur.execute(f"SELECT COUNT(*) FROM {t}")
                        cnt = cur.fetchone()[0]
                        print(f"{t}: {cnt} rows")
                    except:
                        pass

if __name__ == '__main__':
    find_dist_tables()
