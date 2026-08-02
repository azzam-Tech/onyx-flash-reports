import re
with open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

res = re.findall(r'([A-Z_]+)\s*=\s*"""<(?:!DOCTYPE|html)', content)
print(res)

for match in re.finditer(r'([A-Za-z_]+)\s*=\s*"""(.*?)"""', content, re.DOTALL):
    var_name = match.group(1)
    body = match.group(2)
    if '<html' in body or '<!DOCTYPE' in body:
        print(f"Found HTML in variable: {var_name}")
