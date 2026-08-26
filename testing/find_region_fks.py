import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            # Find the primary key constraint name for REGIONS
            cur.execute("""
                SELECT CONSTRAINT_NAME 
                FROM ALL_CONSTRAINTS 
                WHERE TABLE_NAME = 'REGIONS' AND CONSTRAINT_TYPE = 'P' AND OWNER = 'IAS20261'
            """)
            pk_const = cur.fetchone()
            if pk_const:
                pk_name = pk_const[0]
                # Find all foreign keys pointing to this PK
                cur.execute(f"""
                    SELECT TABLE_NAME, CONSTRAINT_NAME
                    FROM ALL_CONSTRAINTS
                    WHERE R_CONSTRAINT_NAME = '{pk_name}' AND OWNER = 'IAS20261'
                """)
                children = cur.fetchall()
                print("Tables referencing REGIONS:")
                for child in children:
                    print(f"  - {child[0]} (FK: {child[1]})")
            else:
                print("Could not find PK for REGIONS")
                
except Exception as e:
    print(f"Error: {e}")
