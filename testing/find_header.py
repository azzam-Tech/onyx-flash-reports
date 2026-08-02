import sys

app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'
with open(app_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
for i, line in enumerate(lines):
    if 'class="top"' in line or 'class="brand"' in line or 'class="logo"' in line or 'class="ttl"' in line:
        print(i+1, repr(line))
