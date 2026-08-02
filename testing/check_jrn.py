import os
import sys
sys.path.append(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute("""
            SELECT DOC_NO, TO_CHAR(DOC_DATE, 'YYYY-MM-DD'), TO_CHAR(AD_DATE, 'YYYY-MM-DD'), TO_CHAR(POST_DATE, 'YYYY-MM-DD'), CR_AMT
            FROM IAS20261.IAS_POST_DTL
            WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
              AND DOC_DATE >= TO_DATE('2026-01-01','YYYY-MM-DD') AND DOC_DATE < TO_DATE('2026-07-01','YYYY-MM-DD')
              AND (AD_DATE >= TO_DATE('2026-07-19', 'YYYY-MM-DD') OR POST_DATE >= TO_DATE('2026-07-19', 'YYYY-MM-DD'))
        """)
        for row in cur.fetchall():
            print(f"DOC_NO: {row[0]}, DOC_DATE: {row[1]}, AD_DATE: {row[2]}, POST_DATE: {row[3]}, AMT: {row[4]}")
