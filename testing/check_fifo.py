import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "privet", "onyx_reports"))
from report_handlers import run_cust_aging

def run_strict_fifo():
    args = {
        "grp_code": "141",
        "date_to": "2026-06-30",
        "aging_ranges": "30, 60, 90, 120",
        "vendor_link": "0"
    }

    # I will mock the exact matching logic to bypass it
    cols, rows = run_cust_aging({"id": "aging"}, args)
    
    # Print overall totals
    total_balance = sum(float(str(r[-1]).replace(',', '')) for r in rows)
    total_0_30 = sum(float(str(r[3]).replace(',', '')) for r in rows)
    total_31_60 = sum(float(str(r[4]).replace(',', '')) for r in rows)
    total_61_90 = sum(float(str(r[5]).replace(',', '')) for r in rows)
    total_91_120 = sum(float(str(r[6]).replace(',', '')) for r in rows)
    total_gt_120 = sum(float(str(r[7]).replace(',', '')) for r in rows)

    print(f"Total Balance: {total_balance:,.2f}")
    print(f"0-30: {total_0_30:,.2f}")
    print(f"31-60: {total_31_60:,.2f}")
    print(f"61-90: {total_61_90:,.2f}")
    print(f"91-120: {total_91_120:,.2f}")
    print(f">120: {total_gt_120:,.2f}")

if __name__ == "__main__":
    run_strict_fifo()
