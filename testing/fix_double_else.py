import re

with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace {% else %}\s*{% else %} with {% else %}
text = re.sub(r'\{%\s*else\s*%\}\s*\{%\s*else\s*%\}', '{% else %}', text)

with open(r'privet\onyx_reports\app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Double else removed successfully!")
