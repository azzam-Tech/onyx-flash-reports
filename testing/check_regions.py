import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT COUNT(*) FROM CITIES
            """)
            print(f"Total Cities remaining: {cur.fetchone()[0]}")
            
            # Check for duplicate regions under the same city
            query = """
                SELECT CITY_NO, R_A_NAME, COUNT(*) 
                FROM REGIONS 
                GROUP BY CITY_NO, R_A_NAME 
                HAVING COUNT(*) > 1
            """
            cur.execute(query)
            dups = cur.fetchall()
            print(f"\nDuplicate Regions found: {len(dups)}")
            for d in dups[:10]:
                print(f"City {d[0]} has {d[2]} regions named '{d[1]}'")
            
except Exception as e:
    print(f"Error: {e}")
