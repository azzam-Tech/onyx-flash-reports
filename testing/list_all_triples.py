app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

is_open = False
for i in range(2500):
    cnt = lines[i].count('"""')
    if cnt % 2 != 0:
        is_open = not is_open
        print(f"Line {i+1} (now open={is_open}): {lines[i].strip()[:70]}")
