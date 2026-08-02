app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "rb") as f:
    lines = f.readlines()

for i in range(2498, 2515):
    print(f"Line {i+1}: {repr(lines[i])}")
