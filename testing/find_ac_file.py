import os
from datetime import datetime

downloads_dir = r"C:\Users\amarn\Downloads"
files = []
for f in os.listdir(downloads_dir):
    if f.endswith('.xlsx') and not f.startswith('~$'):
        full_path = os.path.join(downloads_dir, f)
        mtime = os.path.getmtime(full_path)
        files.append((f, mtime))

# Sort by most recently modified
files.sort(key=lambda x: x[1], reverse=True)
print("Latest Excel files in Downloads:")
for f, mtime in files[:5]:
    # Use ascii encoding to avoid windows console crash with Arabic, just encode/decode safely
    print(f"{f.encode('utf-8', 'replace').decode('utf-8')}")
