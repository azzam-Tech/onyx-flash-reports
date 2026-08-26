import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            tables = [
                'IAS_MAINSUB_GRP_DTL',
                'IAS_SUB_GRP_DTL'
            ]
            for t in tables:
                cur.execute(f"""
                    SELECT COLUMN_NAME 
                    FROM ALL_TAB_COLUMNS 
                    WHERE OWNER = 'IAS20261' AND TABLE_NAME = '{t}'
                """)
                cols = [c[0] for c in cur.fetchall()]
                print(f"Columns in {t}:")
                for c in cols:
                    print("  ", c)
                
            # Also, check if there is a Main Group table
            cur.execute("""
                SELECT TABLE_NAME FROM ALL_TABLES WHERE OWNER = 'IAS20261' AND TABLE_NAME LIKE 'IAS%GRP%'
            """)
            print("\nAll IAS group tables:")
            for r in cur.fetchall():
                print(r[0])
                
except Exception as e:
    print(f"Error: {e}")
