with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

in_triple = False
last_triple_line = -1

for idx, line in enumerate(lines, 1):
    count = line.count('"""')
    if count % 2 != 0:
        in_triple = not in_triple
        last_triple_line = idx
        print(f"Line {idx}: Triple quotes toggled -> in_triple = {in_triple}")

print(f"\nFinal in_triple status: {in_triple}. Last toggled at line {last_triple_line}")
