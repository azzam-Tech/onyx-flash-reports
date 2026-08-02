import json
import codecs
import re

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

idx = content.find('"id":"collection_adopted"')
start = content.rfind('{', 0, idx)
end = content.find('"""}', idx)
print(content[idx:end+4])
