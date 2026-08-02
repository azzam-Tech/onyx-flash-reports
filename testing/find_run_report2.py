import re

with open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

m = re.search(r'def run_report.*?:\s*\n.*?(?=def |\Z)', content, re.DOTALL)
if m:
    print(m.group(0)[:1000])
else:
    print("Not found")
