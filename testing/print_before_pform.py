import re

with open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\rdf_strings.txt", 'r', encoding='utf-8') as f:
    content = f.read()
    
# Extract the BeforePForm function entirely
match = re.search(r'function BeforePForm return boolean is.*?end;', content, re.IGNORECASE | re.DOTALL)
if match:
    print(match.group(0)[:10000]) # print up to 10000 chars
else:
    print("Not found")
