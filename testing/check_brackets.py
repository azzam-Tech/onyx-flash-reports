app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

stack = []

for i in range(908, 1332):
    line = lines[i]
    for char in line:
        if char in '{[':
            stack.append((char, i+1))
        elif char in '}]':
            if not stack:
                print(f"Line {i+1}: Unmatched closing '{char}'")
            else:
                top, top_line = stack.pop()
                if (top == '{' and char != '}') or (top == '[' and char != ']'):
                    print(f"Line {i+1}: Mismatched closing '{char}' for opening '{top}' at line {top_line}")

print(f"Remaining unclosed in stack: {stack}")
