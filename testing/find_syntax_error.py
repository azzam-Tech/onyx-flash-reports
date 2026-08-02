app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

in_triple = False
triple_start_line = 0

for i, l in enumerate(lines, 1):
    cnt = l.count('"""')
    if cnt == 1:
        if not in_triple:
            in_triple = True
            triple_start_line = i
        else:
            in_triple = False
    elif cnt == 2:
        pass # open and close on same line
    elif cnt > 2:
        print(f"Line {i} has >2 triple quotes: {l}")

if in_triple:
    print(f"TRIPLE QUOTE UNCLOSED! Started at line {triple_start_line}: {lines[triple_start_line-1].strip()[:80]}")
else:
    print("All triple quotes are properly balanced!")
