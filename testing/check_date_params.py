import sys
sys.path.insert(0, r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports')
from app import TABS

for t in TABS:
    for r in t['reports']:
        for p in r.get('params', []):
            if p['name'] in ('date_from', 'date_to'):
                print(f"{t['id']} -> {r['id']} : {p}")
