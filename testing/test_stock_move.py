import sys
from dotenv import load_dotenv

sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports')
from report_handlers import run_sql_report
from modules.warehouses.repository import get_stock_move_sql

rpt = {
    'id': 'stock_move',
    'sql': get_stock_move_sql()
}

args = {
    'i_code': 'some_code - Some Name',
    'date_from': '2026-01-01',
    'date_to': '2026-12-31'
}

cols, rows = run_sql_report(rpt, args)
print("Columns:", cols)
print("Rows:", rows)
