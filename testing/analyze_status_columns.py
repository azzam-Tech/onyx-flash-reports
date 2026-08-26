import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def analyze_columns():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT column_name 
                FROM all_tab_columns 
                WHERE table_name = 'IAS_BILL_MST' 
                ORDER BY column_id
            """)
            cols = [c[0] for c in cur.fetchall()]
            
            cur.execute("SELECT * FROM IAS_BILL_MST WHERE BILL_NO = '26314600409'")
            row = cur.fetchone()
            
            if row:
                print("--- Interesting columns for 26314600409 ---")
                for c, v in zip(cols, row):
                    if v is not None and str(v).strip() and str(v) != '0':
                        # Print only interesting column names that might hold status
                        if 'STS' in c or 'FLG' in c or 'STAT' in c or 'ZATCA' in c or 'SYNC' in c or 'INV' in c:
                            print(f"{c}: {v}")
            
            # Also, get the counts of invoices by DOC_TYPE and any potential status column for month 7 and 8
            # In Onyx, E_INV_SYNC_STS or similar might exist.
            potential_status_cols = [c for c in cols if 'STS' in c or 'FLG' in c]
            print(f"\nPotential status cols in IAS_BILL_MST: {potential_status_cols}")

if __name__ == '__main__':
    analyze_columns()
