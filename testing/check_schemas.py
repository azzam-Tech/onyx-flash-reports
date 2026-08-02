import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

try:
    cur.execute("SELECT COUNT(*) FROM IAS20251.IAS_BILL_MST")
    print("IAS20251 exists! Count:", cur.fetchone()[0])
except Exception as e:
    print("IAS20251 error:", e)

try:
    cur.execute("SELECT COUNT(*) FROM IAS20241.IAS_BILL_MST")
    print("IAS20241 exists! Count:", cur.fetchone()[0])
except Exception as e:
    print("IAS20241 error:", e)

try:
    cur.execute("SELECT USERNAME FROM ALL_USERS WHERE USERNAME LIKE 'IAS%'")
    print("All IAS users:", cur.fetchall())
except Exception as e:
    print("Users error:", e)
