import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT C_CODE, C_A_NAME, PROV_NO, CITY_NO, R_CODE FROM CUSTOMER 
                WHERE PROV_NO < 101 OR PROV_NO > 114 OR PROV_NO IS NULL
            """)
            rows = cur.fetchall()
            for r in rows:
                print(r)
            
except Exception as e:
    print(f"Error: {e}")
