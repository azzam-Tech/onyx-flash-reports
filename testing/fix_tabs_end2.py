with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('TABMAP = {t["id"]: t for t in TABS}')
if idx != -1:
    idx_start = text.rfind('WHERE ROWNUM<=300"""}', 0, idx)
    if idx_start != -1:
        new_text = text[:idx_start] + 'WHERE ROWNUM<=300"""}\n ]}\n]\n\n' + text[idx:]
        with open(r'privet\onyx_reports\app.py', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("TABS end cleaned successfully!")
