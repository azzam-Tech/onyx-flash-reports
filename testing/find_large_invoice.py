import os
import sys
import oracledb
from dotenv import load_dotenv

load_dotenv()

# Oracle Thick mode init
ORACLE_CLIENT_PATH = r"C:\oracle\instantclient\instantclient_23_0"
try:
    oracledb.init_oracle_client(lib_dir=ORACLE_CLIENT_PATH)
except Exception as e:
    pass

DB_USER = os.getenv("DB_USER", "RPT_USER")
DB_PASS = os.getenv("DB_PASS", "ULT2016")
DB_HOST = os.getenv("DB_HOST", "100.100.1.100")
DB_PORT = os.getenv("DB_PORT", "1521")
DB_NAME = os.getenv("DB_SERVICE_NAME", "ORCL")

dsn = f"{DB_HOST}:{DB_PORT}/{DB_NAME}"

try:
    conn = oracledb.connect(user=DB_USER, password=DB_PASS, dsn=dsn)
    cursor = conn.cursor()
    
    # Query to find bills with maximum item count in IAS_BILL_DTL
    query = """
    SELECT 
        d.BILL_NO,
        COUNT(*) as ITEM_COUNT,
        m.BILL_DATE,
        c.C_A_NAME,
        m.BILL_AMT
    FROM IAS20261.IAS_BILL_DTL d
    JOIN IAS20261.IAS_BILL_MST m 
      ON d.BILL_DOC_TYPE = m.BILL_DOC_TYPE 
     AND d.BILL_NO = m.BILL_NO 
     AND d.BILL_SER = m.BILL_SER
    LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = m.C_CODE
    GROUP BY d.BILL_NO, m.BILL_DATE, c.C_A_NAME, m.BILL_AMT
    HAVING COUNT(*) BETWEEN 10 AND 18
    ORDER BY COUNT(*) DESC
    FETCH FIRST 10 ROWS ONLY
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    print("--- Large Invoices Found ---")
    for r in rows:
        print(f"Bill No: {r[0]} | Items: {r[1]} | Date: {r[2]} | Total: {r[4]} | Customer: {r[3]}")
        
    cursor.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")
