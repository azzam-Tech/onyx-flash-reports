with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

print("global_vars in app.py:", "global_vars" in text)
print("targets_ui in app.py:", "targets_ui" in text)
print("TARGETS_PAGE in app.py:", "TARGETS_PAGE" in text)
