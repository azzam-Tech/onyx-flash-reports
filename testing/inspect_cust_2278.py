import os
import oracledb
import json
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

        # Fetch customer 2278 and see all columns that have value 1 or 2
        query = """
            SELECT * FROM IAS20261.CUSTOMER WHERE C_CODE = '2278'
        """
        cursor.execute(query)
        row = cursor.fetchone()
        
        if not row:
            print("Customer 2278 not found.")
            return

        col_names = [d[0] for d in cursor.description]
        
        print("Columns for customer 2278:")
        for name, val in zip(col_names, row):
            # Print columns that might represent the Tax Type (often small integers)
            if val in (1, 2, '1', '2') or 'TAX' in name or 'VAT' in name or 'TYP' in name:
                print(f"{name}: {val}")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
