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
              SUM(CASE WHEN DOC_DATE < TO_DATE('2026-01-01', 'YYYY-MM-DD') THEN NVL(DR_AMT,0) ELSE 0 END) as op_dr,
              SUM(CASE WHEN DOC_DATE < TO_DATE('2026-01-01', 'YYYY-MM-DD') THEN NVL(CR_AMT,0) ELSE 0 END) as op_cr,
              SUM(CASE WHEN DOC_DATE >= TO_DATE('2026-01-01', 'YYYY-MM-DD') AND DOC_DATE < TO_DATE('2026-06-30', 'YYYY-MM-DD')+1 THEN NVL(DR_AMT,0) ELSE 0 END) as mv_dr,
              SUM(CASE WHEN DOC_DATE >= TO_DATE('2026-01-01', 'YYYY-MM-DD') AND DOC_DATE < TO_DATE('2026-06-30', 'YYYY-MM-DD')+1 THEN NVL(CR_AMT,0) ELSE 0 END) as mv_cr
          FROM IAS20261.IAS_POST_DTL
          WHERE ('144' IS NULL OR REP_CODE = '144' OR CC_CODE = '144')
            AND NVL(DOC_POST,0)=1
            AND SUBSTR(A_CODE, 1, 5) IN (
                '31102','31104','31105','31109','31110',
                '32101','32201','32401','32801',
                '41101','41202'
            )
          GROUP BY SUBSTR(A_CODE, 1, 5)
        )
        SELECT * FROM gl_base
        ORDER BY acc_code
        """
        cur.execute(query)
        print("acc_code, op_dr, op_cr, mv_dr, mv_cr")
        for row in cur.fetchall():
            print(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}")
