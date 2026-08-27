import os
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

rep_code = '144'
date_from = '2026-01-01'
date_to = '2026-12-31'

sql_app = """
        WITH sales_base AS (
            SELECT SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as sales
            FROM IAS20261.IAS_BILL_MST
            WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
              AND BILL_DATE <= TO_DATE(:date_to,'YYYY-MM-DD')
              AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
              AND TO_CHAR(CC_CODE) = TRIM(:rep_code)
        ),
        returns_base AS (
            SELECT SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as returns
            FROM IAS20261.IAS_RT_BILL_MST
            WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
              AND RT_BILL_DATE <= TO_DATE(:date_to,'YYYY-MM-DD')
              AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
              AND TO_CHAR(CC_CODE) = TRIM(:rep_code)
        )
        SELECT 
          NVL((SELECT NVL(sales, 0) FROM sales_base), 0) - NVL((SELECT NVL(returns, 0) FROM returns_base), 0) as net_sales
        FROM DUAL
"""

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute(sql_app, {'date_from': date_from, 'date_to': date_to, 'rep_code': rep_code})
        row = cur.fetchone()
        print("APP LOGIC SALES:", row[0])
