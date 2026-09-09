import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'zatca_printer')))
from dotenv import load_dotenv
load_dotenv(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'zatca_printer', '.env')))
from app.database import get_conn

conn = get_conn(readonly=True)
cur = conn.cursor()
cur.execute("SELECT W_CODE, W_NAME FROM WAREHOUSES WHERE ROWNUM <= 10")
print(cur.fetchall())
conn.close()
