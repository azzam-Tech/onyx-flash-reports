import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            # 1. Get all columns of IAS_ITM_MST
            cur.execute("""
                SELECT COLUMN_NAME
                FROM ALL_TAB_COLUMNS 
                WHERE OWNER = 'IAS20261' AND TABLE_NAME = 'IAS_ITM_MST'
            """)
            cols = [c[0] for c in cur.fetchall()]
            
            # Print columns that might be group IDs (GRP, G1, G2, LVL, MAIN, SUB, CLASS, CAT)
            grp_cols = [c for c in cols if any(x in c for x in ['GRP', 'LVL', 'MAIN', 'SUB', 'CLASS', 'CAT'])]
            print("Potential Group columns in IAS_ITM_MST:")
            for c in grp_cols:
                print(c)
                
            # 2. Check IAS_GRP_ITM_LVL_TREE columns
            cur.execute("""
                SELECT COLUMN_NAME
                FROM ALL_TAB_COLUMNS 
                WHERE OWNER = 'IAS20261' AND TABLE_NAME = 'IAS_GRP_ITM_LVL_TREE'
            """)
            print("\nColumns in IAS_GRP_ITM_LVL_TREE:")
            for c in cur.fetchall():
                print(c[0])
                
            # 3. Sample from IAS_GRP_ITM_LVL_TREE
            cur.execute("""
                SELECT * FROM IAS_GRP_ITM_LVL_TREE FETCH FIRST 3 ROWS ONLY
            """)
            print("\nSample IAS_GRP_ITM_LVL_TREE:")
            for r in cur.fetchall():
                print(r)
                
except Exception as e:
    print(f"Error: {e}")
