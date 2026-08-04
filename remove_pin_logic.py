with open('privet/onyx_reports/app.py', encoding='utf-8') as f:
    content = f.read()

import re

pin_logic = re.compile(r'    if not session\.get\("set_ok"\):\n        if request\.method == "POST" and request\.form\.get\("pin"\) is not None:\n            if request\.form\.get\("pin"\) == SETTINGS_PIN:\n                session\["set_ok"\] = True\n            else:\n                return render_template\("pin\.html", error=True\)\n        else:\n            return render_template\("pin\.html", error=False\)')

content = re.sub(pin_logic, '', content)

with open('privet/onyx_reports/app.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Removed PIN logic")
