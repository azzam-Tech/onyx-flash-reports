import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            # Get PK of CITIES
            cur.execute("""
                SELECT CONSTRAINT_NAME FROM ALL_CONSTRAINTS
                WHERE TABLE_NAME = 'CITIES' AND CONSTRAINT_TYPE = 'P' AND OWNER = 'IAS20261'
            """)
            city_pk = cur.fetchone()[0]
            
            # Get PK of IAS_PROVINCES
            cur.execute("""
                SELECT CONSTRAINT_NAME FROM ALL_CONSTRAINTS
                WHERE TABLE_NAME = 'IAS_PROVINCES' AND CONSTRAINT_TYPE = 'P' AND OWNER = 'IAS20261'
            """)
            prov_pk = cur.fetchone()[0]
            
            # Find all child tables of CITIES
            cur.execute(f"""
                SELECT TABLE_NAME, CONSTRAINT_NAME FROM ALL_CONSTRAINTS
                WHERE R_CONSTRAINT_NAME = '{city_pk}' AND OWNER = 'IAS20261'
            """)
            city_children = [r[0] for r in cur.fetchall()]
            
            # Find all child tables of PROVINCES
            cur.execute(f"""
                SELECT TABLE_NAME, CONSTRAINT_NAME FROM ALL_CONSTRAINTS
                WHERE R_CONSTRAINT_NAME = '{prov_pk}' AND OWNER = 'IAS20261'
            """)
            prov_children = [r[0] for r in cur.fetchall()]
            
            print(f"CITIES referenced by: {city_children}")
            print(f"IAS_PROVINCES referenced by: {prov_children}")
            
except Exception as e:
    print(f"Error: {e}")
