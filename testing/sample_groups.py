import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM IAS_GRP_ITM_LVL FETCH FIRST 10 ROWS ONLY")
            rows = cur.fetchall()
            print("IAS_GRP_ITM_LVL:")
            for r in rows:
                print("  ", r)
                
            cur.execute("SELECT * FROM IAS_MAINSUB_GRP_DTL FETCH FIRST 10 ROWS ONLY")
            rows2 = cur.fetchall()
            print("\nIAS_MAINSUB_GRP_DTL:")
            for r in rows2:
                print("  ", r)
                
except Exception as e:
    print(f"Error: {e}")
