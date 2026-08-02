import codecs
with codecs.open(r'privet\onyx_reports\app.py', 'r', 'utf-8') as f:
    text = f.read()

idx = text.find('PAGE = """')
idx2 = text.find('"""', idx + 10)
page = text[idx:idx2]
print(page[-2000:])
