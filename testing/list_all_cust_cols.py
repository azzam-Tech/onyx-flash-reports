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
    try:
        connection = get_conn()
        cursor = connection.cursor()

        query = """
            SELECT COLUMN_NAME
            FROM ALL_TAB_COLUMNS 
            WHERE TABLE_NAME = 'CUSTOMER' AND OWNER = 'IAS20261'
        """
        cursor.execute(query)
        columns = [c[0] for c in cursor.fetchall()]
        print(", ".join(columns))

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
