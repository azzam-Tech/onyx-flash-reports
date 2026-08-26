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
                WHERE OWNER = 'IAS20261' AND TABLE_NAME = 'IAS_ITM_MST'
                ORDER BY COLUMN_ID
            """)
            cols = [c[0] for c in cur.fetchall()]
            with open('testing/item_columns.txt', 'w') as f:
                f.write("\n".join(cols))
            print("Columns dumped to testing/item_columns.txt")
except Exception as e:
    print(f"Error: {e}")
