import sys
import os
import re

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    sql_path = 'testing/migrate_refrigerators.sql'
    with open(sql_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extract all I_CODEs from the UPDATE statements
    # Pattern: WHERE I_CODE = '...'
    i_codes = set(re.findall(r"WHERE I_CODE = '(.*?)';", content))
    
    print(f"Found {len(i_codes)} unique item codes in the SQL script.")
    
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            i_codes_list = list(i_codes)
            
            binds = [f":{i+1}" for i in range(len(i_codes_list))]
            query = f"""
                SELECT I_CODE 
                FROM IAS20261.IAS_ITM_MST 
                WHERE I_CODE IN ({','.join(binds)})
            """
            cur.execute(query, i_codes_list)
            
            db_codes = set(r[0] for r in cur.fetchall())
            
            missing_codes = i_codes - db_codes
            
            print(f"Items found in database: {len(db_codes)}")
            
            if missing_codes:
                print(f"\nWARNING: {len(missing_codes)} items from the Excel/SQL were NOT found in the database!")
                for c in sorted(list(missing_codes)):
                    print(f"  - {c}")
            else:
                print("\nSUCCESS: All items from the script exist in the database!")
                
except Exception as e:
    print(f"Error: {e}")
