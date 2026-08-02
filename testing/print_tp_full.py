with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('TARGETS_PAGE =')
idx2 = text.find('"""\n\nfrom flask', idx1)
print(text[idx1:idx2])
