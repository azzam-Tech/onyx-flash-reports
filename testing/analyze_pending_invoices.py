import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def analyze_pending():
    with get_conn() as con:
        with con.cursor() as cur:
            try:
                cur.execute("SELECT table_name FROM all_tables WHERE table_name LIKE '%SYNC%' OR table_name LIKE '%E_INV%'")
                tables = cur.fetchall()
                for t in tables:
                    tname = t[0]
                    try:
                        cur.execute(f"SELECT COUNT(*) FROM {tname}")
                        cnt = cur.fetchone()[0]
                        if cnt > 0:
                            print(f"\n- {tname}: {cnt} rows")
                            cur.execute(f"SELECT column_name FROM all_tab_columns WHERE table_name = '{tname}'")
                            cols = [c[0] for c in cur.fetchall()]
                            
                            for col in cols:
                                if 'FLG' in col or 'STS' in col or 'STAT' in col or 'TYP' in col:
                                    try:
                                        cur.execute(f"SELECT {col}, COUNT(*) FROM {tname} GROUP BY {col}")
                                        res = cur.fetchall()
                                        print(f"   GroupBy {col}: {res}")
                                    except:
                                        pass
                    except:
                        pass
            except Exception as e:
                print(e)
                
if __name__ == '__main__':
    analyze_pending()
