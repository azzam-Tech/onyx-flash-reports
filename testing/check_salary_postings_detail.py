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

def check_salary_postings():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    print("=== Sample Postings for Account 321010003 (مصاريف رواتب التأمينات) ===")
    cur.execute("""
        SELECT p.DOC_DATE, p.DOC_NO, p.DOC_DESC, p.DR_AMT, p.CC_CODE, p.REP_CODE, p.V_CODE, p.EMP_NO
        FROM IAS20261.IAS_POST_DTL p
        WHERE p.A_CODE = '321010003' AND NVL(p.DOC_POST,0) = 1 AND ROWNUM <= 15
        ORDER BY p.DOC_DATE DESC
    """)
    for r in cur.fetchall():
        print(" ", r)

    print("\n=== Sample Postings for Account 321010004 (مصاريف رواتب مؤقتة) ===")
    cur.execute("""
        SELECT p.DOC_DATE, p.DOC_NO, p.DOC_DESC, p.DR_AMT, p.CC_CODE, p.REP_CODE, p.V_CODE, p.EMP_NO
        FROM IAS20261.IAS_POST_DTL p
        WHERE p.A_CODE = '321010004' AND NVL(p.DOC_POST,0) = 1 AND ROWNUM <= 15
        ORDER BY p.DOC_DATE DESC
    """)
    for r in cur.fetchall():
        print(" ", r)

    conn.close()

if __name__ == "__main__":
    check_salary_postings()
