import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

sql = """
SELECT BILL_NO, BILL_DOC_TYPE, CC_CODE, DISC_AMT, DISC_AMT_MST, ADD_DISC_AMT_MST, 
       VAT_AMT, CPN_AMT, OTHR_AMT, NET_AMT
FROM (
  SELECT BILL_NO, BILL_DOC_TYPE, CC_CODE, DISC_AMT, DISC_AMT_MST, ADD_DISC_AMT_MST, VAT_AMT, CPN_AMT, OTHR_AMT, 0 as NET_AMT
  FROM IAS20261.IAS_BILL_MST 
  WHERE BILL_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') 
    AND BILL_DATE < TO_DATE('2026-06-30','YYYY-MM-DD')+1
    AND DISC_AMT > 0 AND NVL(DISC_AMT_MST,0) = 0
)
FETCH FIRST 10 ROWS ONLY
"""
cur.execute(sql)
print("Invoices with DISC_AMT > 0 but DISC_AMT_MST = 0:")
for row in cur.fetchall():
    print(row)
