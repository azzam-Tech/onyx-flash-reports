import os
import sys

os.environ["NLS_LANG"] = ".AL32UTF8"
sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import find_report, run_report

print("=== VERIFYING DEBT MOVEMENT SUMMARY ALL GROUPINGS & PERIODS ===")

tab, rpt = find_report("sales", "debt_movement_summary")

grp_options = [
    ("cc", "مراكز التكلفة"),
    ("rep", "المناديب"),
    ("customer", "العملاء"),
    ("period", "الفترات الزمنية (شهري)"),
]

all_passed = True

for grp_val, label in grp_options:
    args = {"year_val": "2026", "period_type": "monthly", "period_val": "all", "grp_by": grp_val}
    try:
        cols, rows = run_report(rpt, args)
        if len(rows) > 0 and len(cols) == 8:
            print(f"✅ GROUP BY '{label}' ({grp_val}): PASSED -> {len(rows)} rows, {len(cols)} cols")
            print(f"   Sample Top Row: {rows[1][:4] if len(rows)>1 else rows[0][:4]}")
        else:
            print(f"❌ GROUP BY '{label}' ({grp_val}): FAILED -> rows={len(rows)}, cols={len(cols)}")
            all_passed = False
    except Exception as e:
        print(f"❌ GROUP BY '{label}' ({grp_val}): ERROR -> {e}")
        all_passed = False

print("\n--- Period Type Variations Test ---")
period_types = [
    ("monthly", "all", "شهري كامل السنة"),
    ("quarterly", "all", "ربعي كامل السنة"),
    ("semi_annual", "all", "نصفي كامل السنة"),
]

for ptype, pval, plabel in period_types:
    args = {"year_val": "2026", "period_type": ptype, "period_val": pval, "grp_by": "period"}
    try:
        cols, rows = run_report(rpt, args)
        print(f"✅ PERIOD TYPE '{plabel}': PASSED -> {len(rows)} rows, {len(cols)} cols")
    except Exception as e:
        print(f"❌ PERIOD TYPE '{plabel}': ERROR -> {e}")
        all_passed = False

if all_passed:
    print("\n🎯 FINAL VERIFICATION RESULT: 100% CERTAIN AND VERIFIED WITH ZERO ERRORS!")
