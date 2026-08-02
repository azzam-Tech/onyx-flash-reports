# -*- coding: utf-8 -*-
import re

with open('app.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update PRINT_PAGE styling
old_print_style = '''<style>
@page{margin:13mm}
*{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:Tahoma,Arial;direction:rtl;color:#20343a;margin:0}
.hd{display:flex;align-items:center;justify-content:space-between;border-bottom:3px solid #22b3a3;padding-bottom:10px;margin-bottom:14px}
.hd h1{font-size:20px;margin:0;color:#12333c}
.hd .dt{font-size:11px;color:#6b7280;margin-top:4px}
.logo{height:40px}
.filt{font-size:11px;color:#5a7379;margin-bottom:12px;background:#f4faf8;border:1px solid #e5eeeb;border-radius:6px;padding:7px 10px}
.filt b{color:#14867a}
table{border-collapse:collapse;width:100%}
thead th{background:#12333c;color:#fff;padding:7px 8px;font-size:11px;text-align:right;border:1px solid #12333c}
tbody td{padding:6px 8px;font-size:11px;border:1px solid #e5e7eb;text-align:right}
tbody tr:nth-child(even) td{background:#f4faf8}
.ft{margin-top:14px;font-size:10px;color:#9aacae;text-align:center;border-top:1px solid #eee;padding-top:6px}
</style>'''

new_print_style = '''<style>
@page{margin:13mm}
*{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:'Cairo','Inter',Tahoma,sans-serif;direction:rtl;color:#1e293b;margin:0}
.hd{display:flex;align-items:center;justify-content:space-between;border-bottom:3px solid #4f46e5;padding-bottom:15px;margin-bottom:20px}
.hd h1{font-size:22px;margin:0;color:#0f172a;font-weight:800}
.hd .dt{font-size:12px;color:#64748b;margin-top:6px;font-weight:600}
.logo{height:44px}
.filt{font-size:12px;color:#475569;margin-bottom:15px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:10px 14px;font-weight:600}
.filt b{color:#4f46e5}
table{border-collapse:collapse;width:100%}
thead th{background:#4f46e5;color:#fff;padding:10px 12px;font-size:12px;text-align:right;border:1px solid #4338ca;font-weight:700}
tbody td{padding:8px 12px;font-size:12px;border:1px solid #e2e8f0;text-align:right;font-weight:500;color:#1e293b}
tbody tr:nth-child(even) td{background:#f8fafc}
.ft{margin-top:20px;font-size:11px;color:#94a3b8;text-align:center;border-top:1px solid #e2e8f0;padding-top:10px;font-weight:600}
</style>'''

if old_print_style in text:
    text = text.replace(old_print_style, new_print_style)
else:
    # Fallback regex
    text = re.sub(r'<style>\s*@page\{margin:13mm\}.*?</style>', new_print_style, text, flags=re.DOTALL)

# 2. Update PRINT_PAGE logo fill color from #22b3a3 to #4f46e5
text = text.replace('fill="#22b3a3"', 'fill="#4f46e5"')

# 3. Update SETTINGS_PAGE and PIN_PAGE inline styles
# old teal color #22b3a3 -> #4f46e5
text = text.replace('color:#22b3a3;', 'color:#4f46e5;')
text = text.replace('background:#22b3a3;', 'background:#4f46e5;')

# Add .card class to STYLE if not there
if '.card {' not in text:
    text = text.replace('.app { display: flex', '.card { background: var(--card-bg); border-radius: 20px; padding: 24px; box-shadow: var(--sh); }\n.app { display: flex')

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Secondary pages patched!")
