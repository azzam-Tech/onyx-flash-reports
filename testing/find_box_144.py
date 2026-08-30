import os
from dotenv import load_dotenv
import oracledb

load_dotenv(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer\db.env')
oracledb.init_oracle_client(lib_dir=os.getenv('ORA_LIB_DIR'))
conn = oracledb.connect(user=os.getenv('ORA_USER'), password=os.getenv('ORA_PASSWORD'), dsn=os.getenv('ORA_DSN'))
cursor = conn.cursor()

cursor.execute("""
    SELECT A_CODE, A_L_A_NAME FROM ACCOUNT WHERE A_L_A_NAME LIKE '%144%' OR A_L_A_NAME LIKE '%محمد سالم%'
""")
print('ACCOUNTS:', cursor.fetchall())
