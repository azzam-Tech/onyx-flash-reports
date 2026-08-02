import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

sql1 = """
SELECT SUM(ROUND(NVL(CR_AMT,0) / 1.15, 2)) as method1,
       ROUND(SUM(NVL(CR_AMT,0)) / 1.15, 2) as method2
FROM IAS20261.IAS_POST_DTL
WHERE DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
  AND DOC_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') 
  AND DOC_DATE < TO_DATE('2026-06-30','YYYY-MM-DD')+1
"""
cur.execute(sql1)
print("Methods:", cur.fetchone())

sql2 = """
SELECT SUM(DR_AMT) 
FROM IAS20261.IAS_POST_DTL 
WHERE DOC_TYPE = 15 AND NVL(DOC_POST,0) = 1 
  AND DOC_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') 
  AND DOC_DATE < TO_DATE('2026-06-30','YYYY-MM-DD')+1
  AND DR_AMT > 0 AND A_CODE NOT LIKE '223%'
"""
cur.execute(sql2)
print("True DB Sum:", cur.fetchone())

sql3 = """
SELECT SUM(ext_disc) FROM (
  SELECT CC_CODE, ROUND(SUM(NVL(CR_AMT,0)) / 1.15, 2) as ext_disc
  FROM IAS20261.IAS_POST_DTL
  WHERE DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
    AND DOC_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') 
    AND DOC_DATE < TO_DATE('2026-06-30','YYYY-MM-DD')+1
  GROUP BY CC_CODE
)
"""
cur.execute(sql3)
print("Our Report Sum:", cur.fetchone())
