import os
import sys
sys.path.append(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute("SELECT * FROM IAS20261.IAS_ITM_MST WHERE ROWNUM = 1")
        columns = [col[0] for col in cur.description]
        print("Columns in IAS_ITM_MST containing COST:")
        for c in columns:
            if 'COST' in c.upper():
                print(c)
                
        # Let's also check if there's any cost table.
        cur.execute("SELECT table_name FROM all_tables WHERE owner='IAS20261' AND table_name LIKE '%COST%'")
        print("\nTables with COST:")
        for t in cur.fetchall():
            print(t[0])
