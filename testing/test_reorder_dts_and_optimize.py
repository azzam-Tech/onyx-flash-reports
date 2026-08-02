import sys
sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import find_report, run_report

# Test collection_adopted timing
import time
t0 = time.time()
tab, rpt = find_report("dts", "collection_adopted")
cols, rows = run_report(rpt, {"date_from": "2026-06-01", "date_to": "2026-06-30", "grp_by": "rep"})
t1 = time.time()

print(f"Report 'collection_adopted' took ONLY {t1 - t0:.2f} seconds to complete!")
print(f"Returned {len(rows)} rows, {len(cols)} columns.")
