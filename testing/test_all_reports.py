import os
import sys

os.environ["NLS_LANG"] = ".AL32UTF8"
sys.stdout.reconfigure(encoding='utf-8')

# Add privet/onyx_reports to sys.path to import app
sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")

from app import TABS, run_report

print("=== TESTING ALL REPORTS IN APP.PY ===")

failed_reports = []
empty_reports = []
success_reports = []

for tab in TABS:
    tab_id = tab["id"]
    if tab.get("dash"):
        continue
    for rpt in tab.get("reports", []):
        rpt_id = rpt["id"]
        title = rpt["title"]
        try:
            cols, rows = run_report(rpt, {})
            if not rows:
                empty_reports.append(f"{tab_id}/{rpt_id} ({title}): 0 rows returned")
            else:
                success_reports.append(f"{tab_id}/{rpt_id} ({title}): {len(rows)} rows, {len(cols)} cols")
        except Exception as e:
            failed_reports.append(f"{tab_id}/{rpt_id} ({title}): ERROR -> {e}")

print(f"\n✅ SUCCESS REPORTS ({len(success_reports)}):")
for s in success_reports:
    print(" ", s)

print(f"\n⚠️ EMPTY REPORTS ({len(empty_reports)}):")
for e in empty_reports:
    print(" ", e)

print(f"\n❌ FAILED REPORTS ({len(failed_reports)}):")
for f in failed_reports:
    print(" ", f)
