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

def test_amount_search():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    sql = """
    SELECT TO_CHAR(p.DOC_DATE, 'YYYY-MM-DD') AS "التاريخ",
           p.DOC_NO AS "رقم المستند",
           CASE p.DOC_TYPE WHEN 1 THEN 'قيد يومية' WHEN 2 THEN 'سند قبض' WHEN 3 THEN 'سند صرف' ELSE 'قيد أونكس' END AS "نوع المستند",
           NVL(sm.REPRS_A_NAME, TO_CHAR(p.CC_CODE)) AS "الجهة / مركز التكلفة",
           TO_CHAR(NVL(p.DR_AMT, 0), 'FM999,999,990.00') AS "المبلغ / سلفة / راتب",
           TO_CHAR(NVL(p.CR_AMT, 0), 'FM999,999,990.00') AS "سداد / تسوية",
           NVL(p.DOC_DESC, 'قيد تلقائي') AS "اسم الموظف / البيان والتفاصيل"
    FROM IAS20261.IAS_POST_DTL p
    LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(p.CC_CODE)
    WHERE (p.A_CODE LIKE '11402%' OR p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%')
      AND NVL(p.DOC_POST, 0) = 1
      AND p.DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD')
      AND p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD') + 1
      AND (:min_amt IS NULL OR NVL(p.DR_AMT, 0) >= TO_NUMBER(:min_amt) OR NVL(p.CR_AMT, 0) >= TO_NUMBER(:min_amt))
      AND (:max_amt IS NULL OR (NVL(p.DR_AMT, 0) <= TO_NUMBER(:max_amt) AND NVL(p.CR_AMT, 0) <= TO_NUMBER(:max_amt)))
      AND (:text_search IS NULL OR p.DOC_DESC LIKE '%' || :text_search || '%' OR sm.REPRS_A_NAME LIKE '%' || :text_search || '%')
    ORDER BY p.DOC_DATE DESC, p.DOC_NO DESC
    FETCH FIRST 15 ROWS ONLY
    """
    binds = {
        "date_from": "2026-01-01",
        "date_to": "2026-12-31",
        "min_amt": "2000",
        "max_amt": "5000",
        "text_search": None
    }
    cur.execute(sql, binds)
    rows = cur.fetchall()
    print(f"Amount Filter Query (between 2000 and 5000 SAR) returned {len(rows)} rows:")
    for r in rows:
        print(" ", r)

    conn.close()

if __name__ == "__main__":
    test_amount_search()
