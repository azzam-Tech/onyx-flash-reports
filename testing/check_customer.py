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
cur.execute("""
    SELECT 
        m.BILL_NO, 
        c.C_A_NAME,
        ci.CITY_A_NAME,
        co.CNTRY_A_NAME
    FROM IAS20261.IAS_BILL_MST m
    LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = m.C_CODE
    LEFT JOIN IAS20261.CITIES ci ON c.CITY_NO = ci.CITY_NO AND c.CNTRY_NO = ci.CNTRY_NO AND c.PROV_NO = ci.PROV_NO
    LEFT JOIN IAS20261.CNTRY co ON c.CNTRY_NO = co.CNTRY_NO
    ORDER BY m.BILL_DATE DESC
    FETCH FIRST 5 ROWS ONLY
""")
for row in cur.fetchall():
    print(row)
