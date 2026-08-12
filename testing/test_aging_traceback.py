import sys, os
sys.path.append(os.path.abspath('privet/onyx_reports'))
import report_handlers

try:
    rpt = {"id": "aging"}
    args = {
        "date_to": "2026-08-31",
        "rep_code": "144",
        "c_code": "",
        "aging_ranges": "2,30,60,90,120"
    }
    res = report_handlers.run_cust_aging(rpt, args)
    print("Success, rows:", len(res["rows"]))
except Exception as e:
    import traceback
    traceback.print_exc()
