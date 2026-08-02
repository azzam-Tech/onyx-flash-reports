with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('TARGETS_PAGE =')
print(text[idx:idx+1200])
