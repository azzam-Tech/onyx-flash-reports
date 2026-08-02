import sys
sys.path.insert(0, 'privet/onyx_reports')
import app

client = app.app.test_client()

with client.session_transaction() as sess:
    sess['authed'] = True
    sess['pin'] = "00900"

res = client.get("/?tab=sales&report=sales_collection_summary&year_val=2026&period_type=monthly&period_val=all")
print("Status:", res.status_code)
html = res.get_data(as_text=True)
print("Contains report title:", "صافي المبيعات وإجمالي التحصيل" in html)
print("Contains table headers:", "صافي المبيعات" in html and "إجمالي التحصيل" in html)
print("Sample HTML snippet:")
print(html[html.find('<table'):html.find('</table>')+8] if '<table' in html else html[:500])
