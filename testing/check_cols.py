import os
import sys

os.environ["NLS_LANG"] = ".AL32UTF8"
sys.stdout.reconfigure(encoding='utf-8')

import oracledb

_lib = r"C:\oracle\instantclient\instantclient_23_0"
try:
    oracledb.init_oracle_client(lib_dir=_lib)
except Exception:
    pass

DB_USER     = os.environ.get("ORA_USER",     "RPT_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD", "ULT2016")
DB_DSN      = os.environ.get("ORA_DSN",      "100.100.1.100:1521/ORCL")

def main():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()
    
    cur.execute("SELECT column_name FROM all_tab_cols WHERE table_name = 'ITEM_MOVEMENT' AND column_name LIKE '%COST%'")
    print("ITEM_MOVEMENT cost cols:", [r[0] for r in cur.fetchall()])
    
    cur.execute("SELECT column_name FROM all_tab_cols WHERE table_name = 'IAS_BILL_DTL' AND column_name LIKE '%COST%'")
    print("IAS_BILL_DTL cost cols:", [r[0] for r in cur.fetchall()])

if __name__ == '__main__':
    main()
