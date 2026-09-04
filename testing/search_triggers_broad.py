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

        print("Searching for any triggers on IAS_BILL_MST...")
        # Check ALL_TRIGGERS for table_owner IAS20261
        query = """
            SELECT TRIGGER_NAME, TRIGGER_TYPE, TRIGGERING_EVENT, TABLE_OWNER
            FROM ALL_TRIGGERS 
            WHERE TABLE_NAME = 'IAS_BILL_MST'
        """
        cursor.execute(query)
        triggers = cursor.fetchall()
        
        for t in triggers:
            print(f"Found Trigger: {t}")

        print("Searching for any objects containing BILL in ALL_OBJECTS...")
        query2 = """
            SELECT OBJECT_NAME, OBJECT_TYPE, OWNER
            FROM ALL_OBJECTS
            WHERE OBJECT_NAME LIKE '%BILL%' AND OBJECT_TYPE = 'TRIGGER'
            AND ROWNUM <= 10
        """
        cursor.execute(query2)
        objs = cursor.fetchall()
        for o in objs:
            print(f"Found Object: {o}")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
