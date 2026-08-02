import sys

app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

css_lines = [
    ".quick-dates { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 30px; align-items: center; justify-content: center; }\n",
    ".quick-dates .btn-sm { background: #ffffff; border: 2px solid #e2e8f0; color: var(--ink-dark); padding: 14px 28px; border-radius: 16px; font-size: 16px; font-weight: 800; cursor: pointer; transition: all 0.25s ease; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03); }\n",
    ".quick-dates .btn-sm:hover { border-color: var(--primary); color: var(--primary); transform: translateY(-3px); box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.15), 0 4px 6px -2px rgba(79, 70, 229, 0.05); background: #fefeff; }\n",
    ".quick-dates .btn-sm:active, .quick-dates .btn-sm.active { background: var(--primary); border-color: var(--primary); color: #ffffff; transform: translateY(-1px); box-shadow: 0 6px 12px -2px rgba(79, 70, 229, 0.4); }\n"
]

# Remove from LOGIN_PAGE
for c in css_lines:
    content = content.replace(c, "")

# Append to STYLE block
target = "STYLE = \"\"\"<style>\n"
if target in content:
    # Just append it right after STYLE = \"\"\"<style>
    insert_str = "".join(css_lines)
    content = content.replace(target, target + insert_str)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS moved to STYLE block successfully.")
