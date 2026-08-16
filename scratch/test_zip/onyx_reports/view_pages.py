import re

with open('app.py', 'r', encoding='utf-8') as f:
    text = f.read()

print('PRINT_PAGE start:')
match = re.search(r'PRINT_PAGE\s*=\s*\"\"\"(.*?)\"\"\"', text, re.DOTALL)
if match:
    print(match.group(1)[:200])

print('\nSETTINGS_PAGE start:')
match2 = re.search(r'SETTINGS_PAGE\s*=\s*\"\"\"(.*?)\"\"\"', text, re.DOTALL)
if match2:
    print(match2.group(1)[:200])
