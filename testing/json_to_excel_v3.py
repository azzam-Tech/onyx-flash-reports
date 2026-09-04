import os
import oracledb
import json
import csv
from dotenv import load_dotenv

load_dotenv('db.env')
lib_dir = os.getenv("ORA_LIB_DIR", r"C:\oracle\instantclient\instantclient_23_0")
try:
    oracledb.init_oracle_client(lib_dir=lib_dir)
except Exception:
    pass

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

        # Replaced EXTERNAL_POST with C_BOX_CODE for Postal Code based on Onyx mapping
        query = """
            SELECT c.C_CODE, c.C_A_NAME, c.C_TAX_CODE, 
                   NVL(c.CR_NO, c.COMM_REG_NO) as CR_NO,
                   c.BUILDING_NO, c.STREET, c.DSTRCT_NM, c.C_BOX_CODE as POSTAL_CODE, c.ADD_NO, c.CITY_NO, 
                   NVL(c.INACTIVE, 0) as INACTIVE, 
                   NVL(c.INACTIVE_SALES, 0) as INACTIVE_SALES,
                   NVL(c.C_CLASS_VAT, 0) as C_CLASS_VAT,
                   NVL(c.BLK_LST, 0) as BLK_LST,
                   NVL(MAX(cc.INACTIVE_SALES), 0) as CURR_INACTIVE_SALES
            FROM IAS20261.CUSTOMER c
            LEFT JOIN IAS20261.CUSTOMER_CURR cc ON c.C_CODE = cc.C_CODE
            GROUP BY c.C_CODE, c.C_A_NAME, c.C_TAX_CODE, NVL(c.CR_NO, c.COMM_REG_NO), 
                     c.BUILDING_NO, c.STREET, c.DSTRCT_NM, c.C_BOX_CODE, c.ADD_NO, c.CITY_NO, 
                     NVL(c.INACTIVE, 0), NVL(c.INACTIVE_SALES, 0), NVL(c.C_CLASS_VAT, 0), NVL(c.BLK_LST, 0)
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        
        active_fake_customers = []

        for row in rows:
            c_code, c_name, tax, crn, bld, street, dist, post, add_no, city, inactive, inactive_sales, c_class_vat, blk_lst, curr_inactive_sales = row
            
            if c_class_vat == 1:
                continue
                
            if inactive == 1 or inactive_sales == 1 or curr_inactive_sales == 1 or blk_lst == 1:
                continue
            
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
                active_fake_customers.append({
                    'code': c_code,
                    'name': c_name,
                    'issues': ", ".join(missing_or_fake)
                })

        print(f"Updated Active Fake Customers: {len(active_fake_customers)}")

        csv_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\Active_Fake_Customers_V3.csv'
        with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['رقم العميل', 'اسم العميل', 'الحقول الناقصة أو الوهمية'])
            for c in active_fake_customers:
                writer.writerow([c['code'], c['name'], c['issues']])
                
        print(f"Saved to: {csv_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
