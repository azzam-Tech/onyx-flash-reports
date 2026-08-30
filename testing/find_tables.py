import os
from dotenv import load_dotenv
import oracledb

load_dotenv(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer\db.env')
oracledb.init_oracle_client(lib_dir=os.getenv('ORA_LIB_DIR'))
conn = oracledb.connect(user=os.getenv('ORA_USER'), password=os.getenv('ORA_PASSWORD'), dsn=os.getenv('ORA_DSN'))
cursor = conn.cursor()

cursor.execute("""
    SELECT TABLE_NAME FROM ALL_TABLES WHERE TABLE_NAME LIKE '%ACC%' FETCH FIRST 20 ROWS ONLY
""")
print('Tables with ACC:', [r[0] for r in cursor.fetchall()])

cursor.execute("""
    SELECT TABLE_NAME FROM ALL_TABLES WHERE TABLE_NAME LIKE '%BOX%' FETCH FIRST 20 ROWS ONLY
""")
print('Tables with BOX:', [r[0] for r in cursor.fetchall()])
