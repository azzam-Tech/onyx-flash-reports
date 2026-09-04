import os
import oracledb
from dotenv import load_dotenv

load_dotenv('db.env')
lib_dir = os.getenv("ORA_LIB_DIR", r"C:\oracle\instantclient\instantclient_23_0")
try:
    oracledb.init_oracle_client(lib_dir=lib_dir)
except Exception:
    pass

os.environ["NLS_LANG"] = "ARABIC_SAUDI ARABIA.AL32UTF8"

def get_conn():
    return oracledb.connect(
        user=os.getenv("DB_USER", "RPT_USER"),
        password=os.getenv("DB_PASS", "ULT2016"),
        dsn=os.getenv("ORA_DSN", "100.100.1.100:1521/ORCL")
    )

def main():
    try:
        connection = get_conn()
        cursor = connection.cursor()

        query = """
            SELECT C_CODE, C_A_NAME, C_TAX_CODE, COMM_REG_NO, CR_NO, BUILDING_NO, STREET, DSTRCT_NM, EXTERNAL_POST, ADD_NO, CITY_NO, C_BOX, C_BOX_CODE, SHRT_ADD
            FROM IAS20261.CUSTOMER 
            WHERE C_CODE = '2306'
        """
        cursor.execute(query)
        row = cursor.fetchone()
        
        if not row:
            print("Customer 2306 not found.")
            return

        cols = [d[0] for d in cursor.description]
        print("--- Customer 2306 Data ---")
        for k, v in zip(cols, row):
            print(f"{k}: '{v}' (Type: {type(v).__name__})")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
