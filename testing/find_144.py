import os
from dotenv import load_dotenv
import oracledb

load_dotenv(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer\db.env')
oracledb.init_oracle_client(lib_dir=os.getenv('ORA_LIB_DIR'))
conn = oracledb.connect(user=os.getenv('ORA_USER'), password=os.getenv('ORA_PASSWORD'), dsn=os.getenv('ORA_DSN'))
cursor = conn.cursor()

# Find the account for 144
cursor.execute("SELECT A_CODE, A_L_A_NAME, A_A_NAME FROM ACCOUNT WHERE A_CODE LIKE '%144%' OR A_A_NAME LIKE '%144%' OR A_L_A_NAME LIKE '%144%'")
accounts = cursor.fetchall()
for acc in accounts:
    print('ACC:', acc)

cursor.execute("SELECT BOX_NO, BOX_NAME FROM BOXES WHERE BOX_NAME LIKE '%144%'")
boxes = cursor.fetchall()
for box in boxes:
    print('BOX:', box)

# Wait, check if there's a specific box for '144'. Also check 'C_CODE' in CUSTOMER if it's a customer
cursor.execute("SELECT C_CODE, C_A_NAME FROM CUSTOMER WHERE C_A_NAME LIKE '%144%'")
customers = cursor.fetchall()
for cust in customers:
    print('CUST:', cust)
