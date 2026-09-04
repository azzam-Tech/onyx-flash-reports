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
        user="ULT", # Changed from RPT_USER to main DBA user
        password=os.getenv("DB_PASS", "ULT2016"),
        dsn=os.getenv("ORA_DSN", "100.100.1.100:1521/ORCL")
    )

def main():
    with get_conn() as con:
        with con.cursor() as cur:
            try:
                sql = """
                    INSERT INTO IAS20261.CUSTOMER (
                        C_CODE, C_A_NAME, C_A_CODE, REP_CODE, C_CLASS, C_GROUP_CODE, AUTO_APPRVD
                    ) VALUES (
                        '2999', 'DUMMY_SPOOF', '113010146', '146', '146', '146', 0
                    )
                """
                cur.execute(sql)
                con.commit()
                print("SUCCESS: Dummy customer 2999 inserted.")
            except Exception as e:
                print("ERROR:", e)

if __name__ == "__main__":
    main()
