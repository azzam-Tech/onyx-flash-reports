import sys
sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import find_report, run_report

tab, rpt = find_report("prof", "true_income_statement")
print(f"Report found: tab={tab['id']}, rpt={rpt['id']}")
cols, rows = run_report(rpt, {"date_from": "2026-01-01", "date_to": "2026-12-31"})
print(f"SUCCESS: Fetched {len(rows)} rows, {len(cols)} columns.")
for r in rows[:5]:
    print(r)
