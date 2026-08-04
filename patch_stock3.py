import re

file_path = 'privet/onyx_reports/reports_config.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

def replacer(match):
    old_prefix = match.group(1)
    new_prefix = old_prefix[:-1] + ',{"name":"i_code","label":"رقم الصنف (اختياري)","type":"text","default":""}]'
    return new_prefix + match.group(2)

content = re.sub(r'(\{"id":"stock_bal",.*?\[.*?\])(\},"sql":)', replacer, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
