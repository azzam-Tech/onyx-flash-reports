import sys
sys.path.insert(0, r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports')
from app import TABS
for t in TABS:
    for r in t['reports']:
        print(f"{t['id']}: {r['id']} -> {r['title']}")
