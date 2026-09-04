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

def list_tables_like(pattern):
    try:
        connection = get_conn()
        cursor = connection.cursor()
        
        cursor.execute("SELECT TABLE_NAME FROM DBA_TABLES WHERE OWNER = 'IAS20261' AND TABLE_NAME LIKE :1", [pattern])
        tables = [row[0] for row in cursor.fetchall()]
        print(f"Tables matching {pattern}:")
        for t in tables:
            print(t)
            
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_tables_like('%REG%')
    list_tables_like('%LICE%')
