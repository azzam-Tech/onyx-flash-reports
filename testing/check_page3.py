import codecs
with codecs.open(r'privet\onyx_reports\app.py', 'r', 'utf-8') as f:
    text = f.read()

idx = text.find('PAGE = """')
idx2 = text.find('"""', idx + 10)
print(repr(text[idx2-100:idx2+10]))
