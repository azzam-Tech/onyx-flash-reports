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

def check_salary_gl():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    print("=== 1. Checking Chart of Accounts for Salary / HR / Insurance Accounts ===")
    cur.execute("""
        SELECT A_CODE, A_NAME, A_LEVEL, A_REPORT
        FROM IAS20261.ACCOUNT
        WHERE A_NAME LIKE '%راتب%' OR A_NAME LIKE '%رواتب%' OR A_NAME LIKE '%تأمين%' OR A_NAME LIKE '%بدل%' OR A_NAME LIKE '%أجور%' OR A_NAME LIKE '%موظف%' OR A_NAME LIKE '%تأمينات%'
        ORDER BY A_CODE
    """)
    accs = cur.fetchall()
    print(f"Found {len(accs)} accounts matching HR/Salary/Insurance/Allowances:")
    for a in accs:
        print(f"  {a[0]} | {a[1]} | Level {a[2]}")

    print("\n=== 2. Checking Posting Transactions for these accounts ===")
    cur.execute("""
        SELECT p.A_CODE, a.A_NAME, COUNT(*) cnt, SUM(NVL(p.DR_AMT,0)) dr, SUM(NVL(p.CR_AMT,0)) cr
        FROM IAS20261.IAS_POST_DTL p
        JOIN IAS20261.ACCOUNT a ON a.A_CODE = p.A_CODE
        WHERE (a.A_NAME LIKE '%راتب%' OR a.A_NAME LIKE '%رواتب%' OR a.A_NAME LIKE '%تأمين%' OR a.A_NAME LIKE '%بدل%' OR a.A_NAME LIKE '%أجور%' OR a.A_NAME LIKE '%موظف%' OR a.A_NAME LIKE '%تأمينات%')
          AND NVL(p.DOC_POST, 0) = 1
        GROUP BY p.A_CODE, a.A_NAME
        ORDER BY dr DESC
    """)
    posts = cur.fetchall()
    print(f"Found {len(posts)} active posting accounts for salaries/allowances/insurance:")
    for p in posts:
        print(f"  Acc: {p[0]} | {p[1]} | Trans: {p[2]} | Dr: {p[3]:,.2f} | Cr: {p[4]:,.2f}")

    print("\n=== 3. Checking Vendors / Customers / Cost Centers mapped to employees or banks ===")
    cur.execute("""
        SELECT COUNT(*) FROM IAS20261.VENDOR WHERE V_A_NAME LIKE '%راتب%' OR V_A_NAME LIKE '%تأمين%' OR V_A_NAME LIKE '%بنك%' OR V_A_NAME LIKE '%موظف%'
    """)
    print("Vendors with HR/Bank keywords:", cur.fetchone()[0])

    cur.execute("""
        SELECT COUNT(*) FROM IAS20261.CUSTOMER WHERE C_A_NAME LIKE '%موظف%' OR C_A_NAME LIKE '%راتب%' OR C_A_NAME LIKE '%تأمين%'
    """)
    print("Customers with HR keywords:", cur.fetchone()[0])

    conn.close()

if __name__ == "__main__":
    check_salary_gl()
