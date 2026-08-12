import sys
file_path = 'privet/onyx_reports/reports_config.py'
with open(file_path, 'r', encoding='utf-8') as f:
    c = f.read()
    
idx = c.find('"name":"rep_code"')
if idx != -1:
    print("rep_code:", c[idx:idx+150])
    
idx2 = c.find('"name":"c_code"')
if idx2 != -1:
    print("c_code:", c[idx2:idx2+150])
