import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def find_views():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT view_name FROM all_views WHERE view_name LIKE '%ZATCA%' OR view_name LIKE '%SYNC%' OR view_name LIKE '%E_INV%'")
            for r in cur.fetchall():
                print("View:", r[0])
                
            cur.execute("SELECT table_name FROM all_tables WHERE table_name LIKE '%ZATCA%' OR table_name LIKE '%FATOORA%'")
            for r in cur.fetchall():
                print("Table:", r[0])

if __name__ == '__main__':
    find_views()
