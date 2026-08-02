import os
import sys

os.environ["NLS_LANG"] = ".AL32UTF8"
sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import TABS, find_report, run_report

print("=== TESTING THE 5 EMPTY REPORTS WITH DEFAULTS ===")

reports_to_test = [
    ("sales", "sales_collection_summary", {"year_val": "2026", "period_type": "monthly", "period_val": "all", "grp_by": "cc"}),
    ("sales", "debt_movement_summary", {"year_val": "2026", "period_type": "monthly", "period_val": "all", "grp_by": "cc"}),
    ("dts", "perf_aging_exact", {"date_from": "2026-01-01", "date_to": "2026-07-28", "rep_code": ""}),
    ("stock", "stock_move", {"i_code": "101", "date_from": "2026-01-01", "date_to": "2026-07-28"}),
    ("stock", "main_wh_movement", {"date_from": "2026-01-01", "date_to": "2026-07-28", "i_code": ""}),
]

for tab_id, rpt_id, args in reports_to_test:
    tab, rpt = find_report(tab_id, rpt_id)
    try:
        cols, rows = run_report(rpt, args)
        print(f"✅ {tab_id}/{rpt_id} ({rpt['title']}): {len(rows)} rows, {len(cols)} cols")
    except Exception as e:
        print(f"❌ {tab_id}/{rpt_id} ({rpt['title']}): ERROR -> {e}")
