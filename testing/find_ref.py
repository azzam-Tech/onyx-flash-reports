import os
import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(
    user=os.environ.get('ORA_USER', 'RPT_USER'),
    password=os.environ.get('ORA_PASSWORD', 'ULT2016'),
    dsn=os.environ.get('ORA_DSN', '100.100.1.100:1521/ORCL')
)
cur = conn.cursor()

cur.execute("SELECT TABLE_NAME, COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE OWNER='IAS20261' AND DATA_TYPE='VARCHAR2' AND COLUMN_NAME LIKE '%REF%'")
cols = cur.fetchall()

found_tables = []
for tab, col in cols:
    try:
        cur.execute(f"SELECT COUNT(*) FROM IAS20261.{tab} WHERE {col} = '900002332'")
        if cur.fetchone()[0] > 0:
            found_tables.append((tab, col))
            print(f"FOUND IN {tab}.{col}")
    except:
        pass

print("Done scanning.", found_tables)
cur.close()
conn.close()
