import sys, os
from dotenv import load_dotenv
sys.path.append(os.path.abspath(r'zatca_printer'))
load_dotenv(os.path.abspath(r'zatca_printer\.env'))
from app.database import get_conn
conn = get_conn(readonly=True)
cur = conn.cursor()
cur.execute("SELECT TRIM(REP_CODE), INACTIVE FROM IAS20261.CUSTOMER WHERE C_CODE = '040101186'")
print(cur.fetchone())
cur.execute("SELECT C_CODE FROM IAS20261.CUSTOMER WHERE TRIM(REP_CODE) = '144' AND ROWNUM = 1")
print(cur.fetchone())
