import re

with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx_page = text.find('PAGE = """')
idx_print = text.find('PRINT_PAGE = """')
page_content = text[idx_page:idx_print]

matches = list(re.finditer(r'\{%\s*else\s*%\}', page_content))
for m in matches:
    start = max(0, m.start() - 40)
    end = min(len(page_content), m.end() + 40)
    print(repr(page_content[start:end]))
    print("="*30)
