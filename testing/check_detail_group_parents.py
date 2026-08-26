import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT COUNT(*) FROM IAS20261.IAS_DETAIL_GROUP 
                WHERE G_CODE IS NOT NULL OR MNG_CODE IS NOT NULL OR SUBG_CODE IS NOT NULL
            """)
            count = cur.fetchone()[0]
            print(f"Number of Detailed Groups linked to a parent group: {count}")
            
            cur.execute("""
                SELECT COUNT(*) FROM IAS20261.IAS_DETAIL_GROUP 
                WHERE G_CODE IS NULL AND MNG_CODE IS NULL AND SUBG_CODE IS NULL
            """)
            count_null = cur.fetchone()[0]
            print(f"Number of Detailed Groups NOT linked to a parent group (floating): {count_null}")
            
except Exception as e:
    print(f"Error: {e}")
