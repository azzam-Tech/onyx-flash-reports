import re
with open('privet/onyx_reports/reports_config.py', 'r', encoding='utf-8') as f:
    text = f.read()
m = re.search(r'\"id\":\s*\"prof\".*?\"sql\":\s*\"\"\"(.*?)\"\"\"', text, re.DOTALL)
if m:
    print(m.group(1)[:1500])
else:
    print("Not found")
