import os
import oracledb
import json
from dotenv import load_dotenv

load_dotenv('db.env')
lib_dir = os.getenv("ORA_LIB_DIR", r"C:\oracle\instantclient\instantclient_23_0")
try:
    oracledb.init_oracle_client(lib_dir=lib_dir)
except Exception:
    pass

# Set NLS_LANG for Arabic encoding
os.environ["NLS_LANG"] = "ARABIC_SAUDI ARABIA.AL32UTF8"

def get_conn():
    return oracledb.connect(
        user=os.getenv("DB_USER", "RPT_USER"),
        password=os.getenv("DB_PASS", "ULT2016"),
        dsn=os.getenv("ORA_DSN", "100.100.1.100:1521/ORCL")
    )

def is_fake(val):
    if not val:
        return True
    val = str(val).strip()
    if val in ('111', '1111', '11111', '1234', '12345', '123456', '0000', '00000', '3000000000000000003'):
        return True
    if len(val) < 2:
        return True
    if len(set(val)) == 1 and val[0].isdigit():
        return True
    if '12345' in val:
        return True
    return False

def main():
    try:
        connection = get_conn()
        cursor = connection.cursor()

        query = """
            SELECT C_CODE, C_A_NAME, C_TAX_CODE, COMM_REG_NO, BUILDING_NO, STREET, DSTRCT_NM, EXTERNAL_POST, ADD_NO, CITY_NO
            FROM IAS20261.CUSTOMER
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        
        fake_customers = []

        for row in rows:
            c_code, c_name, tax, crn, bld, street, dist, post, add_no, city = row
            
            missing_or_fake = []
            
            if is_fake(tax): missing_or_fake.append("الرقم الضريبي")
            if is_fake(crn): missing_or_fake.append("السجل التجاري")
            if is_fake(bld): missing_or_fake.append("المبنى")
            if is_fake(street): missing_or_fake.append("الشارع")
            if is_fake(dist): missing_or_fake.append("الحي")
            if is_fake(post): missing_or_fake.append("الرمز البريدي")
            if is_fake(add_no): missing_or_fake.append("الرقم الإضافي")
            if not city: missing_or_fake.append("المدينة")

            if missing_or_fake:
                fake_customers.append({
                    'code': c_code,
                    'name': c_name,
                    'issues': ", ".join(missing_or_fake)
                })

        with open(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\fake_customers_data.json', 'w', encoding='utf-8') as f:
            json.dump(fake_customers, f, ensure_ascii=False, indent=4)
        
        print(f"Found {len(fake_customers)} fake customers. JSON generated.")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
