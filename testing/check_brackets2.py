import tokenize

app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "rb") as f:
    tokens = tokenize.tokenize(f.readline)
    stack = []
    try:
        for tok in tokens:
            if tok.type == tokenize.OP:
                if tok.string in '{[':
                    stack.append((tok.string, tok.start[0]))
                elif tok.string in '}]':
                    if not stack:
                        print(f"Line {tok.start[0]}: Unmatched closing '{tok.string}'")
                    else:
                        top, top_line = stack.pop()
                        if (top == '{' and tok.string != '}') or (top == '[' and tok.string != ']'):
                            print(f"Line {tok.start[0]}: Mismatched closing '{tok.string}' for '{top}' at line {top_line}")
    except Exception as e:
        print("Error at token:", e)

print("Remaining stack:", stack)
