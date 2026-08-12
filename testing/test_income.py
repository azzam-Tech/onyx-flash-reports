import sys, os
sys.path.append(os.path.abspath('privet/onyx_reports'))
import report_handlers
from database import get_conn

try:
    args = {'date_from': '2026-08-01', 'date_to': '2026-08-31'}
    rpt = {"id": "true_income_statement"}
    
    from reports_config import TABS
    for tab in TABS:
        for r in tab["reports"]:
            if r["id"] == "true_income_statement":
                rpt = r
                break
            
    cols, rows = report_handlers.run_report(rpt, args)
    print("Success, rows:", len(rows))
except Exception as e:
    import traceback
    traceback.print_exc()
