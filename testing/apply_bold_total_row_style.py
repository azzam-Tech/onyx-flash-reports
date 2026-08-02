app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add CSS style rule for tr.tot-row td
css_target = "tbody tr:hover td { background: #f8fafc; }"
css_replacement = """tbody tr:hover td { background: #f8fafc; }
tr.tot-row td { background: #e2e8f0 !important; color: #0f172a !important; font-weight: 800 !important; font-size: 14px !important; border-bottom: 2px solid #cbd5e1 !important; }"""

if css_target in content:
    content = content.replace(css_target, css_replacement)
    print("Added CSS rule for tr.tot-row td!")

# 2. Update tbody rendering in Jinja template
tbody_target = "<tbody>{% for row in rows %}<tr>{% for cell in row %}<td>{{ '' if cell is none else cell }}</td>{% endfor %}</tr>{% endfor %}</tbody>"
tbody_replacement = "<tbody>{% for row in rows %}<tr class=\"{{ 'tot-row' if (loop.first and (row[0]=='الإجمالي' or row[1]=='الإجمالي')) else '' }}\">{% for cell in row %}<td>{{ '' if cell is none else cell }}</td>{% endfor %}</tr>{% endfor %}</tbody>"

if tbody_target in content:
    content = content.replace(tbody_target, tbody_replacement)
    print("Updated Jinja template for total row styling!")

with open(app_path, "w", encoding="utf-8") as f:
    f.write(content)

print("COMPLETED TOTAL ROW STYLING IN APP.PY SUCCESSFULLY!")
