import sys, os
from dotenv import load_dotenv
sys.path.append(os.path.abspath(r'zatca_printer'))
load_dotenv(os.path.abspath(r'zatca_printer\.env'))
from app.database import get_conn
conn = get_conn(readonly=True)
cur = conn.cursor()
cur.execute("SELECT ITM_UNT FROM IAS20261.IAS_ITEM_PRICE WHERE I_CODE = 'KMCT-55S4K'")
print("Unit:", cur.fetchall())
