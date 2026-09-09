import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'zatca_printer')))
from dotenv import load_dotenv
load_dotenv(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'zatca_printer', '.env')))
from app.database import get_conn

def find_java_license_objects():
    conn = get_conn(readonly=True)
    cur = conn.cursor()
    try:
        # 1) أي كائنات Java (Class/Source/Resource) مرتبطة بالترخيص/التفعيل
        print("=== JAVA objects related to LIC/ACT/DVC/SESSION ===")
        cur.execute("""
            SELECT OWNER, OBJECT_NAME, OBJECT_TYPE, STATUS
            FROM DBA_OBJECTS
            WHERE OBJECT_TYPE LIKE 'JAVA%'
              AND (UPPER(OBJECT_NAME) LIKE '%LIC%'
                OR UPPER(OBJECT_NAME) LIKE '%ACT%'
                OR UPPER(OBJECT_NAME) LIKE '%DVC%'
                OR UPPER(OBJECT_NAME) LIKE '%SESSION%'
                OR UPPER(OBJECT_NAME) LIKE '%GUARD%'
                OR UPPER(OBJECT_NAME) LIKE '%PROTECT%')
            ORDER BY OWNER, OBJECT_NAME
        """)
        for row in cur.fetchall():
            print(" ", row)

        # 2) كل الإجراءات اللي (زي mkdir) معرّفة كـ "language java" في السورس
        print("\n=== PL/SQL wrappers calling embedded Java (language java name) ===")
        cur.execute("""
            SELECT DISTINCT OWNER, NAME, TYPE
            FROM DBA_SOURCE
            WHERE UPPER(TEXT) LIKE '%LANGUAGE JAVA%'
            ORDER BY NAME
        """)
        for row in cur.fetchall():
            print(" ", row)

        # 3) هل يوجد LOGON TRIGGER يفحص عدد الجلسات/الأجهزة عند تسجيل الدخول؟
        print("\n=== LOGON Triggers (may enforce session/device limit at login) ===")
        cur.execute("""
            SELECT OWNER, TRIGGER_NAME, TRIGGERING_EVENT, TABLE_NAME, STATUS
            FROM DBA_TRIGGERS
            WHERE TRIGGERING_EVENT LIKE '%LOGON%'
            ORDER BY OWNER
        """)
        for row in cur.fetchall():
            print(" ", row)

    finally:
        conn.close()

if __name__ == "__main__":
    find_java_license_objects()