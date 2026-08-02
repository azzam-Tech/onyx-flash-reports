import sys
import re

app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'

with open(app_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'tbl-wrap' in line or 'tbody tr:first-child' in line:
        print(i+1, repr(line).encode('ascii', 'ignore').decode('ascii'))
