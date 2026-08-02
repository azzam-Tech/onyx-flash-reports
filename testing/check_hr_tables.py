import oracledb
import os

_lib = r"C:\oracle\instantclient\instantclient_23_0"
try:
    oracledb.init_oracle_client(lib_dir=_lib)
except Exception as e:
    pass

DB_USER     = os.environ.get("ORA_USER",     "RPT_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD", "ULT2016")
DB_DSN      = os.environ.get("ORA_DSN",      "100.100.1.100:1521/ORCL")

def check_hr():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()
    
    keywords = ['EMP', 'SAL', 'PAY', 'BANK', 'INS', 'GOSI', 'HR', 'ALLOW', 'DED', 'SOC']
    
    print("--- Searching All Tables in Oracle DB ---")
    sql = """
        SELECT OWNER, TABLE_NAME 
        FROM ALL_TABLES 
        WHERE OWNER LIKE 'IAS%'
        ORDER BY TABLE_NAME
    """
    cur.execute(sql)
    all_tables = cur.fetchall()
    
    hr_tables = []
    for owner, tname in all_tables:
        for kw in keywords:
            if kw in tname:
                hr_tables.append((owner, tname))
                break
                
    print(f"Total tables found matching HR keywords: {len(hr_tables)}")
    for owner, tname in hr_tables:
        print(f" - {owner}.{tname}")

    conn.close()

if __name__ == "__main__":
    check_hr()
