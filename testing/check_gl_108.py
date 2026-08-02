import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

sql = """
SELECT A_CODE, DR_AMT, CR_AMT, DOC_PST_SQ
FROM IAS20261.IAS_POST_DTL 
WHERE DOC_NO = 26315100108 AND DOC_TYPE = 4
"""
cur.execute(sql)
print("GL entries for invoice 26315100108:")
for row in cur.fetchall():
    print(row)
