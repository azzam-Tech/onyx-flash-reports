import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

sql = """
SELECT ROUND(SUM(NVL(CR_AMT,0)) / 1.15, 2)
FROM IAS20261.IAS_POST_DTL
WHERE DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
  AND DOC_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') 
  AND DOC_DATE < TO_DATE('2026-06-30','YYYY-MM-DD')+1
"""
cur.execute(sql)
print("Total without grouping:", cur.fetchone()[0])
