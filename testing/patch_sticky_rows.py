import sys

app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make the table wrapper allow window-level sticky by removing overflow
old_tw = '.tw { overflow-x: auto; background: var(--card-bg); border-radius: 20px; box-shadow: var(--sh); padding: 10px; }'
new_tw = '.tw { overflow: visible; background: var(--card-bg); border-radius: 20px; box-shadow: var(--sh); padding: 10px; }'
content = content.replace(old_tw, new_tw)

# Make table headers sticky
old_th = 'thead th { white-space: nowrap; color: var(--ink); padding: 8px 12px; text-align: right; font-size: 13px; font-weight: 600; border-bottom: 2px solid var(--line);  }'
new_th = 'thead th { position: sticky; top: 0; z-index: 10; background: #ffffff; white-space: nowrap; color: var(--ink); padding: 8px 12px; text-align: right; font-size: 13px; font-weight: 600; border-bottom: 2px solid var(--line);  }'
content = content.replace(old_th, new_th)

# Make the totals row sticky
old_tot = 'tr.tot-row td { background: #e2e8f0 !important; color: #0f172a !important; font-weight: 800 !important; font-size: 14px !important; border-bottom: 2px solid #cbd5e1 !important; }'
new_tot = 'tr.tot-row td { position: sticky; top: 35px; z-index: 9; background: #e2e8f0 !important; color: #0f172a !important; font-weight: 800 !important; font-size: 14px !important; border-bottom: 2px solid #cbd5e1 !important; }'
content = content.replace(old_tot, new_tot)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Sticky rows applied.")
