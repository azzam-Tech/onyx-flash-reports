import sys
import re

app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove FETCH FIRST n ROWS ONLY
content = re.sub(r'\s*FETCH FIRST \d+ ROWS ONLY', '', content, flags=re.IGNORECASE)

# Remove WHERE ROWNUM <= n
content = re.sub(r'WHERE ROWNUM\s*<=\s*\d+', '', content, flags=re.IGNORECASE)

# Remove python slice rows[:300]
content = content.replace('rows[:300]', 'rows')

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("All limits removed.")
