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
    # Use RPT_USER for querying
    return oracledb.connect(
        user=os.getenv("DB_USER", "RPT_USER"),
        password=os.getenv("DB_PASS", "ULT2016"),
        dsn=os.getenv("ORA_DSN", "100.100.1.100:1521/ORCL")
    )

def main():
    try:
        connection = get_conn()
        cursor = connection.cursor()

        # Find columns in CUSTOMER table that might map to the 9 fields
        query = """
            SELECT COLUMN_NAME, DATA_TYPE 
            FROM ALL_TAB_COLUMNS 
            WHERE TABLE_NAME = 'CUSTOMER' AND OWNER = 'IAS20261'
        """
        cursor.execute(query)
        columns = cursor.fetchall()
        
        print("Columns in CUSTOMER:")
        for col in columns:
            name = col[0]
            # Print only columns that sound like address, tax, cr, building, street, etc.
            if any(k in name for k in ['TAX', 'VAT', 'CR', 'REG', 'BLD', 'BUILD', 'STREET', 'DIST', 'CITY', 'POST', 'ADD', 'ZIP', 'TEL', 'PHONE']):
                print(name)

        # Are there other customer tables?
        query2 = """
            SELECT TABLE_NAME 
            FROM ALL_TABLES 
            WHERE OWNER = 'IAS20261' AND TABLE_NAME LIKE 'CUST%'
        """
        cursor.execute(query2)
        tables = cursor.fetchall()
        print("\nOther Customer Tables:")
        for t in tables:
            print(t[0])

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
