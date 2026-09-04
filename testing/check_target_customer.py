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
            req_no = '7897911'
            print(f"--- Searching for Target Customer Request {req_no} ---")
            
            try:
                # Check CUSTOMER_RQ table
                cur.execute(f"SELECT * FROM IAS20261.CUSTOMER_RQ WHERE C_CODE = '{req_no}' OR C_A_NAME LIKE '%عزام بشار%'")
                rows = cur.fetchall()
                if rows:
                    cols = [col[0] for col in cur.description]
                    for r in rows:
                        row_dict = dict(zip(cols, r))
                        print("FOUND IN CUSTOMER_RQ:")
                        for k, v in row_dict.items():
                            if v is not None:
                                print(f"  {k}: {v}")
                else:
                    print("Not found in CUSTOMER_RQ.")
            except Exception as e:
                print("Error querying CUSTOMER_RQ:", e)
                
            print("\n--- Checking Customer Group 146 ---")
            try:
                cur.execute("SELECT COUNT(*) FROM IAS20261.CUSTOMER WHERE G_TYPE = 146")
                count = cur.fetchone()[0]
                print(f"Total customers in Group 146: {count}")
                
                cur.execute("SELECT MAX(TO_NUMBER(C_CODE)) FROM IAS20261.CUSTOMER WHERE G_TYPE = 146")
                max_code = cur.fetchone()[0]
                print(f"Max C_CODE in Group 146: {max_code}")
                
                cur.execute("SELECT MAX(TO_NUMBER(C_CODE)) FROM IAS20261.CUSTOMER")
                max_global = cur.fetchone()[0]
                print(f"Max C_CODE globally: {max_global}")
            except Exception as e:
                print("Error checking CUSTOMER table:", e)

if __name__ == "__main__":
    main()
