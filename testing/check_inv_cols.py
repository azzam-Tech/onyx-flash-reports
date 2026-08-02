import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

sql2 = """
SELECT *
FROM IAS20261.IAS_BILL_DTL
WHERE BILL_NO = 26315100108 AND BILL_DOC_TYPE = 4
"""
cur.execute(sql2)
columns = [col[0] for col in cur.description]
print("Columns:", columns)
print("Details:", cur.fetchall())
