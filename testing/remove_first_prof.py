app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Line 908 is `  ]},` for vat tab.
# Line 909 is `  {"id":"prof",...` (first duplicate)
# Line 1012 is `   {"id":"prof",...` (second real prof tab)

new_lines = lines[:908] + lines[1011:]

with open(app_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("REMOVED DUPLICATE PROF TAB SUCCESSFULLY!")
