import os
import sys
from dotenv import load_dotenv
import oracledb

sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer')
from database import get_conn

with get_conn() as conn:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT SUM(NVL(DR_AMT,0)) - SUM(NVL(CR_AMT,0)) as BALANCE
            FROM IAS_POST_DTL
            WHERE A_CODE = '111010101' AND AC_CODE_DTL = '144' AND NVL(DOC_POST,0) = 1
        """)
        bal = cur.fetchone()[0]
        print(f"Current Balance for 111010101 / 144: {bal}")
