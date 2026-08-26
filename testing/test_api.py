import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from app import app

client = app.test_client()

# Login to bypass auth (simulate the session)
# Wait, auth might check cookies or headers. Let's see if we can just patch it or simulate login.
# Actually, the easiest way to test reports.py parameter logic is to just call `handle_ar_report` directly.
from modules.ar.services import handle_ar_report
from reports_config import REPORTS
rpt = next(r for r in REPORTS['ar'] if r['id'] == 'aging')
args = {'vendor_link': '0', 'date_to': '2026-08-31'}
cols, rows = handle_ar_report('aging', rpt, args)
print("Handled rows:", len(rows))

# Let's test the route logic directly.
from routes.reports import resolved_params, get_reports_config
# Actually, let's just make a test request without auth.
# If auth is required, maybe I can disable it?
