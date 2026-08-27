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
            SELECT DOC_DATE, SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0))
            FROM IAS20261.IAS_POST_DTL
            WHERE (TO_CHAR(REP_CODE) = '144' OR TO_CHAR(CC_CODE) = '144')
            AND DOC_DATE >= TO_DATE('2026-08-20', 'YYYY-MM-DD')
            GROUP BY DOC_DATE
            ORDER BY DOC_DATE
        """)
        print("Daily Net Balances since Aug 20:")
        for row in cur.fetchall():
            print(row)
