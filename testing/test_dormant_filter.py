import sys
import os
sys.path.append(os.path.abspath('privet/onyx_reports'))
from app import app

def test():
    with app.test_client() as client:
        with client.session_transaction() as sess:
            sess['logged_in'] = True
            sess['branch'] = 'all'
            
        res10 = client.get('/api/reports/stock/stock_dormant?as_of=2026-08-27&days=90&dormancy_pct=10').get_json()
        res100 = client.get('/api/reports/stock/stock_dormant?as_of=2026-08-27&days=90&dormancy_pct=100').get_json()

        rows10 = res10.get('rows', [])
        rows100 = res100.get('rows', [])

        print(f"Rows at 10%: {len(rows10)}")
        print(f"Rows at 100%: {len(rows100)}")

        # Find an item that is in 100% but not in 10%
        set10 = {r[0] for r in rows10[1:] if len(r)>0} if len(rows10)>1 else set()
        set100 = {r[0] for r in rows100[1:] if len(r)>0} if len(rows100)>1 else set()

        diff = set100 - set10
        if diff:
            print(f"Found {len(diff)} items that are considered dormant at 100% but NOT at 10%")
            item_code = list(diff)[0]
            for r in rows100[1:]:
                if r[0] == item_code:
                    print("Example Item:")
                    print(f"Code: {r[0]}, Name: {r[1]}, Sales/Input %: {r[-1]}, Days Dormant: {r[-2]}")
                    break
        else:
            print("No difference found.")

if __name__ == '__main__':
    test()
