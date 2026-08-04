import os
import re

app_file = 'privet/onyx_reports/app.py'
with open(app_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the /settings route
settings_pattern = re.compile(r'@app\.route\("/settings", methods=\["GET","POST"\]\)\ndef settings\(\):.*?return render_template\("settings\.html", tabs=_vis, hidden_tabs=ht, hidden_reports=hr,\n                                  hide_profit=load_hide_profit\(\)\)', re.DOTALL)
content = re.sub(settings_pattern, '', content)

# Modify /globals route to handle hide_profit
globals_pattern = re.compile(r'(def globals_page\(\):.*?if request\.method == "POST":\n)(.*?)(\n\s*save_globals\(targets_data\)\n\s*saved = True\n)', re.DOTALL)

def replacement(match):
    before = match.group(1)
    loop = match.group(2)
    after = match.group(3)
    
    new_loop = """        hide_profit = "hide_profit" in request.form
        save_hidden([], [], hide_profit=hide_profit)
""" + loop
    return before + new_loop + after

content = re.sub(globals_pattern, replacement, content)

# Modify the render_template in globals_page
content = content.replace(
    'return render_template("globals.html", reps=reps, targets=targets_data.get("2026", {}), saved=saved)',
    'return render_template("globals.html", reps=reps, targets=targets_data.get("2026", {}), saved=saved, hide_profit=load_hide_profit())'
)

with open(app_file, 'w', encoding='utf-8') as f:
    f.write(content)

# Delete settings.html
settings_html = 'privet/onyx_reports/templates/settings.html'
if os.path.exists(settings_html):
    os.remove(settings_html)
