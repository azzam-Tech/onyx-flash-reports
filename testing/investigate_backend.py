import re
import sys

# Windows console encoding fix
sys.stdout.reconfigure(encoding='utf-8')

with open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

def print_around(match, context=500):
    start = max(0, match.start() - context)
    end = min(len(content), match.end() + context)
    print(f"--- MATCH ---")
    print(content[start:end])

# Look at how params are evaluated in python
m_app_route = re.search(r'def index\(\):', content)
if m_app_route:
    print_around(m_app_route, 1500)

