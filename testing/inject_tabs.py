import re
import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

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

content = re.sub(r'\]\s*(?=\n(?:PAGE|LOGIN_PAGE|PRINT_PAGE|def|@))', ',\n' + new_tab, content, count=1)

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)
print("SUCCESS")
