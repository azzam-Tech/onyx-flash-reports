import sys
sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import TABS, TABMAP

dts_tab = TABMAP.get("dts")
print("Reports found under tab=dts:")
for idx, r in enumerate(dts_tab["reports"]):
    print(f"  {idx+1}. ID: {r['id']} | Title: {r['title']}")
