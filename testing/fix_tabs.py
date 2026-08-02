import re
import codecs
import json

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

# First, fix the mangled find_report
bad_injection_regex = r'return t, t\["reports"\]\[0,\s*\{\s*"id": "global_vars".*?\]\s*\}\s*\]'
if re.search(bad_injection_regex, content, re.DOTALL):
    content = re.sub(bad_injection_regex, 'return t, t["reports"][0]', content, flags=re.DOTALL)
else:
    print("WARNING: Bad injection not found. Maybe it's already fixed or regex doesn't match.")

# Second, safely append to TABS
new_tab = """    {
        "id": "global_vars",
        "title": "تقارير عامة",
        "icon": '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M19 4h-14a2 2 0 0 0 -2 2v12a2 2 0 0 0 2 2h14a2 2 0 0 0 2 -2v-12a2 2 0 0 0 -2 -2z" /><path d="M16 8v8" /><path d="M12 8v8" /><path d="M8 8v8" /><path d="M4 12h16" />',
        "reports": [
            {
                "id": "targets_ui",
                "title": "تارقت المناديب",
                "sql": "SELECT 1 FROM DUAL",
                "params": [],
                "cols": ["Dummy"]
            }
        ]
    }
]"""

# Find the end of TABS
if '"id": "global_vars"' not in content[:content.find("TABMAP =")]:
    content = content.replace(" ]},\n]", " ]},\n" + new_tab)
else:
    print("global_vars already in TABS")

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)
print("SUCCESS")
