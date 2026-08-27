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
    SELECT DOC_TYPE, DOC_NO, CR_AMT, DR_AMT, DOC_DATE, JV_TYPE
    FROM IAS20261.IAS_POST_DTL
    WHERE (CR_AMT = 1322.50 OR DR_AMT = 1322.50 OR CR_AMT=-1322.50 OR DR_AMT=-1322.50)
      AND TO_CHAR(CC_CODE) = '144'
"""

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute(sql)
        for row in cur.fetchall():
            print(row)
