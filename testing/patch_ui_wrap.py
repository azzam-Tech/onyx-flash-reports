import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

idx = content.find('STYLE =')
end_idx = content.find('"""', idx + 10)
style_block = content[idx:end_idx+3]

# Restore nowrap
if 'th, td { padding: 5px 8px;' in style_block:
    new_style_block = style_block.replace('th, td { padding: 5px 8px;', 'th, td { padding: 5px 8px; white-space: nowrap;')
else:
    new_style_block = style_block.replace('th, td {', 'th, td { white-space: nowrap;')

# Restore min-width: 600px;
if 'min-width: 100%;' in new_style_block:
    new_style_block = new_style_block.replace('min-width: 100%;', 'min-width: 600px;')

content = content.replace(style_block, new_style_block)

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)

print("Restored UI wrap and min-width")
