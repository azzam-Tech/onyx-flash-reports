import re

with open(r'C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'\{\s*"id"\s*:\s*"debt_movement_summary".*?\]\s*\}', text, re.DOTALL)
if m:
    with open(r'C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\dump.txt', 'w', encoding='utf-8') as out:
        out.write(m.group(0))
