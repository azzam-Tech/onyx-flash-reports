import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

sql2 = f"""
SELECT DOC_NO, DOC_DATE, CR_AMT, DR_AMT, CC_CODE
FROM IAS20261.IAS_POST_DTL 
WHERE DOC_TYPE = 15 
  AND CC_CODE = '151'
  AND DOC_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD')
"""
cur.execute(sql2)
print("Discount Notices for CC 151:")
for row in cur.fetchall():
    print(row)
