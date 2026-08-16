import re

with open('privet/onyx_reports/templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
    
scripts = re.findall(r'<script src="([^"]+)"', content)
print("Scripts:")
for s in scripts:
    print(s)
    
styles = re.findall(r'<link rel="stylesheet" href="([^"]+)"', content)
print("\nStyles:")
for s in styles:
    print(s)
