import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT I_CODE, I_NAME, GRP_CLASS_CODE, FOOD_GRP_NO, SUB_FOOD_GRP_NO 
                FROM IAS_ITM_MST 
                WHERE I_NAME LIKE '%ثلاج%' OR I_NAME LIKE '%ثلاجه%' OR I_NAME LIKE '%ثلاجة%'
                FETCH FIRST 5 ROWS ONLY
            """)
            print("Items matching 'ثلاج':")
            items = cur.fetchall()
            for r in items:
                print("  ", r)
                
            if items:
                # Get the group codes from the first matched item
                grp_class = items[0][2]
                food_grp = items[0][3]
                print(f"\nLooking for group names for GRP_CLASS_CODE={grp_class} or FOOD_GRP_NO={food_grp}")
                
                # Check IAS_MAINSUB_GRP_DTL
                cur.execute(f"""
                    SELECT MNG_CODE, MNG_A_NAME FROM IAS_MAINSUB_GRP_DTL WHERE MNG_CODE = '{food_grp}' OR G_CODE = '{grp_class}'
                """)
                for r in cur.fetchall():
                    print("  Found in IAS_MAINSUB_GRP_DTL:", r)
                    
except Exception as e:
    print(f"Error: {e}")
