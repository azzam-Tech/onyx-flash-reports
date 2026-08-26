import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT COLUMN_NAME 
                FROM ALL_TAB_COLUMNS 
                WHERE OWNER = 'IAS20261' AND TABLE_NAME = 'REGIONS'
            """)
            cols = [row[0] for row in cur.fetchall()]
            
            with open('testing/regions_cols.json', 'w') as f:
                json.dump(cols, f, indent=4)
except Exception as e:
    print(f"Error: {e}")
