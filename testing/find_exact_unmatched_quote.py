app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

in_str = False
start_line = 0

for i, line in enumerate(lines, 1):
    pos = 0
    while True:
        pos = line.find('"""', pos)
        if pos == -1:
            break
        pos += 3
        if not in_str:
            in_str = True
            start_line = i
            # print(f"Line {i} OPENED string: {line.strip()[:60]}")
        else:
            in_str = False
            # print(f"Line {i} CLOSED string")
    if i == 2500:
        print(f"Line 2500 state: in_str={in_str}, start_line={start_line}")
