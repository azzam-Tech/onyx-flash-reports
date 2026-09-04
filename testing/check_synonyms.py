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

        # How does RPT_USER see IAS_BILL_MST? Is there a synonym?
        print("Checking synonyms for IAS_BILL_MST...")
        query_synonym = """
            SELECT TABLE_OWNER, TABLE_NAME 
            FROM ALL_SYNONYMS 
            WHERE SYNONYM_NAME = 'IAS_BILL_MST'
        """
        cursor.execute(query_synonym)
        syns = cursor.fetchall()
        for s in syns:
            print(f"Synonym points to Owner: {s[0]}, Table: {s[1]}")
            owner = s[0]
            table = s[1]
            
            print(f"\nChecking triggers on {owner}.{table}...")
            query_triggers = """
                SELECT TRIGGER_NAME, TRIGGER_TYPE, TRIGGERING_EVENT
                FROM ALL_TRIGGERS 
                WHERE TABLE_OWNER = :owner AND TABLE_NAME = :table_name
            """
            cursor.execute(query_triggers, [owner, table])
            triggers = cursor.fetchall()
            if not triggers:
                print("No triggers found.")
            else:
                for t in triggers:
                    print(f"Trigger: {t}")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
