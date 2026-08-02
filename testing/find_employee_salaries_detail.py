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

def search_emp_salaries_detail():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    print("=== 1. Checking GOSI status on S_EMP ===")
    cur.execute("""
        SELECT CASE WHEN SCL_SCRTY_NO IS NOT NULL OR SCL_INSRNCE_NO IS NOT NULL THEN 'على التأمينات' ELSE 'ليسوا على التأمينات' END AS gosi_status,
               COUNT(*) cnt
        FROM IAS20261.S_EMP
        GROUP BY CASE WHEN SCL_SCRTY_NO IS NOT NULL OR SCL_INSRNCE_NO IS NOT NULL THEN 'على التأمينات' ELSE 'ليسوا على التأمينات' END
    """)
    for r in cur.fetchall():
        print(" ", r)

    print("\n=== 2. Checking EMPLYMNT_TYP / CTGRY_NO / Job Types in S_EMP ===")
    cur.execute("""
        SELECT NVL(TO_CHAR(EMPLYMNT_TYP), 'غير محدد') typ, COUNT(*) cnt
        FROM IAS20261.S_EMP
        GROUP BY EMPLYMNT_TYP
    """)
    print("EMPLYMNT_TYP distribution:", cur.fetchall())

    print("\n=== 3. Checking Posting Transactions per individual Employee (p.EMP_NO or p.CC_CODE = e.EMP_NO) ===")
    cur.execute("""
        SELECT e.EMP_NO, TRIM(e.EMP_L_NM) emp_name,
               CASE WHEN e.SCL_SCRTY_NO IS NOT NULL OR e.SCL_INSRNCE_NO IS NOT NULL THEN 'تأمينات' ELSE 'بدون تأمينات' END gosi,
               COUNT(p.DOC_NO) post_count,
               SUM(CASE WHEN p.A_CODE LIKE '321%' THEN NVL(p.DR_AMT,0) ELSE 0 END) salary_exp,
               SUM(CASE WHEN p.A_CODE LIKE '11402%' THEN NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0) ELSE 0 END) net_advances
        FROM IAS20261.S_EMP e
        LEFT JOIN IAS20261.IAS_POST_DTL p ON (p.EMP_NO = e.EMP_NO OR p.CC_CODE = e.EMP_NO) AND NVL(p.DOC_POST,0)=1
        GROUP BY e.EMP_NO, e.EMP_L_NM, CASE WHEN e.SCL_SCRTY_NO IS NOT NULL OR e.SCL_INSRNCE_NO IS NOT NULL THEN 'تأمينات' ELSE 'بدون تأمينات' END
        HAVING COUNT(p.DOC_NO) > 0
        ORDER BY salary_exp DESC
    """)
    rows = cur.fetchall()
    print(f"Found {len(rows)} employees with direct GL posting transactions:")
    for r in rows[:15]:
        print(" ", r)

    print("\n=== 4. Checking S_EMP tables in IAS20261 ===")
    cur.execute("""
        SELECT TABLE_NAME FROM ALL_TABLES WHERE OWNER='IAS20261' AND (TABLE_NAME LIKE '%EMP%' OR TABLE_NAME LIKE '%SLRY%') ORDER BY TABLE_NAME
    """)
    tbls = [r[0] for r in cur.fetchall()]
    print("Tables matching EMP or SLRY in IAS20261:", tbls)

    conn.close()

if __name__ == "__main__":
    search_emp_salaries_detail()
