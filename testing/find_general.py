with open('privet/onyx_reports/reports_config.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '"id":"general"' in l:
        print(i+1, l[:80])
