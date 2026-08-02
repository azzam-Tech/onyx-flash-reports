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

def inspect_emp():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    print("=== S_EMP COLUMNS ===")
    cur.execute("SELECT COLUMN_NAME, DATA_TYPE FROM ALL_TAB_COLUMNS WHERE OWNER='IAS20261' AND TABLE_NAME='S_EMP' ORDER BY COLUMN_ID")
    for cols in cur.fetchall():
        print(f"  {cols[0]} ({cols[1]})")

    print("\n=== S_EMP_BNK COLUMNS ===")
    cur.execute("SELECT COLUMN_NAME, DATA_TYPE FROM ALL_TAB_COLUMNS WHERE OWNER='IAS20261' AND TABLE_NAME='S_EMP_BNK' ORDER BY COLUMN_ID")
    for cols in cur.fetchall():
        print(f"  {cols[0]} ({cols[1]})")

    print("\n=== Searching for GOSI / Insurance / Payroll / Salary tables in IAS20261 ===")
    cur.execute("SELECT TABLE_NAME FROM ALL_TABLES WHERE OWNER='IAS20261' ORDER BY TABLE_NAME")
    tables = [r[0] for r in cur.fetchall()]
    
    keywords = ['EMP', 'SAL', 'PAY', 'INS', 'GOSI', 'SOC', 'BANK', 'BNK', 'JOB', 'ATT']
    matching = [t for t in tables if any(k in t for k in keywords)]
    for m in matching:
        print(" Found Table:", m)

    conn.close()

if __name__ == "__main__":
    inspect_emp()
