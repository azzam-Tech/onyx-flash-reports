import sys

app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_css1 = ".quick-dates { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 24px; align-items: center; }"
old_css2 = ".quick-dates .btn-sm { background: #ffffff; border: 1px solid #e2e8f0; color: var(--ink-dark); padding: 10px 20px; border-radius: 12px; font-size: 14px; font-weight: 700; cursor: pointer; transition: all 0.3s ease; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }"
old_css3 = ".quick-dates .btn-sm:hover { background: #f8fafc; border-color: #cbd5e1; transform: translateY(-2px); box-shadow: 0 6px 12px rgba(0,0,0,0.05); color: var(--primary); }"
old_css4 = ".quick-dates .btn-sm:active, .quick-dates .btn-sm.active { background: var(--primary); border-color: var(--primary); color: #ffffff; transform: translateY(0); box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2); }"

new_css1 = ".quick-dates { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 30px; align-items: center; justify-content: center; }"
new_css2 = ".quick-dates .btn-sm { background: #ffffff; border: 2px solid #e2e8f0; color: var(--ink-dark); padding: 14px 28px; border-radius: 16px; font-size: 16px; font-weight: 800; cursor: pointer; transition: all 0.25s ease; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03); }"
new_css3 = ".quick-dates .btn-sm:hover { border-color: var(--primary); color: var(--primary); transform: translateY(-3px); box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.15), 0 4px 6px -2px rgba(79, 70, 229, 0.05); background: #fefeff; }"
new_css4 = ".quick-dates .btn-sm:active, .quick-dates .btn-sm.active { background: var(--primary); border-color: var(--primary); color: #ffffff; transform: translateY(-1px); box-shadow: 0 6px 12px -2px rgba(79, 70, 229, 0.4); }"

content = content.replace(old_css1, new_css1)
content = content.replace(old_css2, new_css2)
content = content.replace(old_css3, new_css3)
content = content.replace(old_css4, new_css4)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Bold, large, and premium CSS applied.")
