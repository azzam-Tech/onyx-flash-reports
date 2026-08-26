import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            tables_to_check = ['CNTRY', 'IAS_PROVINCES', 'S_ZONE', 'CITY', 'CITIES']
            
            output = {}
            for t in tables_to_check:
                cur.execute(f"SELECT TABLE_NAME FROM ALL_TABLES WHERE OWNER = 'IAS20261' AND TABLE_NAME = '{t}'")
                if cur.fetchone():
                    cur.execute(f"SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE OWNER = 'IAS20261' AND TABLE_NAME = '{t}'")
                    output[t] = [row[0] for row in cur.fetchall()]
                    
            # Check CUSTOMER columns
            cur.execute("""
                SELECT COLUMN_NAME 
                FROM ALL_TAB_COLUMNS 
                WHERE OWNER = 'IAS20261' AND TABLE_NAME = 'CUSTOMER'
            """)
            cust_cols = [row[0] for row in cur.fetchall()]
            geo_cols = [c for c in cust_cols if any(x in c for x in ['CITY', 'CNTRY', 'PROV', 'ZONE', 'REG', 'GOV', 'AREA'])]
            output['CUSTOMER_GEO_COLS'] = geo_cols
            
            with open('testing/geo_schema.json', 'w', encoding='utf-8') as f:
                json.dump(output, f, indent=4, ensure_ascii=False)
            print("Successfully dumped schema to testing/geo_schema.json")
except Exception as e:
    print(f"Error: {e}")
