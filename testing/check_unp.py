import sys
from dotenv import load_dotenv
import oracledb

sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer')
from database import get_conn

with get_conn() as conn:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT DOC_TYPE, SUM(DR_AMT), SUM(CR_AMT)
            FROM IAS_POST_DTL
            WHERE AC_CODE_DTL = '144' AND DOC_POST = 0
            GROUP BY DOC_TYPE
        """)
        rows = cur.fetchall()
        for r in rows:
            print(r)
