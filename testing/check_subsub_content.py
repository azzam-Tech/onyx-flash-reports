import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT SUBG_CODE, SUBG_A_NAME 
                FROM IAS20261.IAS_SUB_GRP_DTL 
                ORDER BY SUBG_CODE
            """)
            rows = cur.fetchall()
            print("Contents of IAS_SUB_GRP_DTL:")
            for r in rows:
                print(r)
                
except Exception as e:
    print(f"Error: {e}")
