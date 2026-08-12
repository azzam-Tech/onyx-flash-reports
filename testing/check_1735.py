import sys
import os

# Add privet directory to path to import report_handlers
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "privet", "onyx_reports"))

from report_handlers import run_cust_aging

args = {
    "tab": "ar",
    "report": "aging",
    "vendor_link": "0",
    "grp_code": "141 - عملاء عبدالله النهدي",
    "cc_code": "",
    "date_to": "2026-06-30",
    "aging_ranges": "30,60,90,120",
    "rep_code": "",
    "c_code": "1735"
}

rpt = {"id": "aging"}
try:
    cols, rows = run_cust_aging(rpt, args)
    
    for row in rows:
        if str(row[0]).strip() == "1735":
            print("--- Our System Totals for 1735 ---")
            print(f"0-30: {row[3]}")
            print(f"31-60: {row[4]}")
            print(f"61-90: {row[5]}")
            print(f"91-120: {row[6]}")
            print(f">120: {row[7]}")
            print(f"Total Balance: {row[8]}")
            break

except Exception as e:
    print("Error:", e)
