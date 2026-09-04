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

def export_package(pkg_name, owner):
    try:
        connection = get_conn()
        cursor = connection.cursor()
        
        # Spec
        cursor.execute("SELECT TEXT FROM DBA_SOURCE WHERE OWNER = :1 AND NAME = :2 AND TYPE = 'PACKAGE' ORDER BY LINE", [owner, pkg_name])
        spec = "".join([row[0] for row in cursor.fetchall()])
        
        # Body
        cursor.execute("SELECT TEXT FROM DBA_SOURCE WHERE OWNER = :1 AND NAME = :2 AND TYPE = 'PACKAGE BODY' ORDER BY LINE", [owner, pkg_name])
        body = "".join([row[0] for row in cursor.fetchall()])
        
        if spec or body:
            with open(f"c:\\Users\\amarn\\OneDrive\\Desktop\\dbOnyxOnAntigravity\\testing\\{pkg_name}.sql", 'w', encoding='utf-8') as f:
                f.write(f"--- SPEC ---\n{spec}\n\n--- BODY ---\n{body}")
            print(f"Exported {pkg_name} successfully.")
        else:
            print(f"Package {pkg_name} not found.")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error exporting {pkg_name}: {e}")

if __name__ == "__main__":
    export_package("ARS_API_CHK_PKG", "IAS20261")
