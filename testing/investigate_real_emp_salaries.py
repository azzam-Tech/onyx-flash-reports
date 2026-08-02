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

def investigate_all_emp_salaries():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    print("=== 1. Checking S_EMP table numeric salary columns for ALL 170 employees ===")
    cur.execute("""
        SELECT e.EMP_NO, TRIM(e.EMP_L_NM) emp_name,
               e.SCL_SCRTY_NO,
               NVL(e.HR_WAGE, 0) hr_wage,
               NVL(e.DY_WAGE, 0) dy_wage,
               NVL(e.EMP_INSRNCE_AMT, 0) ins_amt,
               NVL(e.INSRNCE_OTHRS, 0) ins_others,
               NVL(e.FEED_LMT_AMT, 0) feed_amt,
               NVL(e.WRK_HRS_DY, 8) hrs_day,
               NVL(e.WRK_DY_MNTH, 30) days_month
        FROM IAS20261.S_EMP e
        ORDER BY e.EMP_NO
    """)
    rows = cur.fetchall()
    print(f"Total S_EMP records: {len(rows)}")
    non_zero_salaries = []
    for r in rows:
        if r[3] > 0 or r[4] > 0 or r[5] > 0 or r[6] > 0 or r[7] > 0:
            non_zero_salaries.append(r)

    print(f"Employees with non-zero S_EMP wages/insurance ({len(non_zero_salaries)}):")
    for r in non_zero_salaries[:10]:
        print(" ", r)

    print("\n=== 2. Checking S_EMP_CODE_DTL / S_EMP_CODE_MST (Employee Allowances & Salary Items) ===")
    try:
        cur.execute("SELECT COUNT(*) FROM IAS20261.S_EMP_CODE_DTL")
        print("S_EMP_CODE_DTL count:", cur.fetchone()[0])
        cur.execute("""
            SELECT d.EMP_NO, TRIM(e.EMP_L_NM), d.CODE_NO, d.CODE_VAL
            FROM IAS20261.S_EMP_CODE_DTL d
            JOIN IAS20261.S_EMP e ON e.EMP_NO = d.EMP_NO
            WHERE ROWNUM <= 15
        """)
        for r in cur.fetchall():
            print("  S_EMP_CODE_DTL row:", r)
    except Exception as ex:
        print("S_EMP_CODE_DTL check error:", ex)

    print("\n=== 3. Checking HRS_EMP_MOVMNT or HRS_PRD_WRK_EMP (Payroll Transactions) ===")
    try:
        cur.execute("SELECT COUNT(*) FROM IAS20261.HRS_EMP_MOVMNT")
        print("HRS_EMP_MOVMNT count:", cur.fetchone()[0])
    except Exception as ex:
        print("HRS_EMP_MOVMNT error:", ex)

    try:
        cur.execute("SELECT COUNT(*) FROM IAS20261.HRS_PRD_WRK_EMP")
        print("HRS_PRD_WRK_EMP count:", cur.fetchone()[0])
    except Exception as ex:
        print("HRS_PRD_WRK_EMP error:", ex)

    print("\n=== 4. Checking IAS_POST_DTL for EMP_NO column ONLY ===")
    cur.execute("""
        SELECT p.EMP_NO, TRIM(e.EMP_L_NM), p.A_CODE, a.A_NAME, COUNT(*), SUM(NVL(p.DR_AMT,0)), SUM(NVL(p.CR_AMT,0))
        FROM IAS20261.IAS_POST_DTL p
        JOIN IAS20261.S_EMP e ON e.EMP_NO = p.EMP_NO
        JOIN IAS20261.ACCOUNT a ON a.A_CODE = p.A_CODE
        WHERE NVL(p.DOC_POST,0) = 1
        GROUP BY p.EMP_NO, e.EMP_L_NM, p.A_CODE, a.A_NAME
        ORDER BY SUM(NVL(p.DR_AMT,0)) DESC
    """)
    emp_posts = cur.fetchall()
    print(f"IAS_POST_DTL with exact p.EMP_NO ({len(emp_posts)} records):")
    for p in emp_posts[:15]:
        print(" ", p)

    conn.close()

if __name__ == "__main__":
    investigate_all_emp_salaries()
