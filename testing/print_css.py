import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

idx = content.find('STYLE =')
end_idx = content.find('"""', idx + 10)
style_block = content[idx:end_idx+3]

for line in style_block.split('\n'):
    if 'table' in line or 'th' in line or 'td' in line:
        print(line)
