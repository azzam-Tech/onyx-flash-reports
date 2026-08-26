import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            # Check how many provinces are outside 101-114
            cur.execute("""
                SELECT COUNT(*) FROM IAS_PROVINCES 
                WHERE PROV_NO < 101 OR PROV_NO > 114
            """)
            bad_provs = cur.fetchone()[0]
            
            # Check how many customers are outside 101-114
            cur.execute("""
                SELECT COUNT(*) FROM CUSTOMER 
                WHERE PROV_NO < 101 OR PROV_NO > 114
            """)
            bad_custs = cur.fetchone()[0]
            
            # Check how many cities are outside 101-114
            cur.execute("""
                SELECT COUNT(*) FROM CITIES 
                WHERE PROV_NO < 101 OR PROV_NO > 114
            """)
            bad_cities = cur.fetchone()[0]
            
            print("--- Database Check (IAS20261) ---")
            print(f"Provinces outside 101-114: {bad_provs}")
            print(f"Customers outside 101-114: {bad_custs}")
            print(f"Cities outside 101-114: {bad_cities}")
            
except Exception as e:
    print(f"Error: {e}")
