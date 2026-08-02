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

def check_cols():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    cur.execute("SELECT * FROM IAS20261.S_EMP WHERE ROWNUM <= 1")
    cols = [d[0] for d in cur.description]
    row = cur.fetchone()
    print("\nFirst 20 fields and values:")
    for c, val in list(zip(cols, row))[:20]:
        print(f"  {c}: {val}")

    conn.close()

if __name__ == "__main__":
    check_cols()
