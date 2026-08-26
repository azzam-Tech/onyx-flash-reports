import sys, os, json
sys.path.append(os.path.abspath('privet/onyx_reports'))
from app import app


def test_api():
    with app.test_client() as client:
        # Mocking session behavior to avoid 401
        with client.session_transaction() as sess:
            sess['logged_in'] = True
            
        res = client.get('/api/reports/summary/aging?vendor_link=1')
        print("Status (vendor_link=1):", res.status_code)
        if res.status_code == 200:
            data = res.get_json()
            print("Binds received by handler:", data.get('binds'))
            rows = data.get('rows', [])
            total = sum(float(r[-1].replace(',', '')) for r in rows if r[-1] and 'الإجمالي' not in str(r))
            print(f"Total via API (vendor_link=1): {total:,.2f}")
            
        res2 = client.get('/api/reports/summary/aging?vendor_link=0')
        print("Status (vendor_link=0):", res2.status_code)
        if res2.status_code == 200:
            data = res2.get_json()
            rows = data.get('rows', [])
            total = sum(float(r[-1].replace(',', '')) for r in rows if r[-1] and 'الإجمالي' not in str(r))
            print(f"Total via API (vendor_link=0): {total:,.2f}")

test_api()
