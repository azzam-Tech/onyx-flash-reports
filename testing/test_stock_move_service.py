import sys
from dotenv import load_dotenv

sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports')
from report_handlers import run_sql_report
from reports_config import TABS

stock_move_rpt = None
for t in TABS:
    for r in t['reports']:
        if r['id'] == 'stock_move':
            stock_move_rpt = r
            break

print("Report config:", stock_move_rpt)

from modules.warehouses.services import handle_warehouse_report

args = {
    'i_code': '0101010101 - Some Item',
    'date_from': '2026-01-01',
    'date_to': '2026-12-31'
}

try:
    cols, rows = handle_warehouse_report('stock_move', stock_move_rpt, args)
    print("Cols:", cols)
    print("Rows:", len(rows))
except Exception as e:
    import traceback
    traceback.print_exc()

