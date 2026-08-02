import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

sql = """
SELECT BILL_NO, BILL_AMT, DISC_AMT, ADD_DISC_AMT_MST, TOT_AMT
FROM IAS20261.IAS_BILL_MST 
WHERE BILL_DATE >= TO_DATE('2026-01-01','YYYY-MM-DD') 
  AND BILL_DATE <= TO_DATE('2026-06-30','YYYY-MM-DD') 
  AND DISC_AMT > 0
FETCH FIRST 5 ROWS ONLY
"""
cur.execute(sql)
print("Samples:", cur.fetchall())
