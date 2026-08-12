import os

file_path = 'privet/onyx_reports/reports_config.py'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "'id':'stock'" in line or '"id":"stock"' in line or '"id": "stock"' in line or "'id': 'stock'" in line:
        print(f"Line {i+1}: {line.strip()}")
