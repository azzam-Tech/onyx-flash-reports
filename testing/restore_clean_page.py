import re

with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Find the inline block in PAGE starting from `<style>\n         .tw i` up to `{% else %}\n       <div class="cnt">`
# and replace it with simple `<div class="cnt">`

text = re.sub(
    r'\n\s*<style>\s*\.tw input\[type=number\][\s\S]*?</script>\s*\{%\s*else\s*%\}',
    '',
    text
)

with open(r'privet\onyx_reports\app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Inline block cleanly removed from PAGE!")
