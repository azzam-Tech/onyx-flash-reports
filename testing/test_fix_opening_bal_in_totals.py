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

def test_add_total_row_fix():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    c_code = "1978"
    date_from = "2026-01-01"
    date_to = "2026-07-28"

    sql = """
    WITH open_bal AS (
      SELECT NVL(SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0)),0) as bal
      FROM IAS20261.IAS_POST_DTL
      WHERE C_CODE = :c_code AND NVL(DOC_POST,0)=1
        AND (DOC_DATE < TO_DATE(:date_from,'YYYY-MM-DD') OR NVL(DOC_TYPE,0) = 0)
    ),
    trans AS (
      SELECT p.DOC_DATE, NVL(d.JV_NAME, 'قيد يومية') AS jv_name, p.DOC_NO, p.DOC_DESC,
             NVL(p.DR_AMT,0) dr, NVL(p.CR_AMT,0) cr, p.DOC_SER
      FROM IAS20261.IAS_POST_DTL p
      LEFT JOIN IAS_SYS.IAS_DOCJV_TYPE_SYSTEMS d ON d.DOC_TYPE=p.DOC_TYPE AND d.JV_TYPE=p.JV_TYPE AND d.LANG_NO=1
      WHERE p.C_CODE = :c_code AND NVL(p.DOC_POST,0)=1
        AND NVL(p.DOC_TYPE,0) <> 0
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
        AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
    )
    SELECT "التاريخ","نوع المستند","رقم المستند","البيان","مدين","دائن","الرصيد" FROM (
      SELECT TO_CHAR(TO_DATE(:date_from,'YYYY-MM-DD')-1, 'YYYY-MM-DD') AS "التاريخ",
             'رصيد افتتاحي' AS "نوع المستند",
             NULL AS "رقم المستند",
             'رصيد ما قبل الفترة' AS "البيان",
             TO_CHAR(CASE WHEN bal>0 THEN bal ELSE 0 END,'FM999,999,990.00') AS "مدين",
             TO_CHAR(CASE WHEN bal<0 THEN -bal ELSE 0 END,'FM999,999,990.00') AS "دائن",
             TO_CHAR(NVL(bal,0),'FM999,999,990.00') AS "الرصيد",
             TO_DATE('1900-01-01','YYYY-MM-DD') s1, 0 s2, 0 s3
      FROM open_bal
      UNION ALL
      SELECT TO_CHAR(t.DOC_DATE,'YYYY-MM-DD'),
             t.jv_name,
             t.DOC_NO,
             t.DOC_DESC,
             TO_CHAR(t.dr,'FM999,999,990.00'),
             TO_CHAR(t.cr,'FM999,999,990.00'),
             TO_CHAR((SELECT NVL(bal,0) FROM open_bal) + SUM(t.dr-t.cr) OVER (ORDER BY t.DOC_DATE, t.DOC_NO, t.DOC_SER), 'FM999,999,990.00'),
             t.DOC_DATE s1, t.DOC_NO s2, t.DOC_SER s3
      FROM trans t
    ) ORDER BY s1, s2, s3 FETCH FIRST 1000 ROWS ONLY
    """
    cur.execute(sql, {"c_code": c_code, "date_from": date_from, "date_to": date_to})
    rows = cur.fetchall()
    cols = ["التاريخ","نوع المستند","رقم المستند","البيان","مدين","دائن","الرصيد"]

    # Simulating add_total_row WITH skipping opening balance row
    totals = [0.0] * len(cols)
    for r in rows:
        if r and len(r) > 1 and str(r[1]).strip() == "رصيد افتتاحي":
            continue # SKIP OPENING BALANCE ROW IN MOVEMENT TOTALS
        if r[4]: totals[4] += float(r[4].replace(',',''))
        if r[5]: totals[5] += float(r[5].replace(',',''))

    final_bal = float(rows[-1][6].replace(',',''))

    total_row = [
        "الإجمالي",
        "",
        "",
        "",
        f"{totals[4]:,.2f}",
        f"{totals[5]:,.2f}",
        f"{final_bal:,.2f}"
    ]

    print("=== FIXED TOTAL ROW (EXCLUDING OPENING BALANCE) ===")
    print("Cols:", cols)
    print("Total Row:", total_row)

    conn.close()

if __name__ == "__main__":
    test_add_total_row_fix()
