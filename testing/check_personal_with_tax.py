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

        # Query personal customers (C_CLASS_VAT = 1) who have a Tax Number registered
        query = """
            SELECT C_CODE, C_A_NAME, C_TAX_CODE 
            FROM IAS20261.CUSTOMER 
            WHERE C_CLASS_VAT = 1 
              AND C_TAX_CODE IS NOT NULL 
              AND TRIM(C_TAX_CODE) != ''
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        
        if not rows:
            print("لا يوجد أي عميل شخصي لديه رقم ضريبي مسجل.")
        else:
            print(f"يوجد {len(rows)} عميل شخصي لديهم رقم ضريبي مسجل، وهم:")
            for row in rows:
                print(f"رقم العميل: {row[0]} | الاسم: {row[1]} | الرقم الضريبي: {row[2]}")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
