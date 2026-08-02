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

def test_statement_1978_detail():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    c_code = "1978"
    date_from = "2026-01-01"
    date_to = "2026-07-28"

    print("=== 1. Grouping Transactions for C_CODE 1978 by DOC_TYPE, JV_TYPE, A_CODE ===")
    cur.execute("""
        SELECT p.DOC_TYPE, p.JV_TYPE, d.JV_NAME, p.A_CODE, a.A_NAME,
               COUNT(*), SUM(NVL(p.DR_AMT,0)) dr, SUM(NVL(p.CR_AMT,0)) cr
        FROM IAS20261.IAS_POST_DTL p
        LEFT JOIN IAS20261.ACCOUNT a ON a.A_CODE = p.A_CODE
        LEFT JOIN IAS_SYS.IAS_DOCJV_TYPE_SYSTEMS d ON d.DOC_TYPE=p.DOC_TYPE AND d.JV_TYPE=p.JV_TYPE AND d.LANG_NO=1
        WHERE p.C_CODE = :c_code AND NVL(p.DOC_POST,0)=1
          AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY p.DOC_TYPE, p.JV_TYPE, d.JV_NAME, p.A_CODE, a.A_NAME
        ORDER BY p.DOC_TYPE, p.A_CODE
    """, {"c_code": c_code, "date_from": date_from, "date_to": date_to})
    rows = cur.fetchall()
    print(f"Grouped Transactions ({len(rows)} categories):")
    tot_dr, tot_cr = 0, 0
    for r in rows:
        print(" ", r)
        tot_dr += r[6]
        tot_cr += r[7]

    print(f"\nTOTAL: Debit={tot_dr:,.2f}, Credit={tot_cr:,.2f}")

    print("\n=== 2. Opening Balance Before 2026-01-01 ===")
    cur.execute("""
        SELECT NVL(SUM(NVL(DR_AMT,0)),0) dr, NVL(SUM(NVL(CR_AMT,0)),0) cr, NVL(SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0)),0) net
        FROM IAS20261.IAS_POST_DTL
        WHERE C_CODE = :c_code AND NVL(DOC_POST,0)=1
          AND DOC_DATE < TO_DATE(:date_from,'YYYY-MM-DD')
    """, {"c_code": c_code, "date_from": date_from})
    op_dr, op_cr, op_net = cur.fetchone()
    print(f"Opening Balance before {date_from}: Op_DR={op_dr:,.2f}, Op_CR={op_cr:,.2f}, Op_Net={op_net:,.2f}")

    print("\n=== 3. Why did app.py show Balance = 40,654,714.10? ===")
    # Let's check how app.py calculates running balance or totals in statement report!
    cur.execute("""
       WITH open_bal AS (
         SELECT NVL(SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0)),0) as bal
         FROM IAS20261.IAS_POST_DTL
         WHERE C_CODE = :c_code AND NVL(DOC_POST,0)=1
           AND DOC_DATE < TO_DATE(:date_from,'YYYY-MM-DD')
       ),
       trans AS (
         SELECT p.DOC_DATE, d.JV_NAME, p.DOC_NO, p.DOC_DESC, NVL(p.DR_AMT,0) dr, NVL(p.CR_AMT,0) cr, p.DOC_SER
         FROM IAS20261.IAS_POST_DTL p
         LEFT JOIN IAS_SYS.IAS_DOCJV_TYPE_SYSTEMS d ON d.DOC_TYPE=p.DOC_TYPE AND d.JV_TYPE=p.JV_TYPE AND d.LANG_NO=1
         WHERE p.C_CODE = :c_code AND NVL(p.DOC_POST,0)=1
           AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       )
       SELECT "التاريخ","نوع المستند","رقم المستند","البيان","مدين","دائن","الرصيد" FROM (
         SELECT TO_CHAR(TO_DATE(:date_from,'YYYY-MM-DD')-1, 'YYYY-MM-DD') AS "التاريخ", 'رصيد افتتاحي' AS "نوع المستند",
                NULL AS "رقم المستند", 'رصيد ما قبل الفترة' AS "البيان",
                TO_CHAR(CASE WHEN bal>0 THEN bal ELSE 0 END,'FM999,999,990.00') AS "مدين",
                TO_CHAR(CASE WHEN bal<0 THEN -bal ELSE 0 END,'FM999,999,990.00') AS "دائن",
                TO_CHAR(NVL(bal,0),'FM999,999,990.00') AS "الرصيد",
                TO_DATE('1900-01-01','YYYY-MM-DD') s1, 0 s2, 0 s3
         FROM open_bal
         UNION ALL
         SELECT TO_CHAR(t.DOC_DATE,'YYYY-MM-DD'), t.JV_NAME, t.DOC_NO, t.DOC_DESC,
                TO_CHAR(t.dr,'FM999,999,990.00'), TO_CHAR(t.cr,'FM999,999,990.00'),
                TO_CHAR((SELECT NVL(bal,0) FROM open_bal) + SUM(t.dr-t.cr) OVER (ORDER BY t.DOC_DATE, t.DOC_NO, t.DOC_SER), 'FM999,999,990.00'),
                t.DOC_DATE s1, t.DOC_NO s2, t.DOC_SER s3
         FROM trans t
       ) ORDER BY s1, s2, s3 FETCH FIRST 10 ROWS ONLY
    """, {"c_code": c_code, "date_from": date_from, "date_to": date_to})
    stmt_rows = cur.fetchall()
    print(f"Statement rows in app.py for C_CODE={c_code}:")
    for r in stmt_rows:
        print(" ", r)

    conn.close()

if __name__ == "__main__":
    test_statement_1978_detail()
