import json
import re

with open('privet/onyx_reports/reports_config.py', 'r', encoding='utf-8') as f:
    content = f.read()

tabs = re.findall(r'{"id":"([^"]+)","title":"([^"]+)",(?:.*?)?"reports":\[', content)
for t in tabs:
    print(t)
