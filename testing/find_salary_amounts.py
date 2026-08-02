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

def find_salaries():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    print("=== 1. Searching for all columns containing SLRY, SALARY, WAGE, PAY, BS_ in IAS20261 ===")
    cur.execute("""
        SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE
        FROM ALL_TAB_COLUMNS
        WHERE OWNER = 'IAS20261'
          AND (COLUMN_NAME LIKE '%SLRY%' OR COLUMN_NAME LIKE '%SALARY%' OR COLUMN_NAME LIKE '%WAGE%' OR COLUMN_NAME LIKE '%PAY%')
        ORDER BY TABLE_NAME, COLUMN_NAME
    """)
    cols = cur.fetchall()
    print(f"Found {len(cols)} salary/wage columns in IAS20261:")
    for tname, cname, dtype in cols:
        print(f"  {tname}.{cname} ({dtype})")

    print("\n=== 2. Checking non-null/non-zero data in those tables ===")
    seen_tables = set([c[0] for c in cols])
    for tname in seen_tables:
        t_cols = [c[1] for c in cols if c[0] == tname]
        select_cols = ", ".join(t_cols)
        try:
            cur.execute(f"SELECT COUNT(*) FROM IAS20261.{tname}")
            cnt = cur.fetchone()[0]
            if cnt > 0:
                print(f"Checking table IAS20261.{tname} ({cnt} rows)...")
                cur.execute(f"SELECT EMP_NO, {select_cols} FROM IAS20261.{tname} WHERE ROWNUM <= 5")
                for r in cur.fetchall():
                    print(f"   Row in {tname}: {r}")
        except Exception as ex:
            # Table might not have EMP_NO
            try:
                cur.execute(f"SELECT {select_cols} FROM IAS20261.{tname} WHERE ROWNUM <= 5")
                for r in cur.fetchall():
                    print(f"   Row in {tname} (no EMP_NO): {r}")
            except Exception as ex2:
                print(f"   Error reading {tname}: {ex2}")

    conn.close()

if __name__ == "__main__":
    find_salaries()
