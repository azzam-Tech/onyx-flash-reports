import os
import sys

os.environ["NLS_LANG"] = ".AL32UTF8"
sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import find_report, run_report

tab, rpt = find_report("sales", "by_customer")
print("Testing sales/by_customer execution...")
try:
    cols, rows = run_report(rpt, {"date_from": "2026-01-01", "date_to": "2026-07-28", "c_code": "", "rep_code": ""})
    print(f"SUCCESS: sales/by_customer returned {len(rows)} rows, {len(cols)} columns.")
    print("Cols:", cols)
    for r in rows[:5]:
        print(" ", r)
except Exception as e:
    print("ERROR IN BY_CUSTOMER:", e)
