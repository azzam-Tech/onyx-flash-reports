import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            # Get one region WITH customers
            cur.execute("""
                SELECT r.R_CODE, r.R_A_NAME, c.CITY_A_NAME 
                FROM REGIONS r
                JOIN CITIES c ON r.CITY_NO = c.CITY_NO
                WHERE EXISTS (SELECT 1 FROM CUSTOMER cust WHERE cust.R_CODE = r.R_CODE AND cust.CITY_NO = r.CITY_NO)
                FETCH FIRST 1 ROWS ONLY
            """)
            linked = cur.fetchone()
            
            # Get one region WITHOUT customers/branches/etc
            cur.execute("""
                SELECT r.R_CODE, r.R_A_NAME, c.CITY_A_NAME 
                FROM REGIONS r
                JOIN CITIES c ON r.CITY_NO = c.CITY_NO
                WHERE NOT EXISTS (SELECT 1 FROM CUSTOMER cust WHERE cust.R_CODE = r.R_CODE AND cust.CITY_NO = r.CITY_NO)
                  AND NOT EXISTS (SELECT 1 FROM V_DETAILS v WHERE v.R_CODE = r.R_CODE AND v.CITY_NO = r.CITY_NO)
                  AND NOT EXISTS (SELECT 1 FROM WAREHOUSE_DETAILS w WHERE w.R_CODE = r.R_CODE AND w.CITY_NO = r.CITY_NO)
                  AND NOT EXISTS (SELECT 1 FROM S_BRN b WHERE b.R_CODE = r.R_CODE AND b.CITY_NO = r.CITY_NO)
                FETCH FIRST 1 ROWS ONLY
            """)
            unlinked = cur.fetchone()
            
            print(f"Linked Region: {linked}")
            print(f"Unlinked Region: {unlinked}")
            
except Exception as e:
    print(f"Error: {e}")
