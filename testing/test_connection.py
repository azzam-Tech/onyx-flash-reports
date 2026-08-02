import os
import oracledb

DB_USER = os.environ.get("ORA_USER", "RPT_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD", "ULT2016")
DB_DSN = os.environ.get("ORA_DSN", "100.100.1.100:1521/ORCL")
_lib = r"C:\oracle\instantclient\instantclient_23_0"

print(f"Connecting to {DB_DSN} as {DB_USER} using Thick mode at {_lib} ...")

try:
    oracledb.init_oracle_client(lib_dir=_lib)
    print("Thick mode initialized.")
except Exception as e:
    print("Thick mode init error:", e)

try:
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    print("Connection successful!")
    
    with conn.cursor() as cur:
        cur.execute("SELECT C_CODE, C_A_NAME FROM IAS20261.CUSTOMER FETCH FIRST 5 ROWS ONLY")
        rows = cur.fetchall()
        print(f"\nFetched {len(rows)} customers:")
        for row in rows:
            print(f"- Code: {row[0]}, Name: {row[1]}")
            
except Exception as e:
    print("Connection/Query failed:", e)
