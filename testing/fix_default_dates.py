import sys

app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_1 = '    display = {p["name"]: request.args.get(p["name"], p.get("default","")) for p in rpt["params"]}'
new_1 = '    display = {p["name"]: request.args.get(p["name"]) or (p["get_default"]() if "get_default" in p else p.get("default","")) for p in rpt["params"]}'

old_2 = '    for p in rpt["params"]: qsp[p["name"]] = request.args.get(p["name"], p.get("default",""))'
new_2 = '    for p in rpt["params"]: qsp[p["name"]] = request.args.get(p["name"]) or (p["get_default"]() if "get_default" in p else p.get("default",""))'

content = content.replace(old_1, new_1)
content = content.replace(old_2, new_2)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Default values fixed.")
