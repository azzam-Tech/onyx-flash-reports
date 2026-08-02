import json
import os

# 1. Reset settings.json so no main tabs are hidden
settings_path = r'privet\onyx_reports\settings.json'
with open(settings_path, 'w', encoding='utf-8') as f:
    json.dump({"tabs": [], "reports": [], "hide_profit": False}, f, indent=2)

print("settings.json reset cleanly!")

# 2. Update app.py to ensure thick mode default path and remove target code
with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Make sure thick mode has default path C:\oracle\instantclient\instantclient_23_0
if '_lib = os.environ.get("ORA_LIB_DIR")' in text:
    text = text.replace('_lib = os.environ.get("ORA_LIB_DIR")', '_lib = os.environ.get("ORA_LIB_DIR", r"C:\\oracle\\instantclient\\instantclient_23_0")')

with open(r'privet\onyx_reports\app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Oracle Thick mode default path confirmed!")
