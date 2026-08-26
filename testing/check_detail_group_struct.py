import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT COLUMN_NAME 
                FROM ALL_TAB_COLUMNS 
                WHERE OWNER = 'IAS20261' AND TABLE_NAME = 'IAS_DETAIL_GROUP'
            """)
            cols = [r[0] for r in cur.fetchall()]
            print("Columns in IAS_DETAIL_GROUP:")
            print(", ".join(cols))
            
            cur.execute("SELECT * FROM IAS20261.IAS_DETAIL_GROUP FETCH FIRST 3 ROWS ONLY")
            print("\nSample rows:")
            for r in cur.fetchall():
                print(r)
                
except Exception as e:
    print(f"Error: {e}")
