app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<form method="post" action="/settings">', '<form method="post">')

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)
