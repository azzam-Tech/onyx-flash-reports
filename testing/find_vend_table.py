import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT TABLE_NAME 
                FROM ALL_CONSTRAINTS 
                WHERE CONSTRAINT_NAME = 'VEND_CITYNO_FK' AND OWNER = 'IAS20261'
            """)
            row = cur.fetchone()
            if row:
                print(f"Child Table is: {row[0]}")
            else:
                print("Constraint not found.")
except Exception as e:
    print(f"Error: {e}")
