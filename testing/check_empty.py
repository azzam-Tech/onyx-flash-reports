import os
import sys
sys.path.append(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        query = """
        WITH gl_base AS (
          SELECT 
              SUBSTR(A_CODE, 1, 5) as acc_code,
              SUM(CASE WHEN DOC_DATE >= TO_DATE('2026-01-01', 'YYYY-MM-DD') AND DOC_DATE < TO_DATE('2026-06-30', 'YYYY-MM-DD')+1 THEN NVL(DR_AMT,0) ELSE 0 END) as mv_dr,
              SUM(CASE WHEN DOC_DATE >= TO_DATE('2026-01-01', 'YYYY-MM-DD') AND DOC_DATE < TO_DATE('2026-06-30', 'YYYY-MM-DD')+1 THEN NVL(CR_AMT,0) ELSE 0 END) as mv_cr
          FROM IAS20261.IAS_POST_DTL
          WHERE ('' IS NULL OR REP_CODE = '' OR CC_CODE = '')
            AND NVL(DOC_POST,0)=1
            AND SUBSTR(A_CODE, 1, 5) IN ('41101', '32101')
          GROUP BY SUBSTR(A_CODE, 1, 5)
        )
        SELECT * FROM gl_base
        """
        cur.execute(query)
        print("Test with empty rep_code:")
        for row in cur.fetchall():
            print(row)
