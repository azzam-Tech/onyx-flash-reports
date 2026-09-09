import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'zatca_printer')))
from dotenv import load_dotenv
load_dotenv(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'zatca_printer', '.env')))
from app.database import get_conn

try:
    conn = get_conn(readonly=True)
    cur = conn.cursor()
    print("--- Fetching API Packages ---")
    sql = """
        SELECT OWNER, OBJECT_NAME, OBJECT_TYPE
        FROM ALL_OBJECTS 
        WHERE OBJECT_TYPE IN ('PACKAGE')
          AND (OBJECT_NAME LIKE '%API%' OR OBJECT_NAME LIKE '%ARS%')
        ORDER BY OBJECT_NAME
    """
    cur.execute(sql)
    rows = cur.fetchall()
    for r in rows:
        print(f"{r[0]}.{r[1]} [{r[2]}]")
except Exception as e:
    print(e)
finally:
    if 'conn' in locals():
        conn.close()
