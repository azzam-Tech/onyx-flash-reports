with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove `global_vars` tab block from TABS array
# Find `"id": "global_vars"`
idx_gv = text.find('"global_vars"')
if idx_gv != -1:
    # Find preceding `{`
    idx_start = text.rfind('{', 0, idx_gv)
    # Find `,` before idx_start if any
    idx_comma = text.rfind(',', 0, idx_start)
    # Find matching closing `}` and `]` of global_vars
    idx_end = text.find(']', idx_gv)
    idx_end_bracket = text.find('}', idx_end)
    text = text[:idx_comma] + text[idx_end_bracket+1:]
    print("Removed global_vars from TABS!")

# 2. Remove TARGETS_PAGE definition up to `@app.route("/targets_ui")`
idx_tp = text.find('TARGETS_PAGE =')
if idx_tp != -1:
    idx_tp_end = text.find('"""', idx_tp + 20) + 3
    text = text[:idx_tp] + text[idx_tp_end:]
    print("Removed TARGETS_PAGE!")

# 3. Remove routes /targets_ui and /save_targets up to `@app.route("/")`
idx_route = text.find('@app.route("/targets_ui")')
if idx_route != -1:
    idx_next_route = text.find('@app.route("/")', idx_route)
    text = text[:idx_route] + text[idx_next_route:]
    print("Removed /targets_ui and /save_targets routes!")

# 4. Remove _load_targets_raw and save_targets_to_file functions if present
idx_func = text.find('def _load_targets_raw():')
if idx_func != -1:
    idx_func_end = text.find('def get_conn():', idx_func)
    text = text[:idx_func] + text[idx_func_end:]
    print("Removed targets helper functions!")

with open(r'privet\onyx_reports\app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Target feature safely and completely removed!")
