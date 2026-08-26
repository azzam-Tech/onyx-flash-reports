import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def explore_zatca_schema():
    with get_conn() as con:
        with con.cursor() as cur:
            # Look for ANY table across ALL schemas that has ZATCA or FATOORA in the name
            cur.execute("""
                SELECT owner, table_name 
                FROM all_tables 
                WHERE UPPER(table_name) LIKE '%ZATCA%' 
                   OR UPPER(table_name) LIKE '%FATOORA%'
                   OR UPPER(table_name) LIKE '%E_INV%'
            """)
            print("--- ZATCA/FATOORA related tables across all schemas ---")
            for r in cur.fetchall():
                print(f"{r[0]}.{r[1]}")
                
            # Look for integration tables in IAS20261 that might have status
            cur.execute("""
                SELECT table_name 
                FROM all_tables 
                WHERE owner LIKE '%2026%' 
                  AND (UPPER(table_name) LIKE '%SYNC%' OR UPPER(table_name) LIKE '%EXTRNL%')
            """)
            print("\n--- SYNC related tables in 2026 schema ---")
            for r in cur.fetchall():
                print(r[0])
                
            # Look for columns in IAS_BILL_MST with distinct values (1, 2, 3, 4)
            print("\n--- Checking IAS_BILL_MST columns for 1,2,3,4 distribution ---")
            cur.execute("SELECT column_name FROM all_tab_columns WHERE table_name = 'IAS_BILL_MST'")
            cols = [r[0] for r in cur.fetchall()]
            for c in cols:
                if 'STAT' in c or 'STS' in c or 'FLG' in c or 'TYP' in c:
                    try:
                        cur.execute(f"SELECT {c}, COUNT(*) FROM IAS_BILL_MST GROUP BY {c}")
                        res = cur.fetchall()
                        # Only print if there are values indicating multiple statuses like 2, 3, 4
                        has_multiple = any(str(r[0]) in ['2', '3', '4'] for r in res)
                        if has_multiple:
                            print(f"Column {c} distribution:")
                            for r in res:
                                print(f"  {r[0]}: {r[1]}")
                    except:
                        pass

if __name__ == '__main__':
    explore_zatca_schema()
