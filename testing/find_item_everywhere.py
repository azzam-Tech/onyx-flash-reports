import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def find_item_everywhere():
    icode = 'DORWM-13.5'
    print(f"Searching for item '{icode}' across all database tables...\n")
    
    with get_conn() as con:
        with con.cursor() as cur:
            # Get all tables that have a column named I_CODE
            cur.execute("""
                SELECT table_name 
                FROM all_tab_columns 
                WHERE column_name = 'I_CODE' 
                  AND owner = SYS_CONTEXT('USERENV', 'CURRENT_SCHEMA')
            """)
            tables = [r[0] for r in cur.fetchall()]
            
            print(f"Found {len(tables)} tables with an 'I_CODE' column. Scanning them...\n")
            
            found_in = []
            for table in tables:
                try:
                    # Dynamically check count
                    query = f"SELECT COUNT(*) FROM {table} WHERE I_CODE = :1"
                    cur.execute(query, [icode])
                    count = cur.fetchone()[0]
                    if count > 0:
                        found_in.append((table, count))
                except Exception as e:
                    # Table might be a view or have restrictions
                    pass
            
            print("--- RESULTS ---")
            if found_in:
                print(f"The item '{icode}' has records in the following tables:")
                for tbl, cnt in found_in:
                    print(f" - {tbl}: {cnt} record(s)")
            else:
                print("Item not found anywhere!")

if __name__ == '__main__':
    find_item_everywhere()
