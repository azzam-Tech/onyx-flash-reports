import os
import sys
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

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute("SELECT DOC_TYPE, DOC_NO, CR_AMT, DR_AMT, DOC_DATE, JV_TYPE, TO_CHAR(C_CODE) FROM IAS20261.IAS_POST_DTL WHERE (CR_AMT = 5596.06 OR DR_AMT = 5596.06 OR CR_AMT=-5596.06 OR DR_AMT=-5596.06) AND (TO_CHAR(REP_CODE) = '144' OR TO_CHAR(CC_CODE) = '144')")
        print("Transactions of 5596.06:")
        for row in cur.fetchall():
            print(row)
            
        cur.execute("SELECT TO_CHAR(C_CODE), SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)) FROM IAS20261.IAS_POST_DTL WHERE TO_CHAR(REP_CODE) = '144' OR TO_CHAR(CC_CODE) = '144' GROUP BY TO_CHAR(C_CODE) HAVING SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)) = 5596.06 OR SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)) = -5596.06")
        print("Customers with balance 5596.06:")
        for row in cur.fetchall():
            print(row)
