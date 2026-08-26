import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT I_CODE, I_NAME, G_CODE, MNG_CODE, SUBG_CODE, GROUP_NO 
                FROM IAS_ITM_MST 
                WHERE I_NAME LIKE '%ثلاج%' OR I_NAME LIKE '%ثلاجه%' OR I_NAME LIKE '%ثلاجة%'
                FETCH FIRST 5 ROWS ONLY
            """)
            items = cur.fetchall()
            print("Items matching 'ثلاج':")
            for r in items:
                print("  ", r)
                
            if items:
                # Find group names for the first item
                g_code = items[0][2]
                mng_code = items[0][3]
                subg_code = items[0][4]
                
                print(f"\nGroup IDs for item 1: G_CODE={g_code}, MNG_CODE={mng_code}, SUBG_CODE={subg_code}")
                
                if mng_code:
                    cur.execute(f"SELECT MNG_A_NAME FROM IAS_MAINSUB_GRP_DTL WHERE MNG_CODE = '{mng_code}'")
                    mng = cur.fetchone()
                    print("Main Group Name:", mng[0] if mng else 'Not found')
                    
                if subg_code:
                    cur.execute(f"SELECT SUBG_A_NAME FROM IAS_SUB_GRP_DTL WHERE SUBG_CODE = '{subg_code}'")
                    subg = cur.fetchone()
                    print("Sub Group Name:", subg[0] if subg else 'Not found')
                
except Exception as e:
    print(f"Error: {e}")
