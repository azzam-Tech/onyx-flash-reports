with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx_page = text.find('PAGE = """')
idx_print = text.find('PRINT_PAGE = """')
page_content = text[idx_page:idx_print]

# Find any stray {% else %} without matching if in page_content
print("Occurrences of {% else %} in PAGE:", page_content.count("{% else %}"))
