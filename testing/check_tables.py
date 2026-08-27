import os
import sys
from dotenv import load_dotenv
import oracledb

load_dotenv(r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\db.env")
lib_dir = os.getenv("ORA_LIB_DIR", r"C:\oracle\instantclient\instantclient_23_0")
try:
    oracledb.init_oracle_client(lib_dir=lib_dir)
except Exception as e:
    pass

def get_conn():
    return oracledb.connect(
        user=os.getenv("DB_USER", "RPT_USER"),
        password=os.getenv("DB_PASS", "ULT2016"),
        dsn=os.getenv("ORA_DSN", "100.100.1.100:1521/ORCL")
    )

with get_conn() as con:
    with con.cursor() as cur:
        # Check ACCOUNT table
        cur.execute("SELECT column_name FROM all_tab_columns WHERE table_name = 'ACCOUNT'")
        cols = [r[0] for r in cur.fetchall()]
        print("ACCOUNT Columns:", cols)
        
        # Check if EMP% tables exist
        cur.execute("SELECT table_name FROM all_tables WHERE owner='IAS20261' AND table_name LIKE 'EMP%'")
        tables = [r[0] for r in cur.fetchall()]
        print("EMP Tables:", tables)
