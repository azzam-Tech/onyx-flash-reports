import os
import sys

search_str = "مرتبط"
search_dir = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\frontend\src"

for root, _, files in os.walk(search_dir):
    for f in files:
        if f.endswith(".tsx") or f.endswith(".ts") or f.endswith(".js"):
            path = os.path.join(root, f)
            try:
                with open(path, "r", encoding="utf-8") as file:
                    content = file.read()
                    if search_str in content:
                        print(f"FOUND IN: {path}")
            except Exception as e:
                pass
