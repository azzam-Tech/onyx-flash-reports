import re
import os

file_path = 'privet/onyx_reports/templates/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace CSS
old_css = r'<style>\s*\.dataTables_wrapper\s*\{.*?\}\s*</style>'
new_css = """<style>
.dataTables_wrapper { direction: rtl; padding: 15px 10px; }
.dataTables_wrapper .dataTables_filter { float: right !important; text-align: right; margin-bottom: 15px; }
.dataTables_wrapper .dataTables_length { float: left !important; margin-bottom: 15px; }
.dataTables_wrapper .dataTables_filter label { font-weight: 700; color: var(--ink-dark); font-size: 15px; display:inline-flex; align-items:center; gap:8px; }
.dataTables_wrapper .dataTables_filter input { border: 2px solid #cbd5e1; border-radius: 8px; padding: 10px 14px; font-family: inherit; font-size: 14px; outline: none; transition: 0.3s; width: 300px; background: #f8fafc; }
.dataTables_wrapper .dataTables_filter input:focus { border-color: var(--primary); background: #fff; box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.15); }
table.dataTable thead th, table.dataTable tfoot th { text-align: right; border-bottom: 1px solid #e2e8f0; }
table.dataTable.no-footer { border-bottom: 1px solid #e2e8f0; }
.dataTables_wrapper .dataTables_paginate .paginate_button { padding: 6px 12px; margin-left: 4px; border-radius: 8px !important; border: 1px solid transparent !important; font-weight:600; }
.dataTables_wrapper .dataTables_paginate .paginate_button:hover { background: #f1f5f9 !important; border-color: #cbd5e1 !important; color: #0f172a !important; }
.dataTables_wrapper .dataTables_paginate .paginate_button.current { background: var(--primary) !important; color: #fff !important; border-color: var(--primary) !important; }
</style>"""

html = re.sub(old_css, new_css, html, flags=re.DOTALL)

# Replace Language JS
old_lang = r'"language":\s*\{\s*"url":\s*"//cdn.datatables.net/plug-ins/1.13.6/i18n/ar.json"\s*\}'
new_lang = """"language": {
            "url": "//cdn.datatables.net/plug-ins/1.13.6/i18n/ar.json",
            "search": "بحث سريع:",
            "searchPlaceholder": "اكتب للبحث في التقرير...",
            "lengthMenu": "عرض _MENU_ سجل"
        }"""
html = re.sub(old_lang, new_lang, html)


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("CSS and JS language patched successfully.")
