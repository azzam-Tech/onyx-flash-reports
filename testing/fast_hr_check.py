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

def fast_check():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    cur.execute("SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE OWNER='IAS20261' AND TABLE_NAME='S_EMP'")
    cols = [r[0] for r in cur.fetchall()]

    populated_cols = []
    for c in cols:
        try:
            cur.execute(f"SELECT COUNT({c}) FROM IAS20261.S_EMP")
            cnt = cur.fetchone()[0]
            if cnt > 0:
                populated_cols.append((c, cnt))
        except Exception:
            pass

    print(f"Populated Columns in IAS20261.S_EMP ({len(populated_cols)} / {len(cols)}):")
    for c, cnt in populated_cols:
        print(f"  {c}: {cnt} rows populated")

    conn.close()

if __name__ == "__main__":
    fast_check()
