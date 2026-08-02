import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

sql2 = """
SELECT I_CODE, I_QTY, I_PRICE, DIS_AMT, DIS_AMT_MST
FROM IAS20261.IAS_BILL_DTL
WHERE BILL_NO = 26315100150 AND BILL_DOC_TYPE = 4
"""
cur.execute(sql2)
print("Details 26315100150:", cur.fetchall())
