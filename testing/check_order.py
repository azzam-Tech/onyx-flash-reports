import os
import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(
    user=os.environ.get('ORA_USER', 'RPT_USER'),
    password=os.environ.get('ORA_PASSWORD', 'ULT2016'),
    dsn=os.environ.get('ORA_DSN', '100.100.1.100:1521/ORCL')
)
cur = conn.cursor()

cur.execute('''
    SELECT I_DATE, DOC_TYPE, DOC_NO, IN_OUT, I_QTY, SERIAL, AD_DATE 
    FROM IAS20261.ITEM_MOVEMENT 
    WHERE I_CODE = 'OS32ATVHD' AND W_CODE = 131 
    ORDER BY SERIAL DESC
    FETCH FIRST 5 ROWS ONLY
''')
rows = cur.fetchall()
for r in rows:
    print(r)

cur.close()
conn.close()
