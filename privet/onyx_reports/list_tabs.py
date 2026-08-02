import re, ast

with open('app.py', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'TABS\s*=\s*(\[.*?\])\n[a-zA-Z_]', text, re.DOTALL)
if match:
    tabs_str = match.group(1)
    try:
        tabs = ast.literal_eval(tabs_str)
        for t in tabs:
            print(f"Tab: {t.get('id')} - {t.get('title')}")
            if 'reports' in t:
                for r in t['reports']:
                    print(f"  Report: {r.get('id')} - {r.get('title')}")
    except Exception as e:
        print('Error parsing TABS:', e)
        print(tabs_str[:200])
