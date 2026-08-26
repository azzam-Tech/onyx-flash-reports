import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import DB_DSN, InterceptConnection
import oracledb

def unfreeze():
    print("Connecting to DB as ULT to unfreeze Group 005...")
    conn = InterceptConnection(oracledb.connect(user='ULT', password='ULT2017', dsn=DB_DSN))
    
    with conn as con:
        with con.cursor() as cur:
            try:
                # Unfreeze all items in group 005 that might have been frozen
                cur.execute("UPDATE IAS_ITM_MST SET INACTIVE = 0 WHERE G_CODE = '005' AND INACTIVE = 1")
                rows = cur.rowcount
                con.commit()
                print(f"SUCCESS: {rows} items in Group 005 have been reactivated (INACTIVE = 0).")
            except Exception as e:
                print(f"Error executing statement: {e}")

if __name__ == '__main__':
    unfreeze()
