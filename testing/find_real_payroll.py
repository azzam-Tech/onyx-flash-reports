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

def find_real_payroll():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    print("=== 1. Searching for populated IBAN / Bank columns in any table ===")
    cur.execute("""
        SELECT OWNER, TABLE_NAME, COLUMN_NAME 
        FROM ALL_TAB_COLUMNS 
        WHERE (COLUMN_NAME LIKE '%IBAN%' OR COLUMN_NAME LIKE '%GOSI%' OR COLUMN_NAME LIKE '%SALARY%' OR COLUMN_NAME LIKE '%ALLOW%' OR COLUMN_NAME LIKE '%DED%')
        ORDER BY OWNER, TABLE_NAME
    """)
    cols = cur.fetchall()
    print(f"Found {len(cols)} candidate columns across all tables.")

    populated_cols = []
    for owner, tname, cname in cols:
        try:
            cur.execute(f"SELECT COUNT({cname}) FROM {owner}.{tname}")
            cnt = cur.fetchone()[0]
            if cnt > 0:
                populated_cols.append((owner, tname, cname, cnt))
        except Exception:
            pass

    print(f"\n--- Populated Payroll / GOSI / IBAN Columns ({len(populated_cols)}) ---")
    for owner, tname, cname, cnt in populated_cols:
        print(f"  {owner}.{tname}.{cname} -> {cnt} populated rows")

    print("\n=== 2. Searching for Payroll Vouchers / GL Postings for Salaries (A_CODE like 31% or 41% or 2% or 5%) ===")
    cur.execute("""
        SELECT p.A_CODE, a.A_NAME, COUNT(*), SUM(NVL(p.DR_AMT,0)) dr, SUM(NVL(p.CR_AMT,0)) cr
        FROM IAS20261.IAS_POST_DTL p
        JOIN IAS20261.ACCOUNT a ON a.A_CODE = p.A_CODE
        WHERE (a.A_NAME LIKE '%راتب%' OR a.A_NAME LIKE '%رواتب%' OR a.A_NAME LIKE '%تأمين%' OR a.A_NAME LIKE '%بدل%' OR a.A_NAME LIKE '%أجور%')
          AND NVL(p.DOC_POST, 0) = 1
        GROUP BY p.A_CODE, a.A_NAME
        ORDER BY dr DESC
    """)
    rows = cur.fetchall()
    print(f"Found {len(rows)} salary/payroll GL accounts with posting transactions:")
    for r in rows:
        print(f"  Acc: {r[0]} | {r[1]} | Trans Count: {r[2]} | Dr: {r[3]:,.2f} | Cr: {r[4]:,.2f}")

    conn.close()

if __name__ == "__main__":
    find_real_payroll()
