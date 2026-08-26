import sys, os, json
sys.path.append(os.path.abspath('privet/onyx_reports'))
from app import app
from modules.ar.services import handle_ar_report
from reports_config import TABS

def get_rpt():
    for tab in TABS:
        for r in tab['reports']:
            if r['id'] == 'aging': return r

def test(v_link):
    with app.app_context():
        args = {'vendor_link': str(v_link), 'date_to': '2026-08-31'}
        cols, rows = handle_ar_report('aging', get_rpt(), args)
        total = sum(float(r[-1].replace(',', '')) for r in rows if r[-1] and 'الإجمالي' not in str(r))
        print(f"vendor_link={v_link} Total: {total:,.2f}")

test('1')
test('0')
