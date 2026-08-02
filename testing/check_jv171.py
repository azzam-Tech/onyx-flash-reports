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

def check_jv171():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM IAS20261.IAS_POST_DTL WHERE DOC_NO = 171 AND DOC_TYPE = 1 AND ROWNUM <= 5
    """)
    rows = cur.fetchall()
    desc = [d[0] for d in cur.description]
    print("=== Journal Voucher 171 Rows ===")
    for row in rows:
        print("--- ROW ---")
        for col, val in zip(desc, row):
            if val is not None and str(val) != '0' and str(val) != '':
                print(f"  {col}: {val}")

    conn.close()

if __name__ == "__main__":
    check_jv171()
