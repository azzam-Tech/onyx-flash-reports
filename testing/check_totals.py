import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

sql = """
SELECT SUM(BILL_AMT), SUM(DISC_AMT), SUM(ADD_DISC_AMT_MST),
       SUM(NVL(BILL_AMT,0) - (NVL(DISC_AMT,0) - NVL(ADD_DISC_AMT_MST,0)))
FROM IAS20261.IAS_BILL_MST 
WHERE BILL_DATE >= TO_DATE('2026-01-01','YYYY-MM-DD') 
  AND BILL_DATE <= TO_DATE('2026-06-30','YYYY-MM-DD') 
  AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
"""
cur.execute(sql)
print("Bills Totals Jan-Jun:", cur.fetchone())
