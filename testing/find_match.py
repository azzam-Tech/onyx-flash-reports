import os
import sys
sys.path.append(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        query = """
        SELECT SUM(NVL(CR_AMT,0))
        FROM IAS20261.IAS_POST_DTL
        WHERE SUBSTR(A_CODE, 1, 5) = '41101'
          AND DOC_DATE >= TO_DATE('2026-01-01', 'YYYY-MM-DD')
          AND DOC_DATE <= TO_DATE('2026-06-30', 'YYYY-MM-DD')
        """
        cur.execute(query)
        print(f"Total Revenue Movement: {cur.fetchone()[0]}")
        
        query2 = """
        SELECT SUM(NVL(CR_AMT,0))
        FROM IAS20261.IAS_POST_DTL
        WHERE SUBSTR(A_CODE, 1, 5) = '41101'
          AND DOC_DATE < TO_DATE('2026-01-01', 'YYYY-MM-DD')
        """
        cur.execute(query2)
        print(f"Total Revenue Opening: {cur.fetchone()[0]}")
