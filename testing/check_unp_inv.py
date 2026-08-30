import sys
from dotenv import load_dotenv
import oracledb

sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer')
from database import get_conn

with get_conn() as conn:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT DOC_NO, DR_AMT, CR_AMT
            FROM IAS_POST_DTL
            WHERE AC_CODE_DTL = '144' AND DOC_POST = 0 AND DOC_TYPE = 4
        """)
        rows = cur.fetchall()
        for r in rows:
            print(r)
