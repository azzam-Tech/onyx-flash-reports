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
    
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            # Get columns of IAS_ITM_MST
            cur.execute("""
                SELECT COLUMN_NAME 
                FROM ALL_TAB_COLUMNS 
                WHERE OWNER = 'IAS20261' AND TABLE_NAME = 'IAS_ITM_MST'
                ORDER BY COLUMN_ID
            """)
            cols = [r[0] for r in cur.fetchall()]
            
            # Fetch the item
            cur.execute(f"""
                SELECT * FROM IAS20261.IAS_ITM_MST WHERE I_CODE = '{item_code}'
            """)
            row = cur.fetchone()
            
            if row:
                item_data = dict(zip(cols, row))
                # Let's filter to only show columns that have data, or specifically group columns
                group_cols = [
                    'G_CODE', 'MNG_CODE', 'SUBG_CODE', 'GROUP_NO', 'ILEV_NO', 'DETAIL_NO', 
                    'FOOD_GRP_NO', 'SUB_FOOD_GRP_NO', 'GRP_CLASS_CODE', 'STATCL_CLSS'
                ]
                
                print(f"--- Snapshot of {item_code} BEFORE manual update ---")
                print("1. Group-related columns:")
                for c in group_cols:
                    if c in item_data:
                        print(f"  {c}: {item_data[c]}")
                
                print("\n2. All non-null columns (excluding common flags):")
                for k, v in item_data.items():
                    if v is not None and str(v).strip() != '' and str(v) not in ('0', '1', 'N', 'Y'):
                        print(f"  {k}: {v}")
                        
                with open('testing/snapshot_before.json', 'w', encoding='utf-8') as f:
                    json.dump(item_data, f, default=datetime_converter, indent=2, ensure_ascii=False)
                print("\nFull snapshot saved to testing/snapshot_before.json")
            else:
                print(f"Item {item_code} not found in IAS_ITM_MST!")
                
except Exception as e:
    print(f"Error: {e}")
