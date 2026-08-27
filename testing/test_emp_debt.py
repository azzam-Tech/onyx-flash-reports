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

sql_emp = """
    SELECT SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)) as emp_debt
    FROM IAS20261.IAS_POST_DTL
    WHERE E_CODE IS NOT NULL
      AND TO_CHAR(E_CODE) = :rep_code
"""

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute(sql_emp, {'rep_code': rep_code})
        row = cur.fetchone()
        print("EMP DEBT (E_CODE):", row[0])
