import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT COLUMN_NAME, COMMENTS 
                FROM ALL_COL_COMMENTS 
                WHERE OWNER = 'IAS20261' AND TABLE_NAME = 'CUSTOMER'
            """)
            
            output = []
            for row in cur.fetchall():
                c_name = row[0]
                c_comment = row[1] if row[1] else ""
                
                # We want to find "المنطقة" or similar
                if 'منطق' in c_comment or 'AREA' in c_name or 'ZONE' in c_name or 'REG' in c_name or 'DIST' in c_name or 'BLCK' in c_name:
                    output.append(f"{c_name}: {c_comment}")
                    
            print("--- Possible Region Columns in CUSTOMER ---")
            for item in output:
                print(item)
except Exception as e:
    print(f"Error: {e}")
