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

def test_clean_payroll():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    sql = """
    SELECT p.A_CODE AS "كود الحساب",
           a.A_NAME AS "اسم البند المحاسبي",
           COUNT(*) AS "عدد الحركات",
           TO_CHAR(SUM(NVL(p.DR_AMT,0)), 'FM999,999,990.00') AS "إجمالي الصرف والرواتب",
           TO_CHAR(SUM(NVL(p.CR_AMT,0)), 'FM999,999,990.00') AS "إجمالي التسويات والدائن",
           TO_CHAR(SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)), 'FM999,999,990.00') AS "الصافي المالي"
    FROM IAS20261.IAS_POST_DTL p
    JOIN IAS20261.ACCOUNT a ON a.A_CODE = p.A_CODE
    WHERE (p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%' OR p.A_CODE LIKE '11402%' OR p.A_CODE LIKE '21104%')
      AND NVL(p.DOC_POST, 0) = 1
      AND p.DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD')
      AND p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD') + 1
    GROUP BY p.A_CODE, a.A_NAME
    ORDER BY SUM(NVL(p.DR_AMT,0)) DESC
    """
    binds = {"date_from": "2026-01-01", "date_to": "2026-12-31"}
    cur.execute(sql, binds)
    rows = cur.fetchall()
    print(f"Clean payroll query returned {len(rows)} rows:")
    for r in rows[:10]:
        print(" ", r)

    conn.close()

if __name__ == "__main__":
    test_clean_payroll()
