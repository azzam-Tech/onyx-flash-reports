import codecs
with codecs.open(r'privet\onyx_reports\app.py', 'r', 'utf-8') as f:
    text = f.read()

idx = text.find('<div class="cnt">عدد الصفوف: {{rows|length}}</div>')
print(repr(text[idx:idx+500]))
