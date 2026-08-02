import sys
with open(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if 'div class="filters"' in line or 'form method="get"' in line:
            print(f"{i+1}: {line.strip()}")
