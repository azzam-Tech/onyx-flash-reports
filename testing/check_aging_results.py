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
    "c_code": ""
}

rpt = {"id": "aging"}
try:
    cols, rows = run_cust_aging(rpt, args)
    
    total_0_30 = 0.0
    total_31_60 = 0.0
    total_61_90 = 0.0
    total_91_120 = 0.0
    total_over_120 = 0.0
    total_balance = 0.0

    for row in rows:
        # Indices based on columns: 'رمز العميل', 'اسم العميل', 'المندوب', '0-30', '31-60', '61-90', '91-120', 'أكبر من 120', 'الإجمالي'
        def clean_amt(val):
            if val is None or val == '': return 0.0
            return float(str(val).replace(',', ''))
            
        total_0_30 += clean_amt(row[3])
        total_31_60 += clean_amt(row[4])
        total_61_90 += clean_amt(row[5])
        total_91_120 += clean_amt(row[6])
        total_over_120 += clean_amt(row[7])
        total_balance += clean_amt(row[8])

    print("--- Our System Totals ---")
    print(f"0-30: {total_0_30:,.2f}")
    print(f"31-60: {total_31_60:,.2f}")
    print(f"61-90: {total_61_90:,.2f}")
    print(f"91-120: {total_91_120:,.2f}")
    print(f">120: {total_over_120:,.2f}")
    print(f"Total Balance: {total_balance:,.2f}")

except Exception as e:
    print("Error:", e)
