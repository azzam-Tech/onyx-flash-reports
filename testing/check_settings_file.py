import json, os

with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('SETTINGS_FILE =')
print(text[idx:idx+150])

# Also check settings.json
if os.path.exists(r'privet\onyx_reports\settings.json'):
    with open(r'privet\onyx_reports\settings.json', 'r', encoding='utf-8') as f:
        print("settings.json content:", json.load(f))
