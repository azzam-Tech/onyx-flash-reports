import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

sql = """
SELECT SUM(BILL_AMT)
FROM IAS20261.IAS_RT_BILL_MST 
WHERE RT_BILL_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') 
  AND RT_BILL_DATE < TO_DATE('2026-06-30','YYYY-MM-DD')+1
  AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
"""
cur.execute(sql)
returns = cur.fetchone()[0]

sql = """
SELECT ROUND(SUM(NVL(CR_AMT,0)) / 1.15, 2) as ext_disc
FROM IAS20261.IAS_POST_DTL
WHERE DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
  AND DOC_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') 
  AND DOC_DATE < TO_DATE('2026-06-30','YYYY-MM-DD')+1
"""
cur.execute(sql)
disc = cur.fetchone()[0]

sales = 17098027.14

net = sales - returns - disc
print(f"Sales: {sales}, Returns: {returns}, Disc: {disc}, Net: {net}")

