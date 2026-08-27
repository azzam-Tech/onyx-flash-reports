import os
from dotenv import load_dotenv
import oracledb

load_dotenv(r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\db.env")

lib_dir = os.getenv("ORA_LIB_DIR", r"C:\oracle\instantclient\instantclient_23_0")
try:
    oracledb.init_oracle_client(lib_dir=lib_dir)
except Exception as e:
    pass

def get_conn():
    return oracledb.connect(
        user=os.getenv("DB_USER", "RPT_USER"),
        password=os.getenv("DB_PASS", "ULT2016"),
        dsn=os.getenv("ORA_DSN", "100.100.1.100:1521/ORCL")
    )

sql = """
    SELECT BILL_NO, BILL_AMT, VAT_AMT, CC_CODE, REP_CODE
    FROM IAS20261.IAS_BILL_MST
    WHERE BILL_NO = '26314401058'
"""

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute(sql)
        for row in cur.fetchall():
            print(row)
