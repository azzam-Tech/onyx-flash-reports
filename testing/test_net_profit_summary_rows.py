import sys
sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn, run_sql_report, find_report

tab, rpt = find_report("prof", "true_income_statement")
cols, raw_rows = run_sql_report(rpt, {"date_from": "2026-01-01", "date_to": "2026-12-31", "rep_code": ""})

# Calculate totals
tot_mv_dr = 0.0
tot_mv_cr = 0.0
tot_bal_dr = 0.0
tot_bal_cr = 0.0

for r in raw_rows:
    # r = (code, name, op_dr, op_cr, mv_dr, mv_cr, bal_dr, bal_cr)
    mv_dr = float(r[4].replace(',', '')) if r[4] else 0.0
    mv_cr = float(r[5].replace(',', '')) if r[5] else 0.0
    bal_dr = float(r[6].replace(',', '')) if r[6] else 0.0
    bal_cr = float(r[7].replace(',', '')) if r[7] else 0.0
    
    tot_mv_dr += mv_dr
    tot_mv_cr += mv_cr
    tot_bal_dr += bal_dr
    tot_bal_cr += bal_cr

period_net_profit = tot_mv_cr - tot_mv_dr
final_net_profit = tot_bal_cr - tot_bal_dr

print(f"Total Movement Debit (Costs/Expenses):  {tot_mv_dr:,.2f} SAR")
print(f"Total Movement Credit (Revenues):        {tot_mv_cr:,.2f} SAR")
print(f"--> Period Net Profit (رصيد الفترة صافي الربح): {period_net_profit:,.2f} SAR\n")

print(f"Total Balances Debit (Net Costs):       {tot_bal_dr:,.2f} SAR")
print(f"Total Balances Credit (Net Revenues):   {tot_bal_cr:,.2f} SAR")
print(f"--> Final Net Profit (الرصيد النهائي صافي الربح): {final_net_profit:,.2f} SAR")
