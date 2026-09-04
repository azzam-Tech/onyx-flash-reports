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
        user="ULT",
        password="ULT2017",
        dsn="100.100.1.100:1521/ORCL"
    )

def describe_table(table_name):
    try:
        connection = get_conn()
        cursor = connection.cursor()
        
        cursor.execute(f"SELECT COLUMN_NAME, DATA_TYPE FROM DBA_TAB_COLUMNS WHERE TABLE_NAME = '{table_name}' ORDER BY COLUMN_ID")
        cols = cursor.fetchall()
        print(f"--- Table: {table_name} ---")
        for c in cols:
            print(f"{c[0]} ({c[1]})")
            
        cursor.execute(f"SELECT COUNT(*) FROM IAS20261.{table_name}")
        count = cursor.fetchone()[0]
        print(f"Row count: {count}\n")
            
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error describing {table_name}: {e}\n")

if __name__ == "__main__":
    describe_table('S_USR_HND_DVC')
    describe_table('S_EMP_HND_DVC')
    describe_table('S_APPROVL_APP_DVC')
