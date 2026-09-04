import os
import oracledb
from dotenv import load_dotenv

load_dotenv('db.env')
lib_dir = os.getenv("ORA_LIB_DIR", r"C:\oracle\instantclient\instantclient_23_0")
try:
    oracledb.init_oracle_client(lib_dir=lib_dir)
except Exception:
    pass

def get_conn():
    return oracledb.connect(
        user=os.getenv("DB_USER", "RPT_USER"),
        password=os.getenv("DB_PASS", "ULT2016"),
        dsn=os.getenv("ORA_DSN", "100.100.1.100:1521/ORCL")
    )

def main():
    with get_conn() as con:
        with con.cursor() as cur:
            try:
                cur.execute("SELECT * FROM IAS20261.CUSTOMER_GROUP WHERE ROWNUM <= 10")
                rows = cur.fetchall()
                print("--- CUSTOMER_GROUP ---")
                for r in rows:
                    print(r)
            except Exception as e:
                print("Error CUSTOMER_GROUP:", e)

            try:
                cur.execute("SELECT * FROM IAS20261.CUSTOMER_CLASS WHERE ROWNUM <= 10")
                rows = cur.fetchall()
                print("\n--- CUSTOMER_CLASS ---")
                for r in rows:
                    print(r)
            except Exception as e:
                print("Error CUSTOMER_CLASS:", e)

if __name__ == "__main__":
    main()
