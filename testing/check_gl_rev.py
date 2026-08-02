import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

sql = """
SELECT SUM(CR_AMT) - SUM(DR_AMT)
FROM IAS20261.IAS_POST_DTL 
WHERE A_CODE LIKE '41101%' 
  AND DOC_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') 
  AND DOC_DATE < TO_DATE('2026-06-30','YYYY-MM-DD')+1
  AND NVL(DOC_POST,0) = 1
  AND DOC_TYPE IN (1,2,3,4,5,6,7,8)
"""
cur.execute(sql)
print("GL Revenue for June (Sales only):", cur.fetchone()[0])
