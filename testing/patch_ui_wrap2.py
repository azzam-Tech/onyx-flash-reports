import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

idx = content.find('STYLE =')
end_idx = content.find('"""', idx + 10)
style_block = content[idx:end_idx+3]

# Remove word-wrap from UI table
new_style_block = style_block.replace('word-wrap: break-word; word-break: break-word;', '')

# Add nowrap to thead th and tbody td
if 'thead th {' in new_style_block and 'white-space' not in new_style_block.split('thead th {')[1].split('}')[0]:
    new_style_block = new_style_block.replace('thead th {', 'thead th { white-space: nowrap;')

if 'tbody td {' in new_style_block and 'white-space' not in new_style_block.split('tbody td {')[1].split('}')[0]:
    new_style_block = new_style_block.replace('tbody td {', 'tbody td { white-space: nowrap;')

# Also check table width if it needs min-width. We'll leave it width: 100% since we wrap the table in .tw which has overflow-x auto.
# Actually, the user says "جعلتها ملى الشاشة" -> "made it full screen". 
# The UI table used to have `min-width: 600px;` but width 100% is fine as long as there is white-space: nowrap so it expands naturally.

content = content.replace(style_block, new_style_block)

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)

print("Properly restored UI wrap")
