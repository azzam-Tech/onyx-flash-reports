import os
import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(
    user=os.environ.get('ORA_USER', 'RPT_USER'),
    password=os.environ.get('ORA_PASSWORD', 'ULT2016'),
    dsn=os.environ.get('ORA_DSN', '100.100.1.100:1521/ORCL')
)
cur = conn.cursor()

tables = ['IAS_PR_BILL_MST', 'ITEM_MOVEMENT', 'IAS_POST_MST', 'IAS_POST_DTL', 'GNR_TAX_ITM_MOVMNT']
for t in tables:
    cur.execute(f"SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME='{t}' AND OWNER='IAS20261' AND COLUMN_NAME LIKE '%DATE%'")
    print(t, [r[0] for r in cur.fetchall()])

cur.close()
conn.close()
