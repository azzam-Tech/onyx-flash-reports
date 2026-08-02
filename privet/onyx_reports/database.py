import os
import oracledb

# قراءة المتغيرات من ملف db.env إن وجد
env_path = os.path.join(os.path.dirname(__file__), 'db.env')
if os.path.exists(env_path):
    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            if '=' in line and not line.strip().startswith('#'):
                k, v = line.strip().split('=', 1)
                os.environ[k.strip()] = v.strip()

DB_USER     = os.environ.get("ORA_USER",     "RPT_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD", "ULT2016")
DB_DSN      = os.environ.get("ORA_DSN",      "100.100.1.100:1521/ORCL")
_lib        = os.environ.get("ORA_LIB_DIR")

try:
    if _lib:
        oracledb.init_oracle_client(lib_dir=_lib)
    else:
        try:
            # 1. التجربة الأولى: مسار الأوراكل الثابت في جهازك الحالي
            oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient\instantclient_23_0")
        except Exception:
            # 2. التجربة الثانية: الاعتماد على بيئة الويندوز (هذا ما يعمل في الجهاز الآخر!)
            oracledb.init_oracle_client()
    print("Thick mode ON")
except Exception as e:
    print("thick warn:", e)

def get_conn():
    return oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
