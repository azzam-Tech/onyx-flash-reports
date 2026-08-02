import os
import sys
sys.path.append(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        # What was recently unposted?
        cur.execute("""
            SELECT SUM(CR_AMT)
            FROM IAS20261.IAS_POST_DTL
            WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
              AND DOC_DATE >= TO_DATE('2026-01-01','YYYY-MM-DD') AND DOC_DATE < TO_DATE('2026-07-01','YYYY-MM-DD')
              AND UNPOST_DATE >= TO_DATE('2026-07-19', 'YYYY-MM-DD')
        """)
        val = cur.fetchone()[0]
        print(f"Total Unposted recently: {val}")
