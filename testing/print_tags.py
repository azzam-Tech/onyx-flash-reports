import re

with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx_page = text.find('PAGE = """')
idx_print = text.find('PRINT_PAGE = """')
page_content = text[idx_page:idx_print]

tags = re.findall(r'(\{% (?:if|elif|else|endif).*?%\})', page_content)
for t in tags:
    print(t)
