import json, re

def get_main_tabs(path):
    t = open(path, 'r', encoding='utf-8', errors='ignore').read()
    m = re.search(r'TABS\s*=\s*(\[[\s\S]*?\]\s*)\nTABMAP', t)
    if not m: return []
    # parse Python literal using eval in safe scope
    try:
        # Simple extraction of main tab IDs
        return re.findall(r'\{\s*"id"\s*:\s*"([^"]+)"\s*,\s*"title"\s*:\s*"[^"]+"\s*,\s*"icon"', m.group(1))
    except Exception as e:
        return [str(e)]

print("Original OnyxDB main tabs:", get_main_tabs('c:/Users/amarn/OneDrive/Desktop/onyxdb/privet/onyx_reports/app.py'))
print("Current App main tabs:", get_main_tabs('privet/onyx_reports/app.py'))
