import re
with open('privet/onyx_reports/reports_config.py', 'r', encoding='utf-8') as f:
    text = f.read()

if 'ASOF =' not in text:
    text = text.replace('DTO   = {"name":"date_to"', 'ASOF  = {"name":"as_of","label":"حتى تاريخ","type":"date","get_default": get_default_date_to}\nDTO   = {"name":"date_to"')

text = text.replace('{"name":"as_of","label":"حتى تاريخ","type":"date","default":"2026-07-31"}', 'ASOF')
text = text.replace('{"name":"as_of","label":"إلى تاريخ","type":"date","default":"2026-07-31"}', 'ASOF')

with open('privet/onyx_reports/reports_config.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("reports_config.py fixed!")
