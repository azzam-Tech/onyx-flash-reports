import sys
from dotenv import load_dotenv

sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports')
from report_handlers import run_sql_report
from reports_config import TABS
from modules.warehouses.repository import get_stock_move_sql

rpt = {
    'id': 'stock_move',
    'sql': get_stock_move_sql(),
    'params': [{'name': 'i_code'}, {'name': 'date_from'}, {'name': 'date_to'}]
}

# Let's find an actual item code
from database import get_conn
with get_conn() as con:
    with con.cursor() as cur:
        cur.execute("SELECT I_CODE FROM ITEM_MOVEMENT FETCH FIRST 1 ROWS ONLY")
        real_icode = cur.fetchone()[0]

args = {
    'i_code': real_icode,
    'date_from': '2026-01-01',
    'date_to': '2026-12-31'
}

cols, rows = run_sql_report(rpt, args)
print("Cols:", cols)
print("Rows:", len(rows))
if rows:
    print("First row:", rows[0])
