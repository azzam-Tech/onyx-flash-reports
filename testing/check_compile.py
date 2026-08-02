import sys
import traceback

app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    source = f.read()

try:
    compile(source, app_path, "exec")
    print("NO SYNTAX ERROR FOUND!")
except SyntaxError as e:
    print(f"SyntaxError at line {e.lineno}, col {e.offset}: {e.msg}")
    print("Line content:", e.text)
