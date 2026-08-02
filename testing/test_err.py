import traceback, sys
sys.path.append('privet/onyx_reports')
import app

rpt = next(r for t in app.TABS for r in t.get('reports',[]) if r['id']=='sales_vs_collection')
try:
    cols, rows = app.run_report(rpt, {'p_year':'2026','p_type':'month','p_val':'1'})
    print("Success")
except Exception as e:
    traceback.print_exc()
