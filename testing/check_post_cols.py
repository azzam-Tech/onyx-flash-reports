import oracledb
import os

_lib = r"C:\oracle\instantclient\instantclient_23_0"
try:
    oracledb.init_oracle_client(lib_dir=_lib)
except Exception:
    pass

DB_USER     = os.environ.get("ORA_USER",     "RPT_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD", "ULT2016")
DB_DSN      = os.environ.get("ORA_DSN",      "100.100.1.100:1521/ORCL")

def check_post_dtl_cols():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    cur.execute("SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE OWNER='IAS20261' AND TABLE_NAME='IAS_POST_DTL'")
    cols = [r[0] for r in cur.fetchall()]
    print("IAS_POST_DTL columns:", cols)

    cur.execute("SELECT * FROM IAS20261.IAS_POST_DTL WHERE A_CODE LIKE '11402%' AND ROWNUM <= 1")
    row = cur.fetchone()
    desc = [d[0] for d in cur.description]
    for c, val in zip(desc, row):
        if val is not None:
            print(f"  {c}: {val}")

    conn.close()

if __name__ == "__main__":
    check_post_dtl_cols()
