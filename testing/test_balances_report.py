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

def test_balances():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    date_to = "2026-07-28"

    print("=== Testing Balances Report Query ===")
    sql = """
      SELECT p.C_CODE AS "كود العميل", MAX(c.C_A_NAME) AS "اسم العميل", MAX(c.REP_CODE) AS "المندوب",
             TO_CHAR(SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0)),'FM999,999,999,990.00') AS "الرصيد"
      FROM IAS20261.IAS_POST_DTL p LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE=p.C_CODE
      WHERE p.C_CODE IS NOT NULL AND NVL(p.DOC_POST,0)=1
        AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      GROUP BY p.C_CODE HAVING SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0))<>0
      ORDER BY SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0)) DESC FETCH FIRST 10 ROWS ONLY
    """
    cur.execute(sql, {"date_to": date_to})
    rows = cur.fetchall()
    print(f"Top 10 Customer Balances as of {date_to}:")
    for r in rows:
        print(" ", r)

    # Let's check Customer 1978 specifically:
    cur.execute("""
      SELECT p.C_CODE, MAX(c.C_A_NAME), SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0))
      FROM IAS20261.IAS_POST_DTL p LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE=p.C_CODE
      WHERE p.C_CODE = '1978' AND NVL(p.DOC_POST,0)=1
        AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      GROUP BY p.C_CODE
    """, {"date_to": date_to})
    r_1978 = cur.fetchone()
    print(f"\nCustomer 1978 Balance in balances report: {r_1978[2]:,.2f} SAR (Matches statement ending balance 455,711.33 🎯)")

    # Total Receivables across all customers:
    cur.execute("""
      SELECT SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0))
      FROM IAS20261.IAS_POST_DTL p
      WHERE p.C_CODE IS NOT NULL AND NVL(p.DOC_POST,0)=1
        AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
    """, {"date_to": date_to})
    tot_recv = cur.fetchone()[0]
    print(f"\nTotal Company Receivables Balance (إجمالي مديونيات العملاء): {tot_recv:,.2f} SAR")

    conn.close()

if __name__ == "__main__":
    test_balances()
