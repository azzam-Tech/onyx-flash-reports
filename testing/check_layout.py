import sys

app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'
with open(app_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
for i, line in enumerate(lines):
    if 'class="cnt"' in line or '.wrap {' in line or '.tbl-wrap {' in line or '.filters {' in line or '.quick-dates {' in line:
        print(i+1, repr(line))
