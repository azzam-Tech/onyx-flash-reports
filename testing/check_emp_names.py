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

def check_names():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    cur.execute("SELECT EMP_NO, EMP_L_NM, FRST_L_NM, SCND_L_NM, LST_L_NM, SCL_SCRTY_NO, INSRNCE_NO, SLRY_PAY_WAY FROM IAS20261.S_EMP WHERE ROWNUM <= 10")
    for r in cur.fetchall():
        print(r)

    conn.close()

if __name__ == "__main__":
    check_names()
