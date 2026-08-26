import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT PROV_NO, PROV_A_NAME 
                FROM IAS_PROVINCES 
                WHERE PROV_NO BETWEEN 101 AND 114
                ORDER BY PROV_NO
            """)
            rows = cur.fetchall()
            with open('testing/prov_names.txt', 'w', encoding='utf-8') as f:
                for r in rows:
                    f.write(f"{r[0]}: {r[1]}\n")
            
except Exception as e:
    print(f"Error: {e}")
