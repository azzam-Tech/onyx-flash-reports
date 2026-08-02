import os
import oracledb

_lib = r"C:\oracle\instantclient\instantclient_23_0"
try:
    oracledb.init_oracle_client(lib_dir=_lib)
    print("Thick mode ON")
except Exception as e:
    print("thick warn:", e)

DB_USER     = os.environ.get("ORA_USER",     "RPT_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD", "ULT2016")
DB_DSN      = os.environ.get("ORA_DSN",      "100.100.1.100:1521/ORCL")

sql = """
WITH sales_base AS (
    SELECT CC_CODE,
           SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as sales
    FROM IAS20261.IAS_BILL_MST
    WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
      AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
    GROUP BY CC_CODE
),
returns_base AS (
    SELECT CC_CODE,
           SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as returns
    FROM IAS20261.IAS_RT_BILL_MST
    WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
      AND RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
    GROUP BY CC_CODE
),
ext_disc_base AS (
    SELECT CC_CODE, ROUND(SUM(NVL(CR_AMT,0)) / 1.15, 2) as ext_disc
    FROM IAS20261.IAS_POST_DTL
    WHERE DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
      AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
      AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
    GROUP BY CC_CODE
),
net_sales_summary AS (
    SELECT NVL(NVL(s.CC_CODE, r.CC_CODE), d.CC_CODE) AS CC_CODE,
           SUM(NVL(s.sales, 0)) - SUM(NVL(r.returns, 0)) - SUM(NVL(d.ext_disc, 0)) AS net_sales
    FROM sales_base s
    FULL OUTER JOIN returns_base r ON s.CC_CODE = r.CC_CODE
    FULL OUTER JOIN ext_disc_base d ON NVL(s.CC_CODE, r.CC_CODE) = d.CC_CODE
    GROUP BY NVL(NVL(s.CC_CODE, r.CC_CODE), d.CC_CODE)
),
col_trans AS (
  SELECT TO_CHAR(CC_CODE) as cc_code, CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as cash_ret, 0 as ext_notice, 0 as rcpt_unknown, 0 as unposted_rcpt
  FROM IAS20261.IAS_POST_DTL
  WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
    AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
  UNION ALL
  SELECT TO_CHAR(CC_CODE), 0, 0, 0, 0, 0, 0, CR_AMT
  FROM IAS20261.IAS_POST_DTL
  WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
    AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
  UNION ALL
  SELECT TO_CHAR(CC_CODE), 0, CR_AMT, 0, 0, 0, 0, 0
  FROM IAS20261.IAS_POST_DTL
  WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
    AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
  UNION ALL
  SELECT TO_CHAR(b.CC_CODE), 0, 0, NVL(p.DR_AMT,0) - NVL(b.DISC_AMT,0), 0, 0, 0, 0
  FROM IAS20261.IAS_BILL_MST b
  JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
  WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
    AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
  UNION ALL
  SELECT TO_CHAR(CC_CODE), 0, 0, 0, CR_AMT, 0, 0, 0
  FROM IAS20261.IAS_POST_DTL
  WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0
    AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
  UNION ALL
  SELECT TO_CHAR(CC_CODE), 0, 0, 0, 0, 0, CR_AMT, 0
  FROM IAS20261.IAS_POST_DTL
  WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NULL
    AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
),
col_summary AS (
  SELECT cc_code,
         SUM(rcpt + unposted_rcpt + net_jrn + cash_sales - cash_ret + rcpt_unknown) as total_collection
  FROM col_trans
  GROUP BY cc_code
)
SELECT NVL(TO_CHAR(ns.CC_CODE), cs.cc_code) AS "كود مركز التكلفة",
       MAX(cc.CC_A_NAME) AS "اسم مركز التكلفة",
       TO_CHAR(NVL(SUM(ns.net_sales), 0), 'FM999,999,999,990.00') AS "صافي المبيعات",
       TO_CHAR(NVL(SUM(cs.total_collection), 0), 'FM999,999,999,990.00') AS "إجمالي التحصيل",
       TO_CHAR(NVL(SUM(ns.net_sales), 0) - NVL(SUM(cs.total_collection), 0), 'FM999,999,999,990.00') AS "الفرق (المبيعات - التحصيل)"
FROM net_sales_summary ns
FULL OUTER JOIN col_summary cs ON TO_CHAR(ns.CC_CODE) = cs.cc_code
LEFT JOIN IAS20261.COST_CENTERS cc ON TO_CHAR(cc.CC_CODE) = NVL(TO_CHAR(ns.CC_CODE), cs.cc_code)
WHERE NVL(TO_CHAR(ns.CC_CODE), cs.cc_code) IS NOT NULL
GROUP BY NVL(TO_CHAR(ns.CC_CODE), cs.cc_code)
HAVING NVL(SUM(ns.net_sales), 0) <> 0 OR NVL(SUM(cs.total_collection), 0) <> 0
ORDER BY SUM(ns.net_sales) DESC
"""

con = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
cur = con.cursor()
cur.execute(sql, {"date_from": "2026-01-01", "date_to": "2026-07-10"})
rows = cur.fetchall()
print("Found rows:", len(rows))
for r in rows[:10]:
    print(r)
con.close()
