import os
import oracledb

_lib = r"C:\oracle\instantclient\instantclient_23_0"
try:
    oracledb.init_oracle_client(lib_dir=_lib)
except Exception as e:
    print("thick warn:", e)

DB_USER     = os.environ.get("ORA_USER",     "RPT_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD", "ULT2016")
DB_DSN      = os.environ.get("ORA_DSN",      "100.100.1.100:1521/ORCL")

def get_conn():
    return oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)

sql = """
WITH col_trans AS (
  -- Receipts posted with customer
  SELECT TO_CHAR(DOC_DATE, 'YYYY-MM') as m, CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as cash_ret, 0 as unposted_rcpt
  FROM IAS20261.IAS_POST_DTL
  WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
    AND DOC_DATE >= TO_DATE('2026-01-01','YYYY-MM-DD') AND DOC_DATE < TO_DATE('2026-12-31','YYYY-MM-DD')+1
  UNION ALL
  -- Unposted Receipts with customer
  SELECT TO_CHAR(DOC_DATE, 'YYYY-MM'), 0, 0, 0, 0, CR_AMT
  FROM IAS20261.IAS_POST_DTL
  WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
    AND DOC_DATE >= TO_DATE('2026-01-01','YYYY-MM-DD') AND DOC_DATE < TO_DATE('2026-12-31','YYYY-MM-DD')+1
  UNION ALL
  -- Network Journals
  SELECT TO_CHAR(DOC_DATE, 'YYYY-MM'), 0, CR_AMT, 0, 0, 0
  FROM IAS20261.IAS_POST_DTL
  WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
    AND DOC_DATE >= TO_DATE('2026-01-01','YYYY-MM-DD') AND DOC_DATE < TO_DATE('2026-12-31','YYYY-MM-DD')+1
  UNION ALL
  -- Cash Sales
  SELECT TO_CHAR(b.BILL_DATE, 'YYYY-MM'), 0, 0, NVL(p.DR_AMT,0) - NVL(b.DISC_AMT,0), 0, 0
  FROM IAS20261.IAS_BILL_MST b
  JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
  WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
    AND b.BILL_DATE >= TO_DATE('2026-01-01','YYYY-MM-DD') AND b.BILL_DATE < TO_DATE('2026-12-31','YYYY-MM-DD')+1
  UNION ALL
  -- Cash Returns
  SELECT TO_CHAR(DOC_DATE, 'YYYY-MM'), 0, 0, 0, CR_AMT, 0
  FROM IAS20261.IAS_POST_DTL
  WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0
    AND DOC_DATE >= TO_DATE('2026-01-01','YYYY-MM-DD') AND DOC_DATE < TO_DATE('2026-12-31','YYYY-MM-DD')+1
)
SELECT m, SUM(rcpt + unposted_rcpt + net_jrn + cash_sales - cash_ret)
FROM col_trans
GROUP BY m
ORDER BY m
"""

con = get_conn()
cur = con.cursor()
cur.execute(sql)
print("Monthly Commercial Adopted Collection Totals for 2026:")
for m, tot in cur.fetchall():
    print(f"Month {m}: {tot:,.2f}")
con.close()
