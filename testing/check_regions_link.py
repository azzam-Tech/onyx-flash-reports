import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT 
                    COUNT(*) as total_regions,
                    SUM(CASE WHEN CNTRY_NO IS NOT NULL THEN 1 ELSE 0 END) as with_country,
                    SUM(CASE WHEN PROV_NO IS NOT NULL THEN 1 ELSE 0 END) as with_prov,
                    SUM(CASE WHEN CITY_NO IS NOT NULL THEN 1 ELSE 0 END) as with_city
                FROM REGIONS
            """)
            row = cur.fetchone()
            print(f"Total Regions: {row[0]}")
            print(f"Linked to Country: {row[1]}")
            print(f"Linked to Province: {row[2]}")
            print(f"Linked to City: {row[3]}")
except Exception as e:
    print(f"Error: {e}")
