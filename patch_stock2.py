import re

file_path = 'privet/onyx_reports/reports_config.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the params list dynamically using regex
pattern = r'(\{"id":"stock_bal",.*?\[.*?\])(\},"sql":)'

# We will inject the new param right before the closing bracket of the params list.
# The param list ends with ]}, "sql"
# So let's match the closing `]}` for stock_bal params
def replacer(match):
    # match.group(1) is everything from {"id":"stock_bal" to the closing ] of the params list
    old_prefix = match.group(1)
    
    # insert the new param right before the closing ]
    new_prefix = old_prefix[:-1] + ',{"name":"i_code","label":"رقم الصنف (اختياري)","type":"text","default":""}]'
    return new_prefix + match.group(2)

content = re.sub(pattern, replacer, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("regex patched successfully!")
