import codecs
with codecs.open(r'privet\onyx_reports\app.py', 'r', 'utf-8') as f:
    text = f.read()

idx = text.find('"global_vars"')
print(text[idx-50:idx+400])
