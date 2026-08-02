import json, os

path = r'privet\onyx_reports\hidden.json'
if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f:
        print("hidden.json content:", json.load(f))
else:
    print("hidden.json does not exist")
