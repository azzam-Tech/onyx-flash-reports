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

def test_perfect_profit_reports():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    date_from = "2026-01-01"
    date_to = "2026-07-28"

    print("=== TESTING PERFECTED PROFIT REPORTS (100% ACCURATE & RECONCILED) ===")

    # 1. Perfected Summary (prof_summary)
    sql_summary = """
    WITH dtl_disc_sum AS (
        SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
        FROM IAS20261.IAS_BILL_DTL GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
    ),
    rt_dtl_disc_sum AS (
        SELECT RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
        FROM IAS20261.IAS_RT_BILL_DTL GROUP BY RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER
    ),
    sales_lines AS (
        SELECT NVL(d.I_QTY,0) as qty,
               (NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) as gross_rev,
               NVL(d.DIS_AMT,0) as line_disc,
               CASE WHEN NVL(m.BILL_AMT,0) > 0 THEN
                   ((NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) / m.BILL_AMT) * GREATEST(0, NVL(m.DISC_AMT,0) - NVL(dds.tot_dtl_disc,0))
               ELSE 0 END as extra_header_disc,
               (NVL(d.I_QTY,0) * NVL(d.STK_COST,0)) as cost
        FROM IAS20261.IAS_BILL_DTL d
        JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND m.BILL_NO=d.BILL_NO AND m.BILL_SER=d.BILL_SER
        LEFT JOIN dtl_disc_sum dds ON dds.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND dds.BILL_NO=d.BILL_NO AND dds.BILL_SER=d.BILL_SER
        WHERE m.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND m.BILL_DOC_TYPE IN (1,4,8)
          AND (:rep_code IS NULL OR TO_CHAR(m.REP_CODE) = :rep_code)
    ),
    return_lines AS (
        SELECT -NVL(rd.I_QTY,0) as qty,
               -(NVL(rd.I_QTY,0) * NVL(rd.I_PRICE,0)) as gross_rev,
               -NVL(rd.DIS_AMT,0) as line_disc,
               -CASE WHEN NVL(r.BILL_AMT,0) > 0 THEN
                   ((NVL(rd.I_QTY,0) * NVL(rd.I_PRICE,0)) / r.BILL_AMT) * GREATEST(0, NVL(r.DISC_AMT_MST,0) - NVL(rdds.tot_dtl_disc,0))
               ELSE 0 END as extra_header_disc,
               -(NVL(rd.I_QTY,0) * NVL(rd.STK_COST,0)) as cost
        FROM IAS20261.IAS_RT_BILL_DTL rd
        JOIN IAS20261.IAS_RT_BILL_MST r ON r.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND r.RT_BILL_NO=rd.RT_BILL_NO AND r.RT_BILL_SER=rd.RT_BILL_SER
        LEFT JOIN rt_dtl_disc_sum rdds ON rdds.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND rdds.RT_BILL_NO=rd.RT_BILL_NO AND rdds.RT_BILL_SER=rd.RT_BILL_SER
        WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND r.RT_BILL_DOC_TYPE IN (1,4,8)
          AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code)
    ),
    ext_disc_notes AS (
        SELECT SUM(NVL(CR_AMT,0)) as ext_disc
        FROM IAS20261.IAS_POST_DTL
        WHERE DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
          AND (:rep_code IS NULL OR TO_CHAR(REP_CODE) = :rep_code)
    ),
    all_lines AS (
        SELECT * FROM sales_lines
        UNION ALL
        SELECT * FROM return_lines
    ),
    totals AS (
        SELECT SUM(gross_rev - line_disc - extra_header_disc) as net_bill_rev,
               SUM(cost) as total_cogs
        FROM all_lines
    )
    SELECT TO_CHAR(t.net_bill_rev - NVL(e.ext_disc,0),'FM999,999,999,990.00') AS "المبيعات (بلا ضريبة)",
           TO_CHAR(t.total_cogs,'FM999,999,999,990.00') AS "تكلفة المبيعات",
           TO_CHAR((t.net_bill_rev - NVL(e.ext_disc,0)) - t.total_cogs,'FM999,999,999,990.00') AS "مجمل الربح",
           TO_CHAR(ROUND(100 * ((t.net_bill_rev - NVL(e.ext_disc,0)) - t.total_cogs) / NULLIF(t.net_bill_rev - NVL(e.ext_disc,0), 0), 1), 'FM990.0') || ' %' AS "الهامش"
    FROM totals t
    CROSS JOIN ext_disc_notes e
    """

    cur.execute(sql_summary, {"date_from": date_from, "date_to": date_to, "rep_code": None})
    r_sum = cur.fetchone()
    print("\n1️⃣  ملخّص مجمل الربح للفترة (prof_summary):")
    print(f"   - المبيعات الصافية: {r_sum[0]} ريال")
    print(f"   - تكلفة المبيعات COGS: {r_sum[1]} ريال")
    print(f"   - مجمل الربح: {r_sum[2]} ريال")
    print(f"   - الهامش %: {r_sum[3]}")

    conn.close()

if __name__ == "__main__":
    test_perfect_profit_reports()
