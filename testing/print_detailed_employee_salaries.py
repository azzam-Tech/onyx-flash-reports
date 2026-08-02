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

def print_detailed_salaries():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    cur.execute("""
        SELECT e.EMP_NO AS "كود الموظف",
               TRIM(e.EMP_L_NM) AS "اسم الموظف",
               CASE WHEN e.SCL_SCRTY_NO IS NOT NULL OR e.SCL_INSRNCE_NO IS NOT NULL THEN 'مسجل بالتأمينات' ELSE 'بدون تأمينات / رواتب أخرى' END AS "صفة التغطية والتأمين",
               COUNT(p.DOC_NO) AS "عدد الحركات",
               SUM(CASE WHEN p.A_CODE = '321010003' THEN NVL(p.DR_AMT,0) ELSE 0 END) AS "رواتب التأمينات",
               SUM(CASE WHEN p.A_CODE = '321010004' THEN NVL(p.DR_AMT,0) ELSE 0 END) AS "رواتب مؤقتة / أخرى",
               SUM(CASE WHEN p.A_CODE LIKE '324%' THEN NVL(p.DR_AMT,0) ELSE 0 END) AS "إجمالي البدلات والمزايا",
               SUM(CASE WHEN p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%' THEN NVL(p.DR_AMT,0) ELSE 0 END) AS "إجمالي المستحقات"
        FROM IAS20261.S_EMP e
        LEFT JOIN IAS20261.IAS_POST_DTL p ON (p.EMP_NO = e.EMP_NO OR p.CC_CODE = e.EMP_NO) AND NVL(p.DOC_POST,0)=1
        GROUP BY e.EMP_NO, e.EMP_L_NM, CASE WHEN e.SCL_SCRTY_NO IS NOT NULL OR e.SCL_INSRNCE_NO IS NOT NULL THEN 'مسجل بالتأمينات' ELSE 'بدون تأمينات / رواتب أخرى' END
        ORDER BY SUM(CASE WHEN p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%' THEN NVL(p.DR_AMT,0) ELSE 0 END) DESC
    """)
    rows = cur.fetchall()
    print("=== Detailed Employee Salary Breakdown ===")
    for r in rows:
        if r[7] > 0 or r[3] > 0:
            print(f"EMP {r[0]}: {r[1]} | الصفة: {r[2]} | تأمينات: {r[4]:,.2f} | مؤقتة: {r[5]:,.2f} | بدلات: {r[6]:,.2f} | الإجمالي: {r[7]:,.2f}")

    conn.close()

if __name__ == "__main__":
    print_detailed_salaries()
