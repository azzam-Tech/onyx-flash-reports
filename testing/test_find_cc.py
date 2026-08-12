import sys
file_path = 'privet/onyx_reports/reports_config.py'
with open(file_path, 'r', encoding='utf-8') as f:
    c = f.read()
idx = c.find('"id":"cost_centers"')
if idx != -1:
    print(c[idx:idx+500])
