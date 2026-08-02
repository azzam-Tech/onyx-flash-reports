with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '_lib = os.environ.get("ORA_LIB_DIR")'
replacement = '_lib = os.environ.get("ORA_LIB_DIR", r"C:\\oracle\\instantclient\\instantclient_23_0")'

if target in text:
    text = text.replace(target, replacement)
    with open(r'privet\onyx_reports\app.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Thick mode client path default added successfully!")
else:
    print("Target not found, checking...")
