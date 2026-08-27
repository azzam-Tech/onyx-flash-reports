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

rep_code = '144'

sql_sreen_aging = """
    SELECT SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as total_debt
    FROM IAS20261.IAS_POST_DTL p
    WHERE p.C_CODE IS NOT NULL
      AND (TO_CHAR(p.REP_CODE) = :rep_code OR TO_CHAR(p.CC_CODE) = :rep_code)
      -- AND NVL(p.DOC_POST, 0) = 1 -- Uncomment to test posted only
"""

sql_sreen_aging_posted = """
    SELECT SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as total_debt
    FROM IAS20261.IAS_POST_DTL p
    WHERE p.C_CODE IS NOT NULL
      AND (TO_CHAR(p.REP_CODE) = :rep_code OR TO_CHAR(p.CC_CODE) = :rep_code)
      AND NVL(p.DOC_POST, 0) = 1
"""

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute(sql_sreen_aging, {'rep_code': rep_code})
        row = cur.fetchone()
        print("TOTAL DEBT (ALL):", row[0])
        
        cur.execute(sql_sreen_aging_posted, {'rep_code': rep_code})
        row = cur.fetchone()
        print("TOTAL DEBT (POSTED):", row[0])
