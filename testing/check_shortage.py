import os
import sys
import json
from dotenv import load_dotenv
import oracledb

sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer')
from database import get_conn

with get_conn() as conn:
    with conn.cursor() as cur:
        # Search for any transaction in August with "عجز" in the description
        cur.execute("""
            SELECT DOC_DATE, DR_AMT, CR_AMT, DOC_DESC 
            FROM IAS_POST_DTL
            WHERE A_CODE = '111010101' AND AC_CODE_DTL = '144'
              AND EXTRACT(MONTH FROM DOC_DATE) = 8
              AND DOC_DESC LIKE '%عجز%'
        """)
        rows = cur.fetchall()
        print("Transactions with 'عجز' in August:")
        for r in rows:
            print(r)
