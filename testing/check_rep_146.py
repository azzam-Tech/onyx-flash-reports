import oracledb
import os
from dotenv import load_dotenv

load_dotenv()
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

cur = con.cursor()

print("Query 1: By Customer linked to salesman 146")
cur.execute("""
    SELECT m.BILL_NO, m.BILL_DATE, m.AD_DATE
    FROM IAS20261.IAS_BILL_MST m
    WHERE m.C_CODE IN (
        SELECT C_CODE FROM IAS20261.CUSTOMER WHERE TRIM(REP_CODE) = '146'
    )
    ORDER BY m.BILL_DATE DESC, m.AD_DATE DESC
    FETCH FIRST 1 ROWS ONLY
""")
print(cur.fetchone())

print("\nQuery 2: By REP_CODE directly on the invoice (if it exists)")
try:
    cur.execute("""
        SELECT BILL_NO, BILL_DATE, AD_DATE 
        FROM IAS20261.IAS_BILL_MST 
        WHERE TRIM(REP_CODE) = '146' 
        ORDER BY BILL_DATE DESC, AD_DATE DESC 
        FETCH FIRST 1 ROWS ONLY
    """)
    print(cur.fetchone())
except Exception as e:
    print(e)
