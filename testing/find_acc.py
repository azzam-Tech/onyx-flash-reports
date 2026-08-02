import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

cur.execute("SELECT TABLE_NAME FROM ALL_TABLES WHERE OWNER='IAS20261' AND TABLE_NAME LIKE '%ACC%'")
tables = cur.fetchall()
for t in tables:
    print(t[0])
