import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            # 1. Main Group
            cur.execute("""
                SELECT G_CODE, MNG_CODE, MNG_A_NAME 
                FROM IAS_MAINSUB_GRP_DTL 
                WHERE MNG_CODE = '03' OR MNG_CODE = '3' OR G_CODE = '03'
            """)
            print("Main Groups matching 03:")
            for r in cur.fetchall():
                print("  ", r)
                
            # 2. Sub Groups
            cur.execute("""
                SELECT G_CODE, MNG_CODE, SUBG_CODE, SUBG_A_NAME 
                FROM IAS_SUB_GRP_DTL 
                WHERE MNG_CODE = '03' OR MNG_CODE = '3'
            """)
            print("\nSub Groups matching 03:")
            for r in cur.fetchall():
                print("  ", r)
                
            # 3. Look at items under this group
            # To know how items link to these groups, let's select a few items.
            cur.execute("""
                SELECT I_CODE, I_NAME, GRP_CLASS_CODE, FOOD_GRP_NO, SUB_FOOD_GRP_NO
                FROM IAS_ITM_MST
                WHERE FOOD_GRP_NO = '03' OR FOOD_GRP_NO = '3'
                FETCH FIRST 5 ROWS ONLY
            """)
            print("\nItems under 03:")
            for r in cur.fetchall():
                print("  ", r)
                
except Exception as e:
    print(f"Error: {e}")
