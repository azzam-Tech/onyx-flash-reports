import os
import oracledb

# 1. تحديد مسار ملفات أوراكل لتفعيل (Thick mode)
_lib = r"C:\oracle\instantclient\instantclient_23_0"
try:
    oracledb.init_oracle_client(lib_dir=_lib)
    print("✅ Thick mode ON: تم التعرف على ملفات أوراكل بنجاح.")
except Exception as e:
    print("❌ خطأ في تحميل ملفات أوراكل:", e)

# 2. إعدادات الاتصال بالخادم الوسيط عبر شبكة تيل سكيل
DB_USER     = os.environ.get("ORA_USER", "RPT_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD", "ULT2016")
DB_DSN      = os.environ.get("ORA_DSN", "100.100.1.100:1521/ORCL")

def test_connection():
    print(f"🔄 جاري محاولة الاتصال بقاعدة البيانات على ({DB_DSN})...")
    try:
        # إنشاء الاتصال
        with oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN) as con:
            print("✅ تم الاتصال بقاعدة البيانات بنجاح!\n")
            
            # فتح مؤشر (Cursor) لتنفيذ الاستعلام
            with con.cursor() as cur:
                # استعلام بسيط لجلب أكواد وأسماء أول 5 عملاء
                sql = "SELECT C_CODE, C_A_NAME FROM IAS20261.CUSTOMER FETCH FIRST 5 ROWS ONLY"
                cur.execute(sql)
                
                print("📊 نتائج الاستعلام (أول 5 عملاء):")
                print("-" * 50)
                for row in cur.fetchall():
                    print(f"كود العميل: {row[0]} | اسم العميل: {row[1]}")
                print("-" * 50)
                
    except Exception as e:
        print("\n❌ حدث خطأ أثناء الاتصال أو تنفيذ الاستعلام:")
        print(e)

if __name__ == "__main__":
    test_connection()