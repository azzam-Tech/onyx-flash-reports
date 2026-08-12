import sys, os
import traceback
sys.path.append(os.path.abspath('privet/onyx_reports'))
from reports_config import TABS
import report_handlers

args = {
    'date_from': '2026-07-01',
    'date_to': '2026-08-31',
    'rep_code': '',
    'c_code': '',
    'aging_ranges': '2,30,60,90,120'
}

print("Running all reports to check for errors...")
success_count = 0
error_count = 0
failed_reports = []

for tab in TABS:
    for rpt in tab.get('reports', []):
        try:
            cols, rows = report_handlers.run_report(rpt, args)
            success_count += 1
            print(f"PASS {rpt['id']} - Success ({len(rows)} rows)")
        except Exception as e:
            error_count += 1
            print(f"FAIL {rpt['id']} - FAILED: {str(e)}")
            failed_reports.append((rpt['id'], traceback.format_exc()))

print("\\n--- Summary ---")
print(f"Total Successful: {success_count}")
print(f"Total Failed: {error_count}")

if error_count > 0:
    print("\\n--- Failed Reports Tracebacks ---")
    for rpt_id, tb in failed_reports:
        print(f"REPORT: {rpt_id}")
        print(tb)
