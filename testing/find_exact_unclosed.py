app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for N in range(1, len(lines)+1):
    chunk = "".join(lines[:N])
    try:
        compile(chunk, "<string>", "exec")
    except SyntaxError as e:
        msg = str(e)
        if "unexpected EOF" not in msg and "unterminated" not in msg and "was never closed" not in msg:
            print(f"Line {N} triggered real error: {e}")
            print(f"Line {N} content: {lines[N-1].strip()}")
            break
