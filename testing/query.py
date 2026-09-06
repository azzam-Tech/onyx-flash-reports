import oracledb
oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
con = oracledb.connect('ULT/ULT2017@100.100.1.100:1521/ORCL')
cur = con.cursor()
cur.execute("SELECT TABLE_NAME FROM ALL_TABLES WHERE OWNER='IAS20261' AND (TABLE_NAME LIKE '%VISIT%' OR TABLE_NAME LIKE '%VST%' OR TABLE_NAME LIKE '%PLAN%' OR TABLE_NAME LIKE '%TRIP%')")
for row in cur.fetchall():
    print(row[0])
con.close()
