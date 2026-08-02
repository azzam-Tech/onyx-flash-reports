import sys

app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'
with open(app_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
in_route = False
for i, line in enumerate(lines):
    if '@app.route("/")' in line:
        in_route = True
    if in_route:
        print(i+1, repr(line))
        if 'return render_template_string' in line:
            break
