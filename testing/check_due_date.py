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
        SELECT BILL_NO, TO_CHAR(BILL_DATE, 'DD/MM/YYYY'), TO_CHAR(BILL_DUE_DATE, 'DD/MM/YYYY')
        FROM IAS20261.IAS_BILL_MST 
        WHERE BILL_DOC_TYPE = 2
        AND BILL_DATE != NVL(BILL_DUE_DATE, BILL_DATE)
        FETCH FIRST 5 ROWS ONLY
    """)
    rows = cur.fetchall()
    print("Invoices with different due date:")
    for r in rows:
        print(r)
        
    cur.execute("""
        SELECT BILL_NO, TO_CHAR(BILL_DATE, 'DD/MM/YYYY'), TO_CHAR(BILL_DUE_DATE, 'DD/MM/YYYY')
        FROM IAS20261.IAS_BILL_MST 
        WHERE BILL_NO = '26315500254'
    """)
    print("Specific invoice 26315500254:", cur.fetchone())
