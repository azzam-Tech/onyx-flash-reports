import os
import sys

search_str = "عميل مرتبط بمورد"
search_dir = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports"

for root, _, files in os.walk(search_dir):
    for f in files:
        if f.endswith(".js") or f.endswith(".html") or f.endswith(".py"):
            path = os.path.join(root, f)
            try:
                with open(path, "r", encoding="utf-8") as file:
                    content = file.read()
                    if search_str in content:
                        print(f"FOUND IN: {path}")
            except Exception as e:
                pass
