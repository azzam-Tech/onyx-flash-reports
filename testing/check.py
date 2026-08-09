import re

with open('privet/onyx_reports/reports_config.py', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'\"id\":\"(prof_[^\"]+)\".*?\"sql\":\"\"\"(.*?)\"\"\"', text, re.DOTALL):
    print('REPORT:', m.group(1))
    sql = m.group(2)
    for line in sql.split('\n'):
        if 'cost' in line.lower():
            print('  ', line.strip())
