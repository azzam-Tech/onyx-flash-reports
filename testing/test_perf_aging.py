import os
import sys

os.environ["NLS_LANG"] = ".AL32UTF8"
sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import find_report, run_report

tab, rpt = find_report("dts", "perf_aging_dynamic")
print("Testing dts/perf_aging_dynamic...")
try:
    cols, rows = run_report(rpt, {"date_from": "2026-01-01", "date_to": "2026-07-28"})
    print(f"SUCCESS: dts/perf_aging_dynamic returned {len(rows)} rows, {len(cols)} columns.")
    print("Cols:", cols)
    if rows:
        print("First row:", rows[0])
        print("Second row:", rows[1])
except Exception as e:
    print("ERROR IN PERF_AGING_DYNAMIC:", e)
