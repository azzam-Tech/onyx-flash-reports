import time
import sys
sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import find_report, run_report

print("Testing tab=dts report execution time...")
t0 = time.time()
tab, rpt = find_report("dts", "perf_aging_dynamic_analytical")
cols, rows = run_report(rpt, {"date_from": "2026-06-01", "date_to": "2026-06-30"})
t1 = time.time()

print(f"Report 'perf_aging_dynamic_analytical' took {t1 - t0:.2f} seconds to complete!")
print(f"Returned {len(rows)} rows, {len(cols)} columns.")
