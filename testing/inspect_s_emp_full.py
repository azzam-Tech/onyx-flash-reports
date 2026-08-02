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

def inspect_s_emp():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    cur.execute("""
        SELECT e.EMP_NO, TRIM(e.EMP_L_NM) emp_name,
               TO_CHAR(e.STRT_WRK_DATE, 'YYYY-MM-DD') start_date,
               CASE WHEN NVL(e.INACTIVE,0)=0 THEN 'نشط' ELSE 'موقوف' END st,
               e.SCL_SCRTY_NO, e.INSRNCE_NO, e.INSRNCE_OTHRS,
               e.SLRY_PAY_WAY, e.SLRY_CALC, e.CC_CODE, e.AC_CODE, e.EMPLYMNT_TYP, e.CTGRY_NO, e.NOTES
        FROM IAS20261.S_EMP e
        ORDER BY e.EMP_NO
    """)
    rows = cur.fetchall()
    print(f"Total S_EMP records: {len(rows)}")
    for r in rows:
        print(" ", r)

    conn.close()

if __name__ == "__main__":
    inspect_s_emp()
