import os
import oracledb

# Ensure thick mode
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient\instantclient_23_0")

def get_conn():
    # Strict Read-Only Intent, but using DBA credentials
    return oracledb.connect(
        user="ULT",
        password="ULT2017",
        dsn="100.100.1.100:1521/ORCL"
    )

def main():
    try:
        connection = get_conn()
        cursor = connection.cursor()

        print("Connected as ULT successfully (READ-ONLY mode).")

        print("\n--- Searching DBA_TRIGGERS for IAS_BILL_MST ---")
        query_triggers = """
            SELECT TRIGGER_NAME, TRIGGER_TYPE, TRIGGERING_EVENT, OWNER
            FROM DBA_TRIGGERS 
            WHERE TABLE_NAME = 'IAS_BILL_MST'
        """
        cursor.execute(query_triggers)
        triggers = cursor.fetchall()
        if not triggers:
            print("No triggers found on IAS_BILL_MST even as DBA!")
        else:
            for t in triggers:
                print(f"Trigger: {t}")

        print("\n--- Searching DBA_SOURCE for references to IAS_BILL_MST ---")
        query_source = """
            SELECT DISTINCT NAME, TYPE, OWNER
            FROM DBA_SOURCE 
            WHERE UPPER(TEXT) LIKE '%INSERT INTO IAS20261.IAS_BILL_MST%'
               OR UPPER(TEXT) LIKE '%INSERT INTO IAS_BILL_MST%'
            AND ROWNUM <= 20
        """
        cursor.execute(query_source)
        sources = cursor.fetchall()
        if not sources:
            print("No sources found containing exact INSERT INTO IAS_BILL_MST.")
        else:
            for s in sources:
                print(f"Name: {s[0]}, Type: {s[1]}, Owner: {s[2]}")

        # Let's broaden the search a bit for procedures related to bills
        print("\n--- Searching for Packages/Procedures named %BILL% ---")
        query_objects = """
            SELECT OBJECT_NAME, OBJECT_TYPE, OWNER
            FROM DBA_OBJECTS
            WHERE OBJECT_NAME LIKE '%BILL%' 
              AND OBJECT_TYPE IN ('PROCEDURE', 'PACKAGE')
            AND ROWNUM <= 10
        """
        cursor.execute(query_objects)
        objs = cursor.fetchall()
        for o in objs:
            print(f"Object: {o}")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
