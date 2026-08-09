import re
with open('privet/onyx_reports/reports_config.py', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'\"id\":\"prof_summary\".*?\"sql\":\"\"\"(.*?)\"\"\"', text, re.DOTALL)
sql = m.group(1)
print(sql[:1500])
