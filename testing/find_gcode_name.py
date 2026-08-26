import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            # Let's check where G_CODE is the primary key or referenced
            # We can search all tables with G_CODE column
            cur.execute("""
                SELECT TABLE_NAME, COLUMN_NAME 
                FROM ALL_TAB_COLUMNS 
                WHERE OWNER = 'IAS20261' AND COLUMN_NAME IN ('G_CODE', 'GRP_CLASS_CODE')
            """)
            tables = cur.fetchall()
            
            for t, c in tables:
                try:
                    cur.execute(f"SELECT * FROM {t} WHERE {c} IN ('03', '003') FETCH FIRST 1 ROWS ONLY")
                    row = cur.fetchone()
                    if row:
                        print(f"Found in {t}: {row}")
                except Exception:
                    pass
                
except Exception as e:
    print(f"Error: {e}")
