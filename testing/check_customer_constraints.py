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
            cur.execute("""
                SELECT COLUMN_NAME, DATA_TYPE, DATA_DEFAULT 
                FROM ALL_TAB_COLUMNS 
                WHERE OWNER = 'IAS20261' AND TABLE_NAME = 'CUSTOMER' 
                  AND NULLABLE = 'N'
            """)
            cols = cur.fetchall()
            print("--- NOT NULL COLUMNS IN CUSTOMER ---")
            for c in cols:
                print(c)
                
            # Let's get one real customer for Salesman 146 to copy their data
            cur.execute("SELECT * FROM IAS20261.CUSTOMER WHERE REP_CODE = '146' AND ROWNUM = 1")
            row = cur.fetchone()
            if row:
                col_names = [col[0] for col in cur.description]
                row_dict = dict(zip(col_names, row))
                print("\n--- SAMPLE CUSTOMER FOR 146 ---")
                for k, v in row_dict.items():
                    if v is not None:
                        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
