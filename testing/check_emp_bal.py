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
        cur.execute("SELECT R_A_CODE FROM IAS20261.SALES_MAN WHERE TO_CHAR(REPRS_CODE) = '144'")
        row = cur.fetchone()
        ac_code = row[0] if row else None
        print("R_A_CODE:", ac_code)
        
        if ac_code:
            cur.execute("""
                SELECT SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)) 
                FROM IAS20261.IAS_POST_DTL 
                WHERE TO_CHAR(AC_CODE) = :ac
            """, {'ac': str(ac_code)})
            res = cur.fetchone()
            print("Employee Balance (AC_CODE):", res[0] if res and res[0] is not None else 0)
