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

def check_emp_code():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    print("=== S_EMP_CODE_DTL columns ===")
    cur.execute("SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE OWNER='IAS20261' AND TABLE_NAME='S_EMP_CODE_DTL'")
    cols = [r[0] for r in cur.fetchall()]
    print(cols)

    print("\n=== S_EMP_CODE_DTL rows ===")
    cur.execute("SELECT * FROM IAS20261.S_EMP_CODE_DTL WHERE ROWNUM <= 10")
    for r in cur.fetchall():
        print("  ", r)

    print("\n=== S_EMP_CODE_MST columns & rows ===")
    cur.execute("SELECT * FROM IAS20261.S_EMP_CODE_MST WHERE ROWNUM <= 10")
    for r in cur.fetchall():
        print("  MST:", r)

    conn.close()

if __name__ == "__main__":
    check_emp_code()
