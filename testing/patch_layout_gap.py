import sys
import re

app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .quick-dates CSS to use better margins for flexbox context
old_css = '.quick-dates { display: flex; gap: 12px; flex-wrap: wrap; margin-top: -10px; margin-bottom: 12px; align-items: center; justify-content: center; }'
new_css = '.quick-dates { display: flex; gap: 12px; flex-wrap: wrap; margin-top: -12px; margin-bottom: -8px; align-items: center; justify-content: center; }'
content = content.replace(old_css, new_css)

# Also remove margin-bottom on filters so it doesn't compound with the gap
old_filters = '.filters { background: var(--card-bg); border-radius: 20px; padding: 24px; display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 20px; align-items: end; box-shadow: var(--sh); margin-bottom: 24px; }'
new_filters = '.filters { background: var(--card-bg); border-radius: 20px; padding: 24px; display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 20px; align-items: end; box-shadow: var(--sh); margin-bottom: 0; }'
content = content.replace(old_filters, new_filters)

# 2. Remove the row count text entirely
# The regex looks for `<div class="cnt">...</div>`
cnt_pattern = re.compile(r'\s*<div class="cnt">.*?</div>')
content = cnt_pattern.sub('', content)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed .cnt and optimized margins.")
