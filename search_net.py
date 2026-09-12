import os

search_dir = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\frontend\src"

for root, _, files in os.walk(search_dir):
    for f in files:
        if f.endswith(".tsx"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
                if "netSupplier" in content or "net_supplier" in content:
                    print(f"FOUND IN: {path}")
