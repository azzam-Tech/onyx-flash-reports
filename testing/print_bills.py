import re
content = open(r'C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py', encoding='utf-8').read()
m = re.search(r'(\{"id":"bills".*?"sql":""")(.*?)(\"""\})', content, flags=re.DOTALL)
if m: print(m.group(2))
