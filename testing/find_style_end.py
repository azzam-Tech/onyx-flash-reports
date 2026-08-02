app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(2499, 2600):
    if '"""' in lines[i]:
        print(f"Line {i+1}: {lines[i].strip()}")
