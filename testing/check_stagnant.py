import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_stagnant_fridges():
    with get_conn() as con:
        with con.cursor() as cur:
            # Fridges with NO movement in 25 and 26
            cur.execute("""
                SELECT COUNT(I_CODE) 
                FROM IAS_ITM_MST 
                WHERE G_CODE = '003' 
                AND I_CODE NOT IN (
                    SELECT DISTINCT I_CODE 
                    FROM ITEM_MOVEMENT 
                    WHERE I_CODE IS NOT NULL 
                    AND (TO_CHAR(I_DATE, 'YYYY') = '2025' OR TO_CHAR(I_DATE, 'YYYY') = '2026')
                )
            """)
            no_mov_25_26 = cur.fetchone()[0]
            
            # Fridges that HAVE movement before 2025, but NO movement in 25 and 26
            cur.execute("""
                SELECT COUNT(I_CODE) 
                FROM IAS_ITM_MST 
                WHERE G_CODE = '003' 
                AND I_CODE IN (
                    SELECT DISTINCT I_CODE FROM ITEM_MOVEMENT WHERE I_CODE IS NOT NULL
                )
                AND I_CODE NOT IN (
                    SELECT DISTINCT I_CODE 
                    FROM ITEM_MOVEMENT 
                    WHERE I_CODE IS NOT NULL 
                    AND (TO_CHAR(I_DATE, 'YYYY') = '2025' OR TO_CHAR(I_DATE, 'YYYY') = '2026')
                )
            """)
            stagnant_but_used = cur.fetchone()[0]

            print(f"Total fridges with NO movement in 25/26: {no_mov_25_26}")
            print(f"Of which, {stagnant_but_used} fridges HAVE old movements (before 2025), and {no_mov_25_26 - stagnant_but_used} have NO movement EVER.")

if __name__ == '__main__':
    check_stagnant_fridges()
