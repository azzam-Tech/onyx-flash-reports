import sys

app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_sb = '.sb { width: 260px; background: var(--sb-bg); border-radius: 24px; display: flex; flex-direction: column; padding: 30px 20px; flex-shrink: 0; box-shadow: var(--sh); }'
new_sb = '.sb { width: 260px; background: var(--sb-bg); border-radius: 24px; display: flex; flex-direction: column; padding: 30px 20px; flex-shrink: 0; box-shadow: var(--sh); position: sticky; top: 20px; max-height: calc(100vh - 40px); overflow-y: auto; }'
content = content.replace(old_sb, new_sb)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Sidebar made sticky.")
