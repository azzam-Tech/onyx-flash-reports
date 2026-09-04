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

def get_triggers():
    try:
        connection = get_conn()
        cursor = connection.cursor()

        query = """
            SELECT TRIGGER_NAME, TRIGGER_TYPE, TRIGGERING_EVENT, OWNER
            FROM ALL_TRIGGERS 
            WHERE TABLE_NAME = 'IAS_BILL_MST'
        """
        
        cursor.execute(query)
        triggers = cursor.fetchall()

        if not triggers:
            print("No triggers found on IAS_BILL_MST.")
        else:
            print("Found Triggers on IAS_BILL_MST:")
            for row in triggers:
                print(f"Trigger Name: {row[0]}, Type: {row[1]}, Event: {row[2]}, Owner: {row[3]}")
                
                source_query = """
                    SELECT TEXT 
                    FROM ALL_SOURCE 
                    WHERE NAME = :trigger_name AND TYPE = 'TRIGGER' AND OWNER = :owner
                    ORDER BY LINE
                """
                cursor.execute(source_query, [row[0], row[3]])
                source_lines = cursor.fetchall()
                if source_lines:
                    print("--- Trigger Source Snippet ---")
                    for line in source_lines[:15]:
                        print(line[0].strip())
                    if len(source_lines) > 15:
                        print("... (truncated)")
                    print("------------------------------\n")
                
        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_triggers()
