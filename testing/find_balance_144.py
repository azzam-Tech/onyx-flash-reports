import os
from dotenv import load_dotenv
import oracledb

load_dotenv(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer\db.env')
oracledb.init_oracle_client(lib_dir=os.getenv('ORA_LIB_DIR'))
conn = oracledb.connect(user=os.getenv('ORA_USER'), password=os.getenv('ORA_PASSWORD'), dsn=os.getenv('ORA_DSN'))
cursor = conn.cursor()

cursor.execute("SELECT A_CODE, A_NAME, A_NAME_ENG FROM IAS20261.ACCOUNT WHERE A_NAME LIKE '%144%' OR A_NAME LIKE '%محمد سالم%' OR A_CODE LIKE '%144%'")
accounts = cursor.fetchall()
for acc in accounts:
    print('ACC:', acc)

# Get the balance for this account
for acc in accounts:
    acode = acc[0]
    cursor.execute("""
        SELECT SUM(NVL(DR_AMT,0)) - SUM(NVL(CR_AMT,0)) as BALANCE
        FROM IAS_POST_DTL
        WHERE A_CODE = :acode AND NVL(DOC_POST,0) = 1
    """, {'acode': acode})
    bal = cursor.fetchone()[0]
    print(f'BALANCE for {acode} ({acc[1]}): {bal}')
