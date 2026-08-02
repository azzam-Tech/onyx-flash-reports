with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("targets_ui")
while idx != -1:
    print("MATCH AT:", idx)
    print(text[idx-100:idx+200])
    print("="*40)
    idx = text.find("targets_ui", idx+1)
