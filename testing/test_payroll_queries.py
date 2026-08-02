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

def test_queries():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    print("=== Testing Query 1: Financial Payroll Summary ===")
    sql1 = """
     WITH raw_data AS (
       SELECT p.A_CODE, a.A_NAME,
              CASE WHEN :grp_by = 'rep' THEN NVL(TO_CHAR(p.CC_CODE), 'عام') ELSE TO_CHAR(p.A_CODE) END AS grp_code,
              NVL(p.DR_AMT, 0) AS dr,
              NVL(p.CR_AMT, 0) AS cr,
              p.DOC_DATE
       FROM IAS20261.IAS_POST_DTL p
       JOIN IAS20261.ACCOUNT a ON a.A_CODE = p.A_CODE
       WHERE (p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%' OR p.A_CODE LIKE '11402%' OR p.A_CODE LIKE '21104%')
         AND NVL(p.DOC_POST, 0) = 1
         AND p.DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD')
         AND p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD') + 1
     )
     SELECT r.grp_code AS "الكود",
            MAX(CASE WHEN :grp_by = 'rep' THEN NVL(sm.REPRS_A_NAME, r.grp_code) ELSE r.A_NAME END) AS "اسم الحساب/المندوب",
            COUNT(*) AS "عدد الحركات",
            TO_CHAR(SUM(r.dr), 'FM999,999,990.00') AS "إجمالي الصرف والرواتب",
            TO_CHAR(SUM(r.cr), 'FM999,999,990.00') AS "إجمالي التسويات والدائن",
            TO_CHAR(SUM(r.dr - r.cr), 'FM999,999,990.00') AS "الصافي المالي"
     FROM raw_data r
     LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = r.grp_code
     GROUP BY r.grp_code
     ORDER BY SUM(r.dr) DESC
    """
    binds1 = {"grp_by": "acc", "date_from": "2026-01-01", "date_to": "2026-12-31"}
    cur.execute(sql1, binds1)
    rows1 = cur.fetchall()
    print(f"Query 1 (by Account) returned {len(rows1)} rows:")
    for r in rows1:
        print(" ", r)

    binds1_rep = {"grp_by": "rep", "date_from": "2026-01-01", "date_to": "2026-12-31"}
    cur.execute(sql1, binds1_rep)
    rows1_rep = cur.fetchall()
    print(f"\nQuery 1 (by Salesman/CostCenter) returned {len(rows1_rep)} rows:")
    for r in rows1_rep[:7]:
        print(" ", r)

    print("\n=== Testing Query 2: Employee Advances & Loans ===")
    sql2 = """
     SELECT TO_CHAR(p.DOC_DATE, 'YYYY-MM-DD') AS "التاريخ",
            p.DOC_NO AS "رقم المستند",
            CASE p.DOC_TYPE WHEN 1 THEN 'قيد يومية' WHEN 2 THEN 'سند قبض' WHEN 3 THEN 'سند صرف' ELSE 'قيد أونكس' END AS "نوع المستند",
            NVL(sm.REPRS_A_NAME, TO_CHAR(p.CC_CODE)) AS "المندوب / مركز التكلفة",
            p.A_CODE AS "حساب الذمم",
            TO_CHAR(NVL(p.DR_AMT, 0), 'FM999,999,990.00') AS "سلفة / مدين",
            TO_CHAR(NVL(p.CR_AMT, 0), 'FM999,999,990.00') AS "سداد / دائن",
            NVL(p.PARTICULARS, 'قيد تلقائي') AS "البيان / الشرح"
     FROM IAS20261.IAS_POST_DTL p
     LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(p.CC_CODE)
     WHERE p.A_CODE LIKE '11402%'
       AND NVL(p.DOC_POST, 0) = 1
       AND p.DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD')
       AND p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD') + 1
       AND (:rep_code IS NULL OR TO_CHAR(p.CC_CODE) = :rep_code)
     ORDER BY p.DOC_DATE DESC, p.DOC_NO DESC
     FETCH FIRST 10 ROWS ONLY
    """
    binds2 = {"date_from": "2026-01-01", "date_to": "2026-12-31", "rep_code": None}
    cur.execute(sql2, binds2)
    rows2 = cur.fetchall()
    print(f"\nQuery 2 returned {len(rows2)} sample rows:")
    for r in rows2:
        print(" ", r)

    conn.close()

if __name__ == "__main__":
    test_queries()
