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
            # max for REP_CODE 146 is 2388. Next is 2389.
            # max for C_CLASS 146 is 2379. Next is 2380.
            cur.execute("SELECT C_CODE, C_A_NAME FROM IAS20261.CUSTOMER WHERE C_CODE IN ('2389', '2380')")
            rows = cur.fetchall()
            print("--- Checking for 2389 and 2380 in CUSTOMER ---")
            for r in rows:
                print(r)
                
            # Check what is the absolute MAX C_CODE
            cur.execute("SELECT MAX(TO_NUMBER(C_CODE)) FROM IAS20261.CUSTOMER WHERE REGEXP_LIKE(C_CODE, '^[0-9]+$')")
            max_code = cur.fetchone()[0]
            print(f"Max C_CODE is {max_code}")

if __name__ == "__main__":
    main()
