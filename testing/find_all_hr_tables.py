import oracledb
import os

_lib = r"C:\oracle\instantclient\instantclient_23_0"
try:
    oracledb.init_oracle_client(lib_dir=_lib)
except Exception:
    pass

DB_USER     = os.environ.get("ORA_USER",     "RPT_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD", "ULT2016")
DB_DSN      = os.environ.get("ORA_DSN",      "100.100.1.100:1521/ORCL")

def find_populated_hr():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    cur.execute("""
        SELECT OWNER, TABLE_NAME 
        FROM ALL_TABLES 
        WHERE (TABLE_NAME LIKE '%EMP%' OR TABLE_NAME LIKE '%SAL%' OR TABLE_NAME LIKE '%PAY%' OR TABLE_NAME LIKE '%HR%' OR TABLE_NAME LIKE '%BANK%')
        ORDER BY OWNER, TABLE_NAME
    """)
    tables = cur.fetchall()
    print(f"Total candidate tables found across schemas: {len(tables)}")
    
    populated = []
    for owner, tname in tables:
        try:
            cur.execute(f"SELECT COUNT(*) FROM {owner}.{tname}")
            cnt = cur.fetchone()[0]
            if cnt > 0:
                populated.append((owner, tname, cnt))
        except Exception:
            pass

    print(f"\n--- Populated HR/Salary/Employee Tables ({len(populated)}) ---")
    for owner, tname, cnt in populated:
        print(f"  {owner}.{tname} -> {cnt} rows")

    conn.close()

if __name__ == "__main__":
    find_populated_hr()
