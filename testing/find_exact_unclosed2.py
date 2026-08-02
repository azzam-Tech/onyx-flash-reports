app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

in_triple = False
start_l = 0

for i, l in enumerate(lines, 1):
    count = l.count('"""')
    if count == 1:
        if not in_triple:
            in_triple = True
            start_l = i
        else:
            in_triple = False
            start_l = 0
    elif count == 3:
        if not in_triple:
            in_triple = True
            start_l = i
        else:
            in_triple = False
            start_l = 0

    if i == 2500:
        print(f"At line 2500: in_triple={in_triple}, start_l={start_l}")
