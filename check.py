import oracledb
oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
con = oracledb.connect(user='RPT_USER', password='ULT2016', dsn='100.100.1.100:1521/ORCL')
cur = con.cursor()
cur.execute("SELECT column_name FROM all_tab_columns WHERE table_name = 'CUSTOMER' AND owner = 'IAS20261'")
print([r[0] for r in cur.fetchall()])
