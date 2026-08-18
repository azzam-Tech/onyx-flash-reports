import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_populated():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT 
                    COUNT(G_CODE) as G_C,
                    COUNT(MNG_CODE) as M_C,
                    COUNT(SUBG_CODE) as S_C,
                    COUNT(ASSISTANT_NO) as A_C,
                    COUNT(DETAIL_NO) as D_C
                FROM IAS_ITM_MST
            """)
            print(cur.fetchone())

if __name__ == '__main__':
    check_populated()
