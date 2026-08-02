import codecs
with codecs.open(r'privet\onyx_reports\app.py', 'r', 'utf-8') as f:
    text = f.read()

idx = text.find('PAGE = """')
idx2 = text.find('"""\n\n@app', idx)
page = text[idx:idx2]
print(repr(page[-500:]))
