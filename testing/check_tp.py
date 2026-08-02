with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

print("TARGETS_PAGE in app.py:", "TARGETS_PAGE =" in text)
