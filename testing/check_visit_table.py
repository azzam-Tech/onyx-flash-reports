import oracledb
import json

def check_table():
    try:
        connection = oracledb.connect(
            user="RPT_USER", 
            password="ULT2016", 
            dsn="100.100.1.100:1521/ORCL"
        )
        
        cursor = connection.cursor()
        
        # Get sample row from DTS_CST_VST_MST
        cursor.execute("""
            SELECT *
            FROM IAS20261.DTS_CST_VST_MST
            WHERE ROWNUM <= 1
            ORDER BY VST_DATE DESC
        """)
        
        row = cursor.fetchone()
        if row:
            columns = [col[0] for col in cursor.description]
            print("Sample row:")
            for col, val in zip(columns, row):
                print(f"- {col}: {val}")
        else:
            print("No rows found in DTS_CST_VST_MST")
            
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient\instantclient_23_0")
    check_table()
