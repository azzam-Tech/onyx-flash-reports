import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

sql = """
SELECT A_CODE, DR_AMT, CR_AMT 
FROM IAS20261.IAS_POST_DTL
WHERE DOC_NO = 2621510008 AND DOC_TYPE = 15
"""
cur.execute(sql)
print("Entries for Discount Notice 2621510008:")
for row in cur.fetchall():
    print(row)
