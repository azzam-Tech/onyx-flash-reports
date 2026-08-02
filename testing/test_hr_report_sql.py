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

def test_hr_sql():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    sql = """
     SELECT e.EMP_NO AS "كود الموظف",
            TRIM(e.EMP_L_NM) AS "اسم الموظف",
            TO_CHAR(e.STRT_WRK_DATE, 'YYYY-MM-DD') AS "تاريخ المباشرة",
            CASE WHEN NVL(e.INACTIVE, 0) = 0 THEN 'نشط' ELSE 'موقوف/مستقيل' END AS "حالة الموظف",
            CASE WHEN e.SLRY_PAY_WAY = 2 THEN 'تحويل بنكي' WHEN e.SLRY_PAY_WAY = 1 THEN 'تسليم نقدي' ELSE 'غير محدد' END AS "طريقة استلام الراتب",
            NVL(b.BNK_IBAN, 'غير مسجل') AS "رقم الآيبان IBAN",
            NVL(TO_CHAR(e.SCL_SCRTY_NO), 'غير مسجل') AS "رقم التأمينات (GOSI)",
            NVL(e.INSRNCE_NO, 'غير مسجل') AS "رقم التأمين الطبي",
            TO_CHAR(NVL(e.INSRNCE_OTHRS, 0), 'FM999,999,990.00') AS "مبلغ التأمين",
            CASE WHEN NVL(e.SLRY_CALC, 0) = 1 THEN 'شهري' WHEN NVL(e.SLRY_CALC, 0) = 2 THEN 'يومي' ELSE 'معياري' END AS "احتساب الراتب",
            TO_CHAR(NVL(e.WRK_HRS_DY, 8)) AS "ساعات العمل/يوم",
            TO_CHAR(NVL(e.WRK_DY_MNTH, 30)) AS "أيام العمل/شهر"
     FROM IAS20261.S_EMP e
     LEFT JOIN IAS20261.S_EMP_BNK b ON b.EMP_NO = e.EMP_NO AND NVL(b.SLRY_FLG, 1) = 1
     WHERE (:emp_status IS NULL OR (:emp_status = '1' AND NVL(e.INACTIVE, 0) = 0) OR (:emp_status = '0' AND NVL(e.INACTIVE, 0) = 1))
       AND (:pay_way IS NULL OR TO_CHAR(e.SLRY_PAY_WAY) = :pay_way)
       AND (:emp_search IS NULL OR TO_CHAR(e.EMP_NO) LIKE '%' || :emp_search || '%' OR e.EMP_L_NM LIKE '%' || :emp_search || '%')
     ORDER BY e.EMP_NO
    """
    binds = {"emp_status": None, "pay_way": None, "emp_search": None}
    cur.execute(sql, binds)
    cols = [d[0] for d in cur.description]
    rows = cur.fetchall()

    print("Columns:", cols)
    print(f"Total Rows Fetched: {len(rows)}")
    print("\nFirst 5 Rows:")
    for r in rows[:5]:
        print(" ", r)

    conn.close()

if __name__ == "__main__":
    test_hr_sql()
