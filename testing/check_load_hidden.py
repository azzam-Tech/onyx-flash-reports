with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('def load_hidden():')
print(text[idx:idx+400])
