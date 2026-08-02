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

def check_returns_and_sales():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    print("=== 1. Checking IAS_BILL_MST Document Types and Counts for 2026 ===")
    cur.execute("""
        SELECT b.BILL_DOC_TYPE, COUNT(*), SUM(NVL(b.BILL_AMT,0)), SUM(NVL(b.DISC_AMT,0)), SUM(NVL(b.VAT_AMT,0))
        FROM IAS20261.IAS_BILL_MST b
        WHERE b.BILL_DATE >= TO_DATE('2026-01-01','YYYY-MM-DD') AND b.BILL_DATE <= TO_DATE('2026-07-28','YYYY-MM-DD')
        GROUP BY b.BILL_DOC_TYPE
        ORDER BY b.BILL_DOC_TYPE
    """)
    for r in cur.fetchall():
        print(f"  IAS_BILL_MST DOC_TYPE {r[0]}: Count={r[1]}, Total AMT={r[2]:,.2f}, Total DISC={r[3]:,.2f}, Total VAT={r[4]:,.2f}")

    print("\n=== 2. Checking IAS_RT_BILL_MST (Sales Returns) for 2026 ===")
    cur.execute("""
        SELECT r.RT_BILL_DOC_TYPE, COUNT(*), SUM(NVL(r.BILL_AMT,0)), SUM(NVL(r.DISC_AMT_MST,0)), SUM(NVL(r.VAT_AMT,0))
        FROM IAS20261.IAS_RT_BILL_MST r
        WHERE r.RT_BILL_DATE >= TO_DATE('2026-01-01','YYYY-MM-DD') AND r.RT_BILL_DATE <= TO_DATE('2026-07-28','YYYY-MM-DD')
        GROUP BY r.RT_BILL_DOC_TYPE
        ORDER BY r.RT_BILL_DOC_TYPE
    """)
    for r in cur.fetchall():
        print(f"  IAS_RT_BILL_MST RT_BILL_DOC_TYPE {r[0]}: Count={r[1]}, Total AMT={r[2]:,.2f}, Total DISC={r[3]:,.2f}, Total VAT={r[4]:,.2f}")

    print("\n=== 3. Checking Customer Name & Salesman Name in Sales Invoices ===")
    cur.execute("""
        SELECT b.BILL_NO, b.BILL_DOC_TYPE, TO_CHAR(b.BILL_DATE,'YYYY-MM-DD'),
               b.C_CODE, c.C_A_NAME,
               b.REP_CODE, sm.REPRS_A_NAME,
               b.BILL_AMT, b.DISC_AMT, b.VAT_AMT,
               (NVL(b.BILL_AMT,0) - NVL(b.DISC_AMT,0) + NVL(b.VAT_AMT,0)) as correct_net_vat
        FROM IAS20261.IAS_BILL_MST b
        LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = b.C_CODE
        LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE = b.REP_CODE
        WHERE b.BILL_DATE >= TO_DATE('2026-01-01','YYYY-MM-DD')
          AND ROWNUM <= 5
    """)
    for r in cur.fetchall():
        print(f" Invoice {r[0]} (Type {r[1]}, Date {r[2]}): Cust={r[3]} ({r[4]}), Rep={r[5]} ({r[6]}), Gross={r[7]}, Disc={r[8]}, VAT={r[9]}, Net+VAT={r[10]}")

    conn.close()

if __name__ == "__main__":
    check_returns_and_sales()
