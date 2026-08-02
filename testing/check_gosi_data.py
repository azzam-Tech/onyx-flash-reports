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

def check_gosi():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    cur.execute("""
        SELECT COUNT(*),
               COUNT(SCL_SCRTY_NO),
               COUNT(INSRNCE_NO),
               COUNT(BNK_AC_CODE),
               COUNT(SLRY_PAY_WAY)
        FROM IAS20261.S_EMP
    """)
    row = cur.fetchone()
    print(f"Total Emps: {row[0]}")
    print(f"Emps with GOSI No (SCL_SCRTY_NO): {row[1]}")
    print(f"Emps with Insurance No (INSRNCE_NO): {row[2]}")
    print(f"Emps with Bank Acc Code (BNK_AC_CODE): {row[3]}")
    print(f"Emps with Salary Pay Way (SLRY_PAY_WAY): {row[4]}")

    cur.execute("""
        SELECT EMP_NO, EMP_L_NM, SCL_SCRTY_NO, INSRNCE_NO, EMP_INSRNCE_AMT, SLRY_PAY_WAY, BNK_AC_CODE
        FROM IAS20261.S_EMP
        WHERE SCL_SCRTY_NO IS NOT NULL OR INSRNCE_NO IS NOT NULL OR BNK_AC_CODE IS NOT NULL OR SLRY_PAY_WAY IS NOT NULL
        FETCH FIRST 10 ROWS ONLY
    """)
    rows = cur.fetchall()
    print(f"\nFound {len(rows)} employees with HR/GOSI data. Sample:")
    for r in rows:
        print(" ", r)

    conn.close()

if __name__ == "__main__":
    check_gosi()
