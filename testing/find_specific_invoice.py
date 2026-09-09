import sys, os
from dotenv import load_dotenv
sys.path.append(os.path.abspath(r'zatca_printer'))
load_dotenv(os.path.abspath(r'zatca_printer\.env'))
from app.database import get_conn
conn = get_conn(readonly=True)
cur = conn.cursor()
cur.execute("""
    SELECT BILL_NO, BILL_SER, DOC_SER_EXTRNL, AD_DATE, BILL_AMT
    FROM IAS20261.IAS_BILL_MST 
    WHERE BILL_SER = '202600000110430' OR DOC_SER_EXTRNL = '202600000110430'
""")
for row in cur.fetchall():
    print(row)
