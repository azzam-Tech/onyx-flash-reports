import os
import oracledb
import csv
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

        # Query all customers where C_CLASS_VAT = 1 (Personal)
        query = "SELECT * FROM IAS20261.CUSTOMER WHERE C_CLASS_VAT = 1"
        cursor.execute(query)
        rows = cursor.fetchall()
        
        # Get column names
        col_names = [d[0] for d in cursor.description]

        csv_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\Personal_Customers.csv'
        with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            # Write header
            writer.writerow(col_names)
            # Write all data rows
            for row in rows:
                writer.writerow(row)
                
        print(f"Exported {len(rows)} personal customers to: {csv_path}")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
