import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            
            # 1. Delete REGIONS
            sql_regions = """
                DELETE FROM REGIONS r
                WHERE (r.PROV_NO < 101 OR r.PROV_NO > 113 OR r.PROV_NO IS NULL)
                  AND NOT EXISTS (SELECT 1 FROM CUSTOMER c WHERE c.R_CODE = r.R_CODE)
            """
            cur.execute(sql_regions)
            regions_deleted = cur.rowcount
            print(f"Deleted Regions: {regions_deleted}")
            
            # 2. Delete CITIES
            sql_cities = """
                DELETE FROM CITIES c
                WHERE (c.PROV_NO < 101 OR c.PROV_NO > 113 OR c.PROV_NO IS NULL)
                  AND NOT EXISTS (SELECT 1 FROM CUSTOMER cust WHERE cust.CITY_NO = c.CITY_NO)
            """
            cur.execute(sql_cities)
            cities_deleted = cur.rowcount
            print(f"Deleted Cities: {cities_deleted}")
            
            # 3. Delete IAS_PROVINCES
            sql_provinces = """
                DELETE FROM IAS_PROVINCES p
                WHERE (p.PROV_NO < 101 OR p.PROV_NO > 113 OR p.PROV_NO IS NULL)
                  AND NOT EXISTS (SELECT 1 FROM CUSTOMER c WHERE c.PROV_NO = p.PROV_NO)
            """
            cur.execute(sql_provinces)
            provs_deleted = cur.rowcount
            print(f"Deleted Provinces: {provs_deleted}")
            
            conn.commit()
            print("Changes committed to the database.")
            
except Exception as e:
    print(f"Error: {e}")
