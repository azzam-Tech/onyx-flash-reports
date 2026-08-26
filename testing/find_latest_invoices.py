import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def find_latest():
    with get_conn() as con:
        with con.cursor() as cur:
            # First, double check IAS_BILL_MST
            cur.execute("SELECT MAX(BILL_DATE) FROM IAS_BILL_MST")
            print(f"Max date in IAS_BILL_MST: {cur.fetchone()[0]}")
            
            # Find all tables with BILL_MST
            cur.execute("SELECT table_name FROM all_tables WHERE table_name LIKE '%BILL_MST%' AND table_name NOT LIKE '%V_%'")
            tables = [r[0] for r in cur.fetchall()]
            
            print("\nChecking latest dates in other invoice tables:")
            for t in tables:
                if t != 'IAS_BILL_MST':
                    try:
                        cur.execute(f"SELECT MAX(BILL_DATE) FROM {t}")
                        max_date = cur.fetchone()[0]
                        if max_date:
                            cur.execute(f"SELECT COUNT(*) FROM {t} WHERE BILL_DATE > TO_DATE('2026-08-11', 'YYYY-MM-DD')")
                            cnt = cur.fetchone()[0]
                            print(f"{t}: Max Date = {max_date}, Count after Aug 11 = {cnt}")
                    except Exception as e:
                        pass
            
            # Check SMAN tables specifically (Salesman)
            cur.execute("SELECT table_name FROM all_tables WHERE table_name LIKE '%SMAN%'")
            sman_tables = [r[0] for r in cur.fetchall()]
            for t in sman_tables:
                if t not in tables:
                    try:
                        # try to find a date column
                        cur.execute(f"SELECT column_name FROM all_tab_columns WHERE table_name = '{t}' AND data_type LIKE '%DATE%'")
                        date_cols = [c[0] for c in cur.fetchall()]
                        if date_cols:
                            cur.execute(f"SELECT MAX({date_cols[0]}) FROM {t}")
                            max_date = cur.fetchone()[0]
                            if max_date:
                                print(f"{t}: Max {date_cols[0]} = {max_date}")
                    except:
                        pass

if __name__ == '__main__':
    find_latest()
