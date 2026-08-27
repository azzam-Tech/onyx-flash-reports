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
        cur.execute("SELECT TO_CHAR(C_GROUP_CODE), COUNT(*) FROM IAS20261.CUSTOMER WHERE TO_CHAR(REP_CODE) = '144' GROUP BY TO_CHAR(C_GROUP_CODE)")
        print("Groups for REP_CODE 144:")
        for row in cur.fetchall():
            print(row)
