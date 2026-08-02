import sys
sys.path.insert(0, r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports')
from app import TABS

for tab in TABS:
    for rpt in tab['reports']:
        sql = rpt.get('sql', '')
        if 'الرصيد الافتتاحي مدين' in sql:
            print(f"Found in {tab['id']} -> {rpt['id']}")
