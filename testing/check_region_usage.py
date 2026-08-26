import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            # Check how many regions have at least one customer
            cur.execute("""
                SELECT COUNT(DISTINCT r.R_CODE)
                FROM REGIONS r
                JOIN CUSTOMER c ON r.R_CODE = c.R_CODE AND r.CITY_NO = c.CITY_NO AND r.PROV_NO = c.PROV_NO
            """)
            regions_with_customers = cur.fetchone()[0]
            
            # Check total regions
            cur.execute("SELECT COUNT(*) FROM REGIONS")
            total_regions = cur.fetchone()[0]
            
            # Find how many regions are totally unused across key tables
            query_unused = """
                SELECT COUNT(*) FROM REGIONS r
                WHERE NOT EXISTS (SELECT 1 FROM CUSTOMER c WHERE c.R_CODE = r.R_CODE AND c.CITY_NO = r.CITY_NO)
                  AND NOT EXISTS (SELECT 1 FROM V_DETAILS v WHERE v.R_CODE = r.R_CODE AND v.CITY_NO = r.CITY_NO)
                  AND NOT EXISTS (SELECT 1 FROM WAREHOUSE_DETAILS w WHERE w.R_CODE = r.R_CODE AND w.CITY_NO = r.CITY_NO)
                  AND NOT EXISTS (SELECT 1 FROM S_BRN b WHERE b.R_CODE = r.R_CODE AND b.CITY_NO = r.CITY_NO)
            """
            cur.execute(query_unused)
            unused_regions = cur.fetchone()[0]
            
            print(f"Total Regions: {total_regions}")
            print(f"Regions with at least 1 customer: {regions_with_customers}")
            print(f"Completely empty regions (0 customers, 0 branches, 0 warehouses, 0 vendors): {unused_regions}")
            
except Exception as e:
    print(f"Error: {e}")
