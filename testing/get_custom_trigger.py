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

        query_source = """
            SELECT TEXT 
            FROM DBA_SOURCE 
            WHERE NAME = 'TRG_PREVENT_SUSPENDED_SALES' AND TYPE = 'TRIGGER'
            ORDER BY LINE
        """
        cursor.execute(query_source)
        sources = cursor.fetchall()
        
        if not sources:
            print("Could not find the source for TRG_PREVENT_SUSPENDED_SALES.")
        else:
            print("--- Source Code for TRG_PREVENT_SUSPENDED_SALES ---")
            for line in sources:
                print(line[0].rstrip("\n"))
            print("---------------------------------------------------")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
