import os
import sys
from dotenv import load_dotenv
import oracledb

sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer')
from database import get_conn

with get_conn() as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = 'IAS_POST_DTL'")
        cols = [r[0] for r in cur.fetchall()]
        print("Columns in IAS_POST_DTL:", cols)
