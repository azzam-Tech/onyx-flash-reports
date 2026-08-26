import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_item():
    icode = 'DORWM-13.5'
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("""
            SELECT I_CODE, I_NAME, G_CODE, NVL(INACTIVE, 0)
            FROM IAS_ITM_MST 
            WHERE I_CODE = :1
            """, [icode])
            row = cur.fetchone()
            
            if row:
                print(f"Details for {icode}:")
                print(f"Name: '{row[1]}'")
                print(f"Group: {row[2]}")
                print(f"Inactive?: {row[3]}")
            else:
                print(f"Item {icode} not found in IAS_ITM_MST at all!")

if __name__ == '__main__':
    check_item()
