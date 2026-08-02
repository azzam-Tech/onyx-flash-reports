import re

with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove `global_vars` from TABS
content = re.sub(r',\s*\{\s*"id":\s*"global_vars"[\s\S]*?\n\s*\}', '', content)
content = re.sub(r'\{\s*"id":\s*"global_vars"[\s\S]*?\n\s*\}', '', content)

# 2. Remove TARGETS_PAGE
content = re.sub(r'TARGETS_PAGE\s*=\s*"""[\s\S]*?"""', '', content)

# 3. Remove routes and functions related to targets
content = re.sub(r'TARGETS_FILE\s*=[\s\S]*?@app\.route\("/targets_ui"\)[\s\S]*?def save_targets\(\):[\s\S]*?return jsonify\(\{.*?\}\)\n', '', content)
content = re.sub(r'@app\.route\("/targets_ui"\)[\s\S]*?def save_targets\(\):[\s\S]*?return jsonify\(\{.*?\}\)\n', '', content)

# 4. Remove any leftover targets references in index or PAGE
content = content.replace('Environment().from_string(app.TARGETS_PAGE);', '')

with open(r'privet\onyx_reports\app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Targets feature cleanly removed from app.py!")
