file_path = 'privet/onyx_reports/reports_config.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re
match = re.search(r'\{"name":"w_code".*?\]', content)
if match:
    print('FOUND EXACTLY:')
    print(match.group(0))
