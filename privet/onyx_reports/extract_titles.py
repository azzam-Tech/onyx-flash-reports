import re

with open('app.py', 'r', encoding='utf-8') as f:
    text = f.read()

titles = re.findall(r'\"title\"\:\"(.*?)\"', text)
print(titles[:30])
