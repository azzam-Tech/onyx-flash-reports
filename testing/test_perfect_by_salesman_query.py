IAS_ITEM_PRICEimport os
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

def test_perfect_by_salesman():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    date_from = "2026-01-01"
    date_to = "2026-07-28"

    sql = """
    WITH sales_mst AS (
        SELECT TO_CHAR(b.REP_CODE) as rep_code,
               TO_CHAR(b.C_CODE) as c_code,
               1 as is_sale,
               0 as is_ret,
               NVL(b.BILL_AMT,0) as gross_amt,
               NVL(b.DISC_AMT,0) as disc_amt,
               0 as ext_disc,
               NVL(b.VAT_AMT,0) as vat_amt,
               NVL(b.OTHR_AMT,0) as othr_amt
        FROM IAS20261.IAS_BILL_MST b
        LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(b.REP_CODE)
        WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND b.BILL_DOC_TYPE IN (1,4,8)
          AND b.REP_CODE IS NOT NULL
          AND (:rep_code IS NULL OR TO_CHAR(b.REP_CODE) = :rep_code OR sm.REPRS_A_NAME LIKE '%' || :rep_code || '%')
    ),
    returns_mst AS (
        SELECT TO_CHAR(r.REP_CODE) as rep_code,
               TO_CHAR(r.C_CODE) as c_code,
               0 as is_sale,
               1 as is_ret,
               NVL(r.BILL_AMT,0) as gross_amt,
               NVL(r.DISC_AMT_MST,0) as disc_amt,
               0 as ext_disc,
               NVL(r.VAT_AMT,0) as vat_amt,
               0 as othr_amt
        FROM IAS20261.IAS_RT_BILL_MST r
        LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(r.REP_CODE)
        WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND r.RT_BILL_DOC_TYPE IN (1,4,8)
          AND r.REP_CODE IS NOT NULL
          AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code OR sm.REPRS_A_NAME LIKE '%' || :rep_code || '%')
    ),
    ext_disc_notes AS (
        SELECT TO_CHAR(p.REP_CODE) as rep_code,
               TO_CHAR(p.C_CODE) as c_code,
               0 as is_sale,
               0 as is_ret,
               0 as gross_amt,
               0 as disc_amt,
               NVL(p.CR_AMT,0) as ext_disc,
               0 as vat_amt,
               0 as othr_amt
        FROM IAS20261.IAS_POST_DTL p
        LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(p.REP_CODE)
        WHERE p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND p.DOC_TYPE = 15 AND NVL(p.CR_AMT,0) > 0 AND NVL(p.DOC_POST,0) = 1
          AND p.REP_CODE IS NOT NULL
          AND (:rep_code IS NULL OR TO_CHAR(p.REP_CODE) = :rep_code OR sm.REPRS_A_NAME LIKE '%' || :rep_code || '%')
    ),
    all_rep_trans AS (
        SELECT * FROM sales_mst
        UNION ALL
        SELECT * FROM returns_mst
        UNION ALL
        SELECT * FROM ext_disc_notes
    )
    SELECT t.rep_code AS "كود المندوب",
           MAX(sm.REPRS_A_NAME) AS "اسم المندوب",
           COUNT(DISTINCT t.c_code) AS "عدد العملاء",
           SUM(t.is_sale) AS "فواتير مبيعات",
           SUM(t.is_ret) AS "فواتير مرتجعات",
           TO_CHAR(SUM(t.gross_amt * t.is_sale),'FM999,999,999,990.00') AS "المبيعات",
           TO_CHAR(SUM(t.gross_amt * t.is_ret),'FM999,999,999,990.00') AS "المردودات (-)",
           TO_CHAR(SUM(t.disc_amt * t.is_sale - t.disc_amt * t.is_ret),'FM999,999,999,990.00') AS "خصم الفواتير والأصناف (-)",
           TO_CHAR(SUM(t.ext_disc),'FM999,999,999,990.00') AS "إشعار خصم مستقل (-)",
           TO_CHAR(SUM((t.gross_amt - t.disc_amt) * t.is_sale - (t.gross_amt - t.disc_amt) * t.is_ret - t.ext_disc),'FM999,999,999,990.00') AS "الصافي قبل الضريبة",
           TO_CHAR(SUM((t.gross_amt - t.disc_amt + t.vat_amt + t.othr_amt) * t.is_sale - (t.gross_amt - t.disc_amt + t.vat_amt) * t.is_ret - t.ext_disc),'FM999,999,999,990.00') AS "الإجمالي بالضريبة"
    FROM all_rep_trans t
    LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(t.rep_code)
    GROUP BY t.rep_code
    ORDER BY SUM((t.gross_amt - t.disc_amt) * t.is_sale - (t.gross_amt - t.disc_amt) * t.is_ret - t.ext_disc) DESC
    FETCH FIRST 300 ROWS ONLY
    """

    params = {"date_from": date_from, "date_to": date_to, "rep_code": None}
    cur.execute(sql, params)
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]

    print(f"Perfect By Salesman Query returned {len(rows)} rows with {len(cols)} columns:")
    print("Cols:", cols)
    for r in rows[:10]:
        print(" ", r)

    conn.close()

if __name__ == "__main__":
    test_perfect_by_salesman()
