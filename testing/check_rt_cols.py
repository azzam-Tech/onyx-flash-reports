import os
import sys
sys.path.append(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute("""
            SELECT DISTINCT PREV_YEAR 
            FROM IAS20261.IAS_RT_BILL_MST
        """)
        for row in cur.fetchall():
            print(f"PREV_YEAR: {row[0]}")
