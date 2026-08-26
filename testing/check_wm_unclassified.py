import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_wm_unclassified_movement():
    with get_conn() as con:
        with con.cursor() as cur:
            query = """
                SELECT 
                    m.I_CODE, 
                    MAX(t.I_NAME) as I_NAME, 
                    MAX(m.I_DATE) as last_mov,
                    MAX(t.MNG_CODE) as mng_code,
                    MAX(t.SUBG_CODE) as subg_code
                FROM ITEM_MOVEMENT m
                JOIN IAS_ITM_MST t ON m.I_CODE = t.I_CODE
                WHERE t.G_CODE = '005' 
                  AND (t.MNG_CODE IS NULL OR t.SUBG_CODE IS NULL)
                GROUP BY m.I_CODE
                ORDER BY last_mov DESC
            """
            cur.execute(query)
            unclassified_with_movement = cur.fetchall()
            
            print(f"Total washing machines WITH movement but WITHOUT proper sub-groups: {len(unclassified_with_movement)}")
            
            if unclassified_with_movement:
                print("--- Examples ---")
                for i, r in enumerate(unclassified_with_movement[:20]):
                    code = r[0]
                    name = r[1]
                    last_mov = r[2].strftime('%Y-%m-%d') if r[2] else 'Unknown'
                    print(f"{i+1}. {code} : {name}  | آخر حركة: {last_mov}")

if __name__ == '__main__':
    check_wm_unclassified_movement()
