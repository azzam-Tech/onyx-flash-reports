import tokenize
from io import BytesIO

app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "rb") as f:
    tokens = tokenize.tokenize(f.readline)
    try:
        for tok in tokens:
            if tok.start[0] >= 2500:
                print(f"Line {tok.start[0]}:{tok.start[1]} Token {tokenize.tok_name[tok.type]} -> {repr(tok.string)}")
    except tokenize.TokenError as e:
        print(f"TokenError: {e}")
