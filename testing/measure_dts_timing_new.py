import time
import sys
sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import find_report, run_report

t0 = time.time()
tab, rpt = find_report("dts", "") # gets first report in tab=dts
print("Default report for tab=dts:", rpt["id"], rpt["title"])
cols, rows = run_report(rpt, {})
t1 = time.time()

print(f"Opening tab=dts now takes ONLY {t1 - t0:.2f} seconds!")
print(f"Fetched {len(rows)} rows, {len(cols)} columns.")
