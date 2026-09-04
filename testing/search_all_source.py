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

        # Let's search ALL_SOURCE for IAS_BILL_MST to see if there are stored procedures
        query = """
            SELECT DISTINCT NAME, TYPE, OWNER
            FROM ALL_SOURCE 
            WHERE UPPER(TEXT) LIKE '%IAS_BILL_MST%'
            AND TYPE IN ('PROCEDURE', 'PACKAGE', 'PACKAGE BODY', 'TRIGGER')
            AND ROWNUM <= 20
        """
        
        cursor.execute(query)
        sources = cursor.fetchall()

        if not sources:
            print("No sources found referencing IAS_BILL_MST.")
        else:
            print("Found sources referencing IAS_BILL_MST:")
            for row in sources:
                print(f"Name: {row[0]}, Type: {row[1]}, Owner: {row[2]}")
                
        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
