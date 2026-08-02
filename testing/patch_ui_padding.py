import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

# Replace STYLE padding for the main UI
content = content.replace(
    "thead th { color: var(--ink); padding: 16px; text-align: right; font-size: 13px; font-weight: 600; border-bottom: 2px solid var(--line); white-space: nowrap; }",
    "thead th { color: var(--ink); padding: 8px 12px; text-align: right; font-size: 13px; font-weight: 600; border-bottom: 2px solid var(--line); white-space: nowrap; }"
)

content = content.replace(
    "tbody td { padding: 16px; border-bottom: 1px solid var(--line); font-size: 14px; font-weight: 500; color: var(--ink-dark); white-space: nowrap; transition: 0.2s; }",
    "tbody td { padding: 6px 12px; border-bottom: 1px solid var(--line); font-size: 13px; font-weight: 500; color: var(--ink-dark); white-space: nowrap; transition: 0.2s; }"
)

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)

print("UI CSS Padding updated!")
