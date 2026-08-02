import sys

app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_css1 = ".quick-dates { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 24px; justify-content: center; background: var(--card-bg); padding: 16px; border-radius: 20px; box-shadow: var(--sh); }"
old_css2 = ".quick-dates .btn-sm { background: #f8fafc; border: 1px solid var(--line); color: var(--ink-dark); padding: 8px 16px; border-radius: 12px; font-size: 13px; font-weight: 700; cursor: pointer; transition: 0.2s; }"
old_css3 = ".quick-dates .btn-sm:hover { background: var(--primary); border-color: var(--primary); color: #fff; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(79,70,229,0.2); }"

new_css1 = ".quick-dates { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 24px; justify-content: flex-start; align-items: center; background: transparent; padding: 0; box-shadow: none; border-radius: 0; }"
new_css2 = ".quick-dates .btn-sm { background: rgba(79, 70, 229, 0.08); border: 1px solid rgba(79, 70, 229, 0.1); color: var(--primary); padding: 10px 18px; border-radius: 100px; font-size: 13px; font-weight: 700; cursor: pointer; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }"
new_css3 = ".quick-dates .btn-sm:hover { background: var(--primary); border-color: var(--primary); color: #fff; transform: translateY(-3px) scale(1.02); box-shadow: 0 8px 16px rgba(79, 70, 229, 0.25); }"

content = content.replace(old_css1, new_css1)
content = content.replace(old_css2, new_css2)
content = content.replace(old_css3, new_css3)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Quick Date CSS replaced successfully.")
