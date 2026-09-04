import sqlite3
import os
import json

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app_data.db')

def get_local_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_local_db():
    with get_local_db() as conn:
        cursor = conn.cursor()
        
        # جدول إعدادات النظام وتعيينات المناديب
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS rep_mapping (
                rep_code TEXT PRIMARY KEY,
                emp_code TEXT NOT NULL
            )
        """)
        
        # جدول الجلسات الدائمة أو عربة التسوق المؤقتة (لاحقاً)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cart (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rep_code TEXT,
                customer_code TEXT,
                cart_data TEXT,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        
        # عملية استيراد البيانات القديمة من JSON إذا كانت موجودة والجدول فارغ
        cursor.execute("SELECT COUNT(*) FROM rep_mapping")
        count = cursor.fetchone()[0]
        
        if count == 0:
            json_path = os.path.join(os.path.dirname(__file__), 'rep_mapping.json')
            if os.path.exists(json_path):
                try:
                    with open(json_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        for rep_code, emp_code in data.items():
                            cursor.execute(
                                "INSERT INTO rep_mapping (rep_code, emp_code) VALUES (?, ?)",
                                (rep_code, emp_code)
                            )
                    conn.commit()
                    print("تم استيراد بيانات rep_mapping.json بنجاح إلى SQLite.")
                except Exception as e:
                    print("خطأ أثناء استيراد الـ JSON:", e)

def get_emp_code(rep_code):
    with get_local_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT emp_code FROM rep_mapping WHERE rep_code = ?", (str(rep_code).strip(),))
        row = cursor.fetchone()
        if row:
            return row['emp_code']
    return str(rep_code).strip()
