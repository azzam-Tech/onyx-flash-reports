import sys
import os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_group_name():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT G_CODE, G_A_NAME, G_E_NAME FROM GROUP_DETAILS WHERE G_CODE = '003'")
            row = cur.fetchone()
            
            with open("testing/group_003.json", "w", encoding="utf-8") as f:
                json.dump({"G_CODE": row[0], "G_A_NAME": row[1], "G_E_NAME": row[2]}, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    check_group_name()
