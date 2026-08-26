import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT DETAIL_NO, DETAIL_A_NAME 
                FROM IAS20261.IAS_DETAIL_GROUP
            """)
            with open('testing/detail_groups.txt', 'w', encoding='utf-8') as f:
                for r in cur.fetchall():
                    f.write(f"ID: {r[0]}, Name: {r[1]}\n")
                
except Exception as e:
    print(f"Error: {e}")
