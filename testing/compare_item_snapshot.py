import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

def datetime_converter(o):
    import datetime
    if isinstance(o, datetime.datetime):
        return o.__str__()

try:
    item_code = 'SRRF-286NFS'
    
    with open('testing/snapshot_before.json', 'r', encoding='utf-8') as f:
        snapshot_before = json.load(f)
        
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT COLUMN_NAME 
                FROM ALL_TAB_COLUMNS 
                WHERE OWNER = 'IAS20261' AND TABLE_NAME = 'IAS_ITM_MST'
                ORDER BY COLUMN_ID
            """)
            cols = [r[0] for r in cur.fetchall()]
            
            cur.execute(f"SELECT * FROM IAS20261.IAS_ITM_MST WHERE I_CODE = '{item_code}'")
            row = cur.fetchone()
            
            if row:
                snapshot_after = dict(zip(cols, row))
                
                print(f"--- Changes detected for {item_code} ---")
                changes_found = False
                for col in cols:
                    val_before = snapshot_before.get(col)
                    val_after = snapshot_after.get(col)
                    
                    # Convert datetimes to string for comparison
                    if hasattr(val_after, 'isoformat'):
                        val_after = str(val_after)
                        
                    if str(val_before) != str(val_after):
                        changes_found = True
                        print(f"  {col}:")
                        print(f"    BEFORE: {val_before}")
                        print(f"    AFTER : {val_after}")
                        
                if not changes_found:
                    print("  No changes detected in IAS_ITM_MST!")
            else:
                print("Item not found!")
                
except Exception as e:
    print(f"Error: {e}")
