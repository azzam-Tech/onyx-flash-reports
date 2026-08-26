import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT COUNT(*) FROM IAS20261.IAS_SUB_GRP_DTL
            """)
            print(f"Total rows in IAS_SUB_GRP_DTL: {cur.fetchone()[0]}")
            
            cur.execute("""
                SELECT DISTINCT G_CODE FROM IAS20261.IAS_SUB_GRP_DTL
            """)
            g_codes = [r[0] for r in cur.fetchall()]
            print(f"G_CODEs in IAS_SUB_GRP_DTL: {g_codes}")
            
            # Maybe the G_CODE is '3' or ' 3' or '003'?
            if g_codes:
                cur.execute(f"""
                    SELECT G_CODE, MNG_CODE, SUBG_CODE, SUBG_A_NAME 
                    FROM IAS20261.IAS_SUB_GRP_DTL
                    FETCH FIRST 10 ROWS ONLY
                """)
                print("\nSample rows from IAS_SUB_GRP_DTL:")
                for r in cur.fetchall():
                    print(r)
                    
            # Check other tables with 'SUB' in name
            cur.execute("""
                SELECT TABLE_NAME FROM ALL_TAB_COLUMNS 
                WHERE OWNER = 'IAS20261' AND COLUMN_NAME = 'SUBG_CODE'
                AND TABLE_NAME LIKE 'IAS_%'
            """)
            tables = [r[0] for r in cur.fetchall()]
            print(f"\nTables with SUBG_CODE: {tables}")
            
except Exception as e:
    print(f"Error: {e}")
