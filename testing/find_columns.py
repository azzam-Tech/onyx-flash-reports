import os
from dotenv import load_dotenv
import oracledb

load_dotenv(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer\db.env')
oracledb.init_oracle_client(lib_dir=os.getenv('ORA_LIB_DIR'))
conn = oracledb.connect(user=os.getenv('ORA_USER'), password=os.getenv('ORA_PASSWORD'), dsn=os.getenv('ORA_DSN'))
cursor = conn.cursor()

cursor.execute("""
    SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = 'ACCOUNT'
""")
print('ACCOUNT Columns:', [r[0] for r in cursor.fetchall()])
