import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

sql = """
SELECT BILL_AMT, DISC_AMT, ADD_DISC_AMT_MST
FROM IAS20261.IAS_BILL_MST 
WHERE BILL_NO = 26315100108 AND BILL_DOC_TYPE = 4
"""
cur.execute(sql)
print("Invoice 26315100108:", cur.fetchone())

sql2 = """
SELECT NVL(SUM(T_AMT), 0)
FROM IAS20261.IAS_BILL_DTL
WHERE BILL_NO = 26315100108 AND BILL_DOC_TYPE = 4
"""
cur.execute(sql2)
print("Invoice 26315100108 Details Sum:", cur.fetchone())
