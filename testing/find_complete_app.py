import os
import glob
import re

def check_file(path):
    if not os.path.exists(path): return 0, []
    t = open(path, 'r', encoding='utf-8', errors='ignore').read()
    m = re.search(r'TABS\s*=\s*\[(.*?)\]\s*TABMAP', t, re.DOTALL)
    if not m: return len(t), []
    main_tabs = re.findall(r'\{\s*\"id\"\s*:\s*\"([^\"]+)\"\s*,\s*\"title\"', m.group(1))
    return len(t), main_tabs

for p in ['privet/onyx_reports/app.py', 'testing/recovered_app.py', 'testing/app_rebuild.py', 'testing/app_rebuild2.py', 'testing/app_rebuild3.py', 'c:/Users/amarn/OneDrive/Desktop/onyxdb/privet/onyx_reports/app.py']:
    sz, mt = check_file(p)
    print(p, "Size:", sz, "Main Tabs:", mt)
