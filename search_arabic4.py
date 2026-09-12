import os
import sys

search_str = "مرتبط"
search_dir = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity"

for root, _, files in os.walk(search_dir):
    if '.git' in root or 'node_modules' in root or '.venv' in root: continue
    for f in files:
        path = os.path.join(root, f)
        try:
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
                if search_str in content:
                    print(f"FOUND IN: {path}")
        except Exception as e:
            pass
