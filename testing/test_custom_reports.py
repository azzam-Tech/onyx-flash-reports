import os
import sys

os.environ["NLS_LANG"] = ".AL32UTF8"
sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import find_report, run_report

print("=== TESTING SALES COLLECTION AND DEBT MOVEMENT SUMMARY REPORTS ===")

tab1, rpt1 = find_report("sales", "sales_collection_summary")
try:
    cols1, rows1 = run_report(rpt1, {"year_val": "2026", "period_type": "monthly", "period_val": "all", "grp_by": "cc"})
    print(f"✅ sales_collection_summary: {len(rows1)} rows, {len(cols1)} cols")
    if rows1:
        print("  First row:", rows1[0])
except Exception as e:
    print("❌ sales_collection_summary ERROR:", e)

tab2, rpt2 = find_report("sales", "debt_movement_summary")
try:
    cols2, rows2 = run_report(rpt2, {"year_val": "2026", "period_type": "monthly", "period_val": "all", "grp_by": "cc"})
    print(f"✅ debt_movement_summary: {len(rows2)} rows, {len(cols2)} cols")
    if rows2:
        print("  First row:", rows2[0])
except Exception as e:
    print("❌ debt_movement_summary ERROR:", e)
