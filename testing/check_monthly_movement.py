import sys, os
sys.path.append(os.path.abspath('privet/onyx_reports'))
from app import app
def test():
    with app.test_client() as client:
        with client.session_transaction() as sess:
            sess['logged_in'] = True
        res = client.get('/api/reports/stock/monthly_movement_pivot?p_year=2026')
        print(res.get_data(as_text=True))
test()
