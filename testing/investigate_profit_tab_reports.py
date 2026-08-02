import os
import sys

os.environ["NLS_LANG"] = ".AL32UTF8"
sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import find_report, run_report

print("=== INSPECTING PROFIT TAB REPORTS (EXCLUDING TRUE_INCOME_STATEMENT) ===")

reports = [
    ("prof_summary", "ملخّص مجمل الربح للفترة", {"date_from": "2026-01-01", "date_to": "2026-07-28", "rep_code": ""}),
    ("net_profit", "صافي الربح للفترة (بعد كل المصاريف)", {"date_from": "2026-01-01", "date_to": "2026-07-28"}),
    ("prof_item", "ربحية الصنف", {"date_from": "2026-01-01", "date_to": "2026-07-28", "rep_code": ""}),
    ("prof_cust", "ربحية العميل", {"date_from": "2026-01-01", "date_to": "2026-07-28", "rep_code": ""}),
    ("prof_rep", "ربحية المندوب", {"date_from": "2026-01-01", "date_to": "2026-07-28"}),
]

for rpt_id, title, args in reports:
    tab, rpt = find_report("prof", rpt_id)
    try:
        cols, rows = run_report(rpt, args)
        print(f"\n📊 {rpt_id} ({title}): {len(rows)} rows, {len(cols)} cols")
        print("   Cols:", cols)
        if rows:
            print("   First row:", rows[0])
            if len(rows) > 1:
                print("   Second row:", rows[1])
    except Exception as e:
        print(f"\n❌ {rpt_id} ({title}): ERROR -> {e}")
