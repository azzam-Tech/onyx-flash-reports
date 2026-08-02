import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

sql = """
SELECT BILL_NO, BILL_DOC_TYPE, BILL_AMT, DISC_AMT, ADD_DISC_AMT_MST
FROM IAS20261.IAS_BILL_MST 
WHERE CC_CODE='151' 
  AND BILL_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') 
  AND BILL_DATE < TO_DATE('2026-06-30','YYYY-MM-DD')+1
  AND (DISC_AMT > 0 OR ADD_DISC_AMT_MST > 0)
"""
cur.execute(sql)
print("CC 151 Bills:")
for row in cur.fetchall():
    print(row)
