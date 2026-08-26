import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            # Check columns in IAS_MAINSUB_GRP_DTL
            cur.execute("""
                SELECT COLUMN_NAME 
                FROM ALL_TAB_COLUMNS 
                WHERE OWNER = 'IAS20261' AND TABLE_NAME = 'IAS_MAINSUB_GRP_DTL'
                ORDER BY COLUMN_ID
            """)
            cols = [r[0] for r in cur.fetchall()]
            print("Columns in IAS_MAINSUB_GRP_DTL:")
            print(cols)
            
            # Check primary key constraints for IAS_MAINSUB_GRP_DTL
            cur.execute("""
                SELECT cols.column_name
                FROM all_constraints cons, all_cons_columns cols
                WHERE cons.constraint_type = 'P'
                AND cons.constraint_name = cols.constraint_name
                AND cons.owner = cols.owner
                AND cons.table_name = 'IAS_MAINSUB_GRP_DTL'
                AND cons.owner = 'IAS20261'
                ORDER BY cols.position
            """)
            pks = [r[0] for r in cur.fetchall()]
            print("\nPrimary Key for IAS_MAINSUB_GRP_DTL:")
            print(pks)
            
            # Check foreign keys from IAS_ITM_MST
            print("\nChecking if IAS_ITM_MST has G_CODE/MNG_CODE as references...")
            
except Exception as e:
    print(f"Error: {e}")
