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

def print_salary_accs():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    cur.execute("""
        SELECT p.A_CODE, a.A_NAME, COUNT(*) cnt, SUM(NVL(p.DR_AMT,0)) dr, SUM(NVL(p.CR_AMT,0)) cr
        FROM IAS20261.IAS_POST_DTL p
        JOIN IAS20261.ACCOUNT a ON a.A_CODE = p.A_CODE
        WHERE (a.A_NAME LIKE '%راتب%' OR a.A_NAME LIKE '%رواتب%' OR a.A_NAME LIKE '%تأمين%' OR A_NAME LIKE '%بدل%' OR a.A_NAME LIKE '%أجور%' OR a.A_NAME LIKE '%موظف%' OR a.A_NAME LIKE '%تأمينات%' OR p.A_CODE LIKE '321%' OR p.A_CODE LIKE '11402%')
          AND NVL(p.DOC_POST, 0) = 1
        GROUP BY p.A_CODE, a.A_NAME
        ORDER BY dr DESC
    """)
    rows = cur.fetchall()
    print("=== Active Salary & HR GL Accounts ===")
    for r in rows:
        print(f"Code: {r[0]} | Name: {r[1]} | Trans: {r[2]} | Dr: {r[3]:,.2f} | Cr: {r[4]:,.2f}")

    conn.close()

if __name__ == "__main__":
    print_salary_accs()
