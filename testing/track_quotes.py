app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(1, 2501):
    sub_source = "".join(lines[:i])
    try:
        compile(sub_source, "<string>", "exec")
    except SyntaxError as e:
        if "unexpected EOF" not in str(e):
            print(f"Line {i} syntax error: {e}")

print("Done checking partial compilation.")
