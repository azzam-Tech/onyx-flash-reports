# -*- coding: utf-8 -*-
import os, sys
import oracledb

lib = os.environ.get("ORA_LIB_DIR", r"C:\oracle64\instantclient_19_23")
try:
    oracledb.init_oracle_client(lib_dir=lib)
except Exception as e:
    pass

try:
    conn = oracledb.connect(
        user=os.environ.get("ORA_USER", "ULT"),
        password=os.environ.get("ORA_PASSWORD", "ULT2017"),
        dsn=os.environ.get("ORA_DSN", "192.168.1.10:1521/ORCL"))
    cur = conn.cursor()
except Exception as e:
    print("خطأ في الاتصال بقاعدة البيانات:", e)
    sys.exit(1)

SCHEMA = "IAS20261"
ITEM = 'OS32ATVHD'

print("="*60)
print(" أداة التحقق من تطابق قاعدة البيانات مع النظام الحي (Live DB Verifier) ")
print("="*60)

print("نقوم الآن بالبحث عن حركات محددة موجودة في صور واجهة أونكس للتأكد من أننا متصلون بالسيرفر الصحيح...\n")

# الحركة 1: تحويل وارد رقم 762 في تاريخ 06/06/2026 بكمية 56
cur.execute(f"""
    SELECT DOC_NO, I_QTY, TO_CHAR(I_DATE, 'YYYY-MM-DD')
    FROM {SCHEMA}.ITEM_MOVEMENT
    WHERE DOC_NO = 762 AND I_CODE = :item AND W_CODE = 121
""", item=ITEM)
row1 = cur.fetchone()

# الحركة 2: المردود رقم 11 في تاريخ 04/07/2026 بكمية 94-
cur.execute(f"""
    SELECT DOC_NO, I_QTY, TO_CHAR(I_DATE, 'YYYY-MM-DD')
    FROM {SCHEMA}.ITEM_MOVEMENT
    WHERE DOC_NO = 11 AND DOC_TYPE = 7 AND I_CODE = :item AND W_CODE = 121
""", item=ITEM)
row2 = cur.fetchone()

if row1 and str(row1[1]) == "56":
    print("✅ ممتاز! قاعدة البيانات هذه تحتوي على الحركات الحقيقية المطابقة للصور (السيرفر الحي).")
else:
    print("❌ خطأ خطير: البيانات لا تتطابق مع الصور!")
    print("الصورة تؤكد وجود تحويل رقم 762 بكمية 56، لكن قاعدة البيانات التي اتصلنا بها لا تحتويه أو تحتويه ببيانات مختلفة.")
    print("هذا يعني أن عنوان IP أو اسم قاعدة البيانات (ORCL) في السكربت يتصل بقاعدة بيانات اختبارية (Test DB) قديمة، وليس السيرفر الحي!")
    print(f"بيانات الاتصال الحالية: DSN = {os.environ.get('ORA_DSN', '192.168.1.10:1521/ORCL')}")

print("\n--- فحص الحركة التي قرأها السكربت السابق لمعرفة مصدرها ---")
cur.execute(f"""
    SELECT DOC_TYPE, DOC_NO, I_QTY, TO_CHAR(I_DATE, 'YYYY-MM-DD')
    FROM {SCHEMA}.ITEM_MOVEMENT
    WHERE DOC_NO = 178 AND I_CODE = :item AND W_CODE = 121
""", item=ITEM)
row3 = cur.fetchone()
if row3:
    print(f"مستند 178 الذي ظهر في السكربت هو من نوع (DOC_TYPE = {row3[0]}) بكمية {row3[2]} بتاريخ {row3[3]}")
    print("إذا لم يكن هذا المستند موجوداً في واجهة أونكس لديك، فهذا يؤكد 100% أننا متصلون بقاعدة بيانات أخرى.")

cur.close()
conn.close()
