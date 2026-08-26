import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT TABLE_NAME 
                FROM ALL_TABLES 
                WHERE OWNER = 'IAS20261' 
                  AND (TABLE_NAME LIKE '%ITM%GRP%' OR TABLE_NAME LIKE '%GRP%')
            """)
            tables = cur.fetchall()
            print("Group related tables:")
            for t in tables:
                print(t[0])
            
            # Let's check columns of IAS_ITM_MST to see the group fields
            cur.execute("""
                SELECT COLUMN_NAME, DATA_TYPE
                FROM ALL_TAB_COLUMNS 
                WHERE OWNER = 'IAS20261' AND TABLE_NAME = 'IAS_ITM_MST'
                  AND COLUMN_NAME LIKE '%GRP%'
            """)
            cols = cur.fetchall()
            print("\nGroup columns in IAS_ITM_MST:")
            for c in cols:
                print(c[0])
            
except Exception as e:
    print(f"Error: {e}")
