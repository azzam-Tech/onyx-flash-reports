import os
import oracledb
from dotenv import load_dotenv

load_dotenv('db.env')
lib_dir = os.getenv("ORA_LIB_DIR", r"C:\oracle\instantclient\instantclient_23_0")
try:
    oracledb.init_oracle_client(lib_dir=lib_dir)
except Exception:
    pass

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
    # If it's a long string of just one repeating character like '111111111'
    if len(set(val)) == 1 and val[0].isdigit():
        return True
    # If it contains sequence '12345'
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

        # Generate markdown report
        md_content = "# تقرير العملاء ذوي البيانات الناقصة أو الوهمية (حقول هيئة الزكاة)\n\n"
        md_content += f"**إجمالي العملاء المخالفين:** {len(fake_customers)}\n\n"
        
        if fake_customers:
            md_content += "| رقم العميل | اسم العميل | الحقول الناقصة أو الوهمية |\n"
            md_content += "|---|---|---|\n"
            for c in fake_customers[:100]: # limit to 100 to avoid massive markdown
                md_content += f"| {c['code']} | {c['name']} | {c['issues']} |\n"
            
            if len(fake_customers) > 100:
                md_content += f"\n*(تم عرض أول 100 عميل فقط من أصل {len(fake_customers)})*\n"

        with open(r'c:\Users\amarn\.gemini\antigravity-ide\brain\4fb2f17e-6238-41c0-acb1-78bf3adf7214\fake_data_customers.md', 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"Found {len(fake_customers)} fake customers. Report generated.")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
