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

def investigate_bills():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    print("=== 1. Inspecting IAS_BILL_MST fields for Sales Invoices ===")
    cur.execute("""
      SELECT b.BILL_DOC_TYPE, b.BILL_NO, b.BILL_SER, b.BILL_AMT, b.DISC_AMT, b.DISC_AMT_MST, b.VAT_AMT, b.OTHR_AMT
      FROM IAS20261.IAS_BILL_MST b
      WHERE b.BILL_DOC_TYPE IN (1,4) AND ROWNUM <= 10
    """)
    rows = cur.fetchall()
    print("Sample Invoices from IAS_BILL_MST:")
    for r in rows:
        b_type, b_no, b_ser, b_amt, disc, disc_mst, vat, othr = r
        print(f" Bill {b_no} (Type {b_type}): BILL_AMT={b_amt}, DISC_AMT={disc}, DISC_AMT_MST={disc_mst}, VAT={vat}, OTHR={othr}")

    print("\n=== 2. Comparing IAS_BILL_MST BILL_AMT vs IAS_BILL_DTL sums ===")
    cur.execute("""
      SELECT b.BILL_DOC_TYPE, b.BILL_NO, b.BILL_AMT, b.DISC_AMT, b.DISC_AMT_MST, b.VAT_AMT,
             (SELECT SUM(NVL(DIS_AMT,0)) FROM IAS20261.IAS_BILL_DTL d WHERE d.BILL_DOC_TYPE=b.BILL_DOC_TYPE AND d.BILL_NO=b.BILL_NO AND d.BILL_SER=b.BILL_SER) as itm_disc,
             (SELECT SUM(NVL(I_QTY,0)*NVL(I_PRICE,0)) FROM IAS20261.IAS_BILL_DTL d WHERE d.BILL_DOC_TYPE=b.BILL_DOC_TYPE AND d.BILL_NO=b.BILL_NO AND d.BILL_SER=b.BILL_SER) as dtl_gross
      FROM IAS20261.IAS_BILL_MST b
      WHERE b.BILL_DOC_TYPE IN (1,4) AND ROWNUM <= 10
    """)
    for r in cur.fetchall():
        print(f" Bill {r[1]} (Type {r[0]}): Gross AMT={r[2]} | DISC_AMT={r[3]} | DISC_MST={r[4]} | DTL Item Disc={r[6]} | DTL Gross={r[7]}")

    print("\n=== 3. Checking Document Types (b.BILL_DOC_TYPE) in Onyx ===")
    cur.execute("""
      SELECT DISTINCT b.BILL_DOC_TYPE
      FROM IAS20261.IAS_BILL_MST b
      WHERE b.BILL_DOC_TYPE IS NOT NULL
      ORDER BY b.BILL_DOC_TYPE
    """)
    print("All BILL_DOC_TYPEs in IAS_BILL_MST:", [r[0] for r in cur.fetchall()])

    print("\n=== 4. Checking Salesman Name join in IAS_BILL_MST ===")
    cur.execute("""
      SELECT b.BILL_NO, b.REP_CODE, sm.REPRS_A_NAME
      FROM IAS20261.IAS_BILL_MST b
      LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE = b.REP_CODE
      WHERE b.REP_CODE IS NOT NULL AND ROWNUM <= 5
    """)
    for r in cur.fetchall():
        print(f" Bill {r[0]}: RepCode={r[1]} -> RepName='{r[2]}'")

    conn.close()

if __name__ == "__main__":
    investigate_bills()
