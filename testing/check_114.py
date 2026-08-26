import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT COUNT(*) FROM IAS_PROVINCES WHERE PROV_NO = 114
            """)
            count = cur.fetchone()[0]
            print(f"Province 114 count: {count}")
            
except Exception as e:
    print(f"Error: {e}")
