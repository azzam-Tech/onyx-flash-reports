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
        cur.execute("""
            SELECT SUM(NVL(p.DR_AMT, 0)) AS dr_sum, SUM(NVL(p.CR_AMT, 0)) as cr_sum
            FROM IAS20261.IAS_POST_DTL p
            WHERE (p.A_CODE LIKE '11402%' OR p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%')
              AND (TO_CHAR(p.AC_CODE_DTL) = '144' OR TO_CHAR(p.CC_CODE) = '144')
              AND NVL(p.DOC_POST, 0) = 1
        """)
        row = cur.fetchone()
        print("Salesman 144:", row)
        
        cur.execute("""
            SELECT a.A_NAME, SUM(NVL(p.DR_AMT, 0)) AS dr_sum, SUM(NVL(p.CR_AMT, 0)) as cr_sum
            FROM IAS20261.IAS_POST_DTL p
            JOIN IAS20261.ACCOUNT a ON a.A_CODE = p.A_CODE
            WHERE (p.A_CODE LIKE '11402%' OR p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%')
              AND (TO_CHAR(p.AC_CODE_DTL) = '144' OR TO_CHAR(p.CC_CODE) = '144')
              AND NVL(p.DOC_POST, 0) = 1
            GROUP BY a.A_NAME
        """)
        for r in cur.fetchall():
            print("  Acct:", r)
