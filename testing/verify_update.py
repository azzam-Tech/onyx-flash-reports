import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    test_items = ['ADSD50MWQ', 'ARRRE-69S', 'GVRF-65-1 GVC PRO', 'WBARE-90WL', 'KMF-185H', 'SWTM20AX']
    
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            binds = [f":{i+1}" for i in range(len(test_items))]
            query = f"""
                SELECT I_CODE, MNG_CODE, SUBG_CODE 
                FROM IAS20261.IAS_ITM_MST 
                WHERE I_CODE IN ({','.join(binds)})
            """
            cur.execute(query, test_items)
            
            print("--- Checking current groups in the Database ---")
            results = cur.fetchall()
            for r in results:
                print(f"Item: {r[0]} | MNG_CODE (فرعية): {r[1]} | SUBG_CODE (تحت فرعية): {r[2]}")
                
except Exception as e:
    print(f"Error: {e}")
