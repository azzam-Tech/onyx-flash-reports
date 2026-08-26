import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_sman_sync():
    with get_conn() as con:
        with con.cursor() as cur:
            try:
                # Check column names
                cur.execute("SELECT column_name FROM all_tab_columns WHERE table_name = 'IAS_SMAN_DOC_SYNC_DTS'")
                cols = [c[0] for c in cur.fetchall()]
                print("Columns in IAS_SMAN_DOC_SYNC_DTS:", cols)
                
                # If there's a status column, group by it
                for col in cols:
                    if 'STS' in col or 'FLG' in col or 'STATUS' in col or 'SYNC' in col:
                        try:
                            cur.execute(f"SELECT {col}, COUNT(*) FROM IAS_SMAN_DOC_SYNC_DTS GROUP BY {col}")
                            print(f"\nGroup by {col}:")
                            for r in cur.fetchall():
                                print(r)
                        except:
                            pass
            except Exception as e:
                print(f"Error: {e}")

if __name__ == '__main__':
    check_sman_sync()
