import codecs
import re

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", 'r', 'utf-8') as f:
    content = f.read()

for match in re.finditer(r'(.{0,50}DOC_TYPE=2.{0,100})', content):
    if 'def run_' not in match.group(1) and 'def ' not in match.group(1):
        print(match.group(1).strip())
