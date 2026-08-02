with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = "{% endif %}\n     {% endif %}\n     {% endif %}\n   </div>"
replacement = "{% endif %}\n     {% endif %}\n   </div>"

if target in text:
    text = text.replace(target, replacement)
    with open(r'privet\onyx_reports\app.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Extra endif successfully removed!")
else:
    print("Target not found, checking...")
