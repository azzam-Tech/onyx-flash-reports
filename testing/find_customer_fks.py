import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT CONSTRAINT_NAME 
                FROM ALL_CONSTRAINTS 
                WHERE TABLE_NAME = 'CUSTOMER' AND CONSTRAINT_TYPE = 'P' AND OWNER = 'IAS20261'
            """)
            pk = cur.fetchone()
            if pk:
                pk_name = pk[0]
                cur.execute(f"""
                    SELECT a.TABLE_NAME, a.COLUMN_NAME
                    FROM ALL_CONS_COLUMNS a
                    JOIN ALL_CONSTRAINTS c ON a.CONSTRAINT_NAME = c.CONSTRAINT_NAME AND a.OWNER = c.OWNER
                    WHERE c.R_CONSTRAINT_NAME = '{pk_name}' 
                      AND c.OWNER = 'IAS20261'
                """)
                fks = cur.fetchall()
                print(f"Tables referencing CUSTOMER (Total {len(fks)}):")
                for fk in fks[:30]:
                    print(f"  - {fk[0]}.{fk[1]}")
                if len(fks) > 30:
                    print("  ... and more")
            else:
                print("No PK found for CUSTOMER")
                
except Exception as e:
    print(f"Error: {e}")
