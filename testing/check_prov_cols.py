import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT COLUMN_NAME, DATA_TYPE, NULLABLE 
                FROM ALL_TAB_COLUMNS 
                WHERE TABLE_NAME = 'IAS_PROVINCES' AND OWNER = 'IAS20261'
            """)
            cols = cur.fetchall()
            for c in cols:
                print(c)
                
            cur.execute("""
                SELECT * FROM IAS_PROVINCES WHERE PROV_NO = 1010
            """)
            row = cur.fetchone()
            print("Row 1010:", row)
            
except Exception as e:
    print(f"Error: {e}")
