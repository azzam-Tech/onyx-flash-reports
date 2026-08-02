with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(''.join(lines[75:105]))
