import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn
import json

def check_structure():
    with get_conn() as con:
        with con.cursor() as cur:
            # Query group data for fridges
            cur.execute("""
                SELECT m.I_CODE, m.I_NAME, m.G_CODE, m.DETAIL_NO, m.GROUP_NO
                FROM IAS_ITM_MST m
                WHERE m.I_NAME LIKE '%ثلاج%'
                AND ROWNUM <= 5
            """)
            
            print(json.dumps(cur.fetchall(), ensure_ascii=False))
            
            # Check how many distinct levels are actually used
            cur.execute("SELECT COUNT(DISTINCT G_CODE) FROM IAS_ITM_MST")
            g = cur.fetchone()[0]
            cur.execute("SELECT COUNT(DISTINCT GROUP_NO) FROM IAS_ITM_MST")
            gn = cur.fetchone()[0]
            cur.execute("SELECT COUNT(DISTINCT DETAIL_NO) FROM IAS_ITM_MST")
            dn = cur.fetchone()[0]
            
            print(f"Distinct G_CODE: {g}")
            print(f"Distinct GROUP_NO: {gn}")
            print(f"Distinct DETAIL_NO: {dn}")
            
            # Count items that have these fields populated
            cur.execute("SELECT COUNT(*) FROM IAS_ITM_MST WHERE G_CODE IS NOT NULL")
            gc = cur.fetchone()[0]
            cur.execute("SELECT COUNT(*) FROM IAS_ITM_MST WHERE GROUP_NO IS NOT NULL")
            gnc = cur.fetchone()[0]
            cur.execute("SELECT COUNT(*) FROM IAS_ITM_MST WHERE DETAIL_NO IS NOT NULL")
            dnc = cur.fetchone()[0]
            
            print(f"Items with G_CODE: {gc}")
            print(f"Items with GROUP_NO: {gnc}")
            print(f"Items with DETAIL_NO: {dnc}")

if __name__ == '__main__':
    check_structure()
