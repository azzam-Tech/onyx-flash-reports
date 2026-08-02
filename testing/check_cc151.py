import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

sql = """
SELECT BILL_DOC_TYPE, SUM(BILL_AMT), SUM(DISC_AMT), SUM(ADD_DISC_AMT_MST)
FROM IAS20261.IAS_BILL_MST 
WHERE CC_CODE='151' 
  AND BILL_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') 
  AND BILL_DATE < TO_DATE('2026-06-30','YYYY-MM-DD')+1
GROUP BY BILL_DOC_TYPE
"""
cur.execute(sql)
print("CC 151 by DOC_TYPE:")
for row in cur.fetchall():
    print(row)
