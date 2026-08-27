import os
from dotenv import load_dotenv
import oracledb

load_dotenv(r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\db.env")
lib_dir = os.getenv("ORA_LIB_DIR", r"C:\oracle\instantclient\instantclient_23_0")
try:
    oracledb.init_oracle_client(lib_dir=lib_dir)
except Exception as e:
    pass

con = oracledb.connect(
    user=os.getenv("DB_USER", "RPT_USER"),
    password=os.getenv("DB_PASS", "ULT2016"),
    dsn=os.getenv("ORA_DSN", "100.100.1.100:1521/ORCL")
)

with con.cursor() as cur:
    cur.execute("""
        SELECT column_name 
        FROM all_tab_columns 
        WHERE table_name = 'IAS_BILL_MST' 
          AND (column_name LIKE '%DATE%' OR column_name LIKE '%DUE%' OR column_name LIKE '%PAY%')
    """)
    for r in cur.fetchall():
        print(r[0])
