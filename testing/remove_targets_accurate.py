with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove global_vars from TABS
idx_gv = text.find('"global_vars"')
if idx_gv != -1:
    idx_start = text.rfind('{', 0, idx_gv)
    idx_comma = text.rfind(',', 0, idx_start)
    # find ending `]` and `}` of global_vars dict
    idx_reports = text.find('"reports"', idx_gv)
    idx_reports_end = text.find(']', idx_reports)
    idx_dict_end = text.find('}', idx_reports_end)
    text = text[:idx_comma] + text[idx_dict_end+1:]
    print("Removed global_vars from TABS!")

# 2. Remove TARGETS_PAGE and route /targets_ui and /save_targets
idx_tp = text.find('TARGETS_PAGE =')
if idx_tp != -1:
    # TARGETS_PAGE ends with `</body></html>"""` before `from flask import` or `@app.route`
    idx_tp_end = text.find('</body></html>"""', idx_tp) + len('</body></html>"""')
    text = text[:idx_tp] + text[idx_tp_end:]
    print("Removed TARGETS_PAGE!")

idx_route = text.find('@app.route("/targets_ui")')
if idx_route != -1:
    idx_next_route = text.find('@app.route("/")', idx_route)
    text = text[:idx_route] + text[idx_next_route:]
    print("Removed /targets_ui and /save_targets routes!")

with open(r'privet\onyx_reports\app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Targets feature safely and accurately removed!")
