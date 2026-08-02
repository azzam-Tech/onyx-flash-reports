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

def test_by_item_query():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    date_from = "2026-01-01"
    date_to = "2026-07-28"

    print("=== 1. Checking Item Sales in IAS_BILL_DTL for 2026 ===")
    cur.execute("""
      SELECT COUNT(DISTINCT dt.I_CODE), SUM(NVL(dt.I_QTY,0)), SUM(NVL(dt.I_QTY,0)*NVL(dt.I_PRICE,0)), SUM(NVL(dt.DIS_AMT,0))
      FROM IAS20261.IAS_BILL_DTL dt
      JOIN IAS20261.IAS_BILL_MST b ON b.BILL_DOC_TYPE=dt.BILL_DOC_TYPE AND b.BILL_NO=dt.BILL_NO AND b.BILL_SER=dt.BILL_SER
      WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        AND b.BILL_DOC_TYPE IN (1,4,8)
    """, {"date_from": date_from, "date_to": date_to})
    r_sales = cur.fetchone()
    print(f" Item Sales (IAS_BILL_DTL): Distinct Items={r_sales[0]}, Total Qty={r_sales[1]:,.2f}, Gross Amt={r_sales[2]:,.2f}, Item Disc={r_sales[3]:,.2f}")

    print("\n=== 2. Checking Item Returns in IAS_RT_BILL_DTL for 2026 ===")
    cur.execute("""
      SELECT COUNT(DISTINCT rdt.I_CODE), SUM(NVL(rdt.I_QTY,0)), SUM(NVL(rdt.I_QTY,0)*NVL(rdt.I_PRICE,0)), SUM(NVL(rdt.DIS_AMT,0))
      FROM IAS20261.IAS_RT_BILL_DTL rdt
      JOIN IAS20261.IAS_RT_BILL_MST r ON r.RT_BILL_DOC_TYPE=rdt.RT_BILL_DOC_TYPE AND r.RT_BILL_NO=rdt.RT_BILL_NO AND r.RT_BILL_SER=rdt.RT_BILL_SER
      WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        AND r.RT_BILL_DOC_TYPE IN (1,4,8)
    """, {"date_from": date_from, "date_to": date_to})
    r_ret = cur.fetchone()
    print(f" Item Returns (IAS_RT_BILL_DTL): Distinct Items={r_ret[0]}, Total Return Qty={r_ret[1]:,.2f}, Return Gross Amt={r_ret[2]:,.2f}, Return Disc={r_ret[3]:,.2f}")

    conn.close()

if __name__ == "__main__":
    test_by_item_query()
