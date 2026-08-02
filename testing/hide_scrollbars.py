import sys

app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

hide_scrollbars_css = """
/* Hide scrollbars completely while keeping scroll functionality */
::-webkit-scrollbar { display: none; }
* { -ms-overflow-style: none; scrollbar-width: none; }
"""

# Insert right after <style> tag in STYLE
target = 'STYLE = """<style>\n'
if target in content:
    content = content.replace(target, target + hide_scrollbars_css)
else:
    print("Could not find STYLE target.")
    sys.exit(1)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Scrollbars hidden.")
