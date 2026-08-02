with open(r'C:\Users\amarn\OneDrive\Desktop\onyxdb\privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text1 = f.read()

with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text2 = f.read()

import re
def get_tabs(t):
    m = re.search(r'TABS\s*=\s*\[(.*?)\]\s*TABMAP', t, re.DOTALL)
    if not m: return []
    return re.findall(r'\"id\"\s*:\s*\"([^\"]+)\"', m.group(1))

print("Initial onyxdb tabs:", get_tabs(text1))
print("Current app tabs:", get_tabs(text2))
