import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

sql = "SELECT BILL_NO, DISC_AMT, DISC_AMT_MST, DISC_AMT_DTL, ADD_DISC_AMT_MST, ADD_DISC_AMT_DTL FROM IAS20261.IAS_BILL_MST WHERE BILL_NO = 26315100150 AND BILL_DOC_TYPE = 4"
cur.execute(sql)
print("Invoice 150:", cur.fetchone())

sql2 = "SELECT SUM(DISC_AMT), SUM(DISC_AMT_MST), SUM(DISC_AMT_DTL), SUM(ADD_DISC_AMT_MST) FROM IAS20261.IAS_BILL_MST WHERE BILL_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') AND BILL_DATE < TO_DATE('2026-06-30','YYYY-MM-DD')+1"
cur.execute(sql2)
print("Totals:", cur.fetchone())
