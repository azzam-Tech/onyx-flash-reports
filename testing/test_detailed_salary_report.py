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

def test_detailed_report():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    sql = """
    SELECT e.EMP_NO AS "كود الموظف",
           TRIM(e.EMP_L_NM) AS "اسم الموظف",
           CASE WHEN NVL(e.INACTIVE, 0) = 0 THEN 'نشط' ELSE 'موقوف/مستقيل' END AS "حالة الموظف",
           TO_CHAR(SUM(CASE WHEN p.A_CODE = '321010003' THEN NVL(p.DR_AMT,0) ELSE 0 END), 'FM999,999,990.00') AS "رواتب التأمينات",
           TO_CHAR(SUM(CASE WHEN p.A_CODE = '321010004' THEN NVL(p.DR_AMT,0) ELSE 0 END), 'FM999,999,990.00') AS "رواتب مؤقتة وعقود",
           TO_CHAR(SUM(CASE WHEN p.A_CODE LIKE '324%' THEN NVL(p.DR_AMT,0) ELSE 0 END), 'FM999,999,990.00') AS "البدلات والمزايا",
           TO_CHAR(SUM(CASE WHEN p.A_CODE LIKE '11402%' THEN NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0) ELSE 0 END), 'FM999,999,990.00') AS "رصيد الذمم والسلف",
           TO_CHAR(SUM(CASE WHEN p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%' THEN NVL(p.DR_AMT,0) ELSE 0 END), 'FM999,999,990.00') AS "إجمالي المستحقات"
    FROM IAS20261.S_EMP e
    LEFT JOIN IAS20261.IAS_POST_DTL p ON (p.EMP_NO = e.EMP_NO OR p.CC_CODE = e.EMP_NO) AND NVL(p.DOC_POST,0)=1
       AND p.DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD')
       AND p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD') + 1
    WHERE (:emp_search IS NULL OR TO_CHAR(e.EMP_NO) LIKE '%' || :emp_search || '%' OR e.EMP_L_NM LIKE '%' || :emp_search || '%')
    GROUP BY e.EMP_NO, e.EMP_L_NM, NVL(e.INACTIVE, 0)
    HAVING (SUM(CASE WHEN p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%' THEN NVL(p.DR_AMT,0) ELSE 0 END) > 0 OR SUM(CASE WHEN p.A_CODE LIKE '11402%' THEN NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0) ELSE 0 END) <> 0)
    ORDER BY SUM(CASE WHEN p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%' THEN NVL(p.DR_AMT,0) ELSE 0 END) DESC
    """
    binds = {"date_from": "2026-01-01", "date_to": "2026-12-31", "emp_search": None}
    cur.execute(sql, binds)
    rows = cur.fetchall()
    print(f"Detailed Employee Salaries query returned {len(rows)} employees:")
    for r in rows[:10]:
        print(" ", r)

    conn.close()

if __name__ == "__main__":
    test_detailed_report()
