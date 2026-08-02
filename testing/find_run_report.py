import re

with open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

m = re.search(r'def run_report.*?\n\s*sql = rpt\["sql"\]', content, re.DOTALL)
if m:
    print(m.group(0))
else:
    print("Not found")
