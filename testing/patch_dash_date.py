import sys
import re

file_path = 'privet/onyx_reports/public/assets/index-Bw-_kdJV.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the exact pattern with backticks
pattern = r"\[([a-zA-Z0-9_]+),([a-zA-Z0-9_]+)\]=\(0,S\.useState\)\(new Date\(\)\.getFullYear\(\)\+`-01-01`\)"
match = re.search(pattern, content)

if match:
    replacement = f"[{match.group(1)},{match.group(2)}]=(0,S.useState)(new Date().getFullYear() + '-' + String(new Date().getMonth() + 1).padStart(2, '0') + '-01')"
    new_content = content.replace(match.group(0), replacement)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Dashboard JS Date Patched!")
else:
    print("Match not found, let's search just for the inner string")
    matches = re.findall(r".{0,30}new Date\(\)\.getFullYear\(\)\+`-01-01`.{0,30}", content)
    for m in matches:
        print("Found:", m)
