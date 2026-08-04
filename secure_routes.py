with open('privet/onyx_reports/app.py', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '@app.route("/settings", methods=["GET","POST"])\ndef settings():',
    '@app.route("/settings", methods=["GET","POST"])\ndef settings():\n    if session.get("role") != "admin": return "لا تملك صلاحية", 403'
)

content = content.replace(
    '@app.route("/globals", methods=["GET","POST"])\ndef globals_page():',
    '@app.route("/globals", methods=["GET","POST"])\ndef globals_page():\n    if session.get("role") != "admin": return "لا تملك صلاحية", 403'
)

with open('privet/onyx_reports/app.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Secured backend routes")
