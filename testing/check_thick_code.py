with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('init_oracle_client')
print(text[idx-50:idx+250])
