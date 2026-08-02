import codecs
import re

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

# 1. Rename tab
content = content.replace('"id": "global_vars",\n        "title": "تقارير عامة",', '"id": "global_vars",\n        "title": "المتغيرات العامة",')

# 2. Add custom_route to targets_ui
targets_ui_str = """                "title": "تارقت المناديب",
                "sql": "SELECT 1 FROM DUAL",
                "params": [],
                "cols": ["Dummy"]"""

targets_ui_new = """                "title": "تارقت المناديب",
                "custom_route": "/targets_ui",
                "sql": "SELECT 1 FROM DUAL",
                "params": [],
                "cols": ["Dummy"]"""

content = content.replace(targets_ui_str, targets_ui_new)

# 3. Set default target to 1,000,000
js_old = "let val = smData[m] || 0;"
js_new = "let val = smData[m] !== undefined ? smData[m] : 1000000;"
content = content.replace(js_old, js_new)

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)
print("SUCCESS")
