import os
import sys

os.environ["NLS_LANG"] = ".AL32UTF8"
sys.stdout.reconfigure(encoding='utf-8')

import oracledb

_lib = r"C:\oracle\instantclient\instantclient_23_0"
try:
    oracledb.init_oracle_client(lib_dir=_lib)
except Exception:
    pass

DB_USER     = os.environ.get("ORA_USER",     "RPT_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD", "ULT2016")
DB_DSN      = os.environ.get("ORA_DSN",      "100.100.1.100:1521/ORCL")

def print_utf8():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    cur.execute("""
        SELECT A_CODE, A_NAME
        FROM IAS20261.ACCOUNT
        WHERE A_CODE IN ('114020001', '321010003', '321010004', '324010033', '324010042', '324010004', '324010043', '211040004', '321010001')
        ORDER BY A_CODE
    """)
    for code, name in cur.fetchall():
        print(f"Account Code {code}: {name}")

    conn.close()

if __name__ == "__main__":
    print_utf8()
