import os

with open('privet/onyx_reports/app.py', 'r', encoding='utf-8') as f:
    app_lines = f.readlines()

with open('testing/temp_aging_analytical.py', 'r', encoding='utf-8') as f:
    analytical_content = f.read()

# Find insertion point for function
insert_idx = -1
for i, line in enumerate(app_lines):
    if 'def run_main_wh_movement(rpt, args):' in line:
        insert_idx = i
        break

if insert_idx != -1:
    app_lines.insert(insert_idx, analytical_content + '\n\n')

# Find TABS and insert the new tab
tab_content = '''        {"id":"perf_aging_dynamic_analytical","title":"أعمار التحصيل الصافي (تحليلي)","params":[DFROM,DTO,REP,INCR,INCN,INCC,INCRT],"sql":"""
       -- This report dynamically processes valid collections via Python FIFO per customer
       SELECT 'Dynamic Analytical' as "Placeholder" FROM DUAL
       """},
'''
for i, line in enumerate(app_lines):
    if '"id":"perf_aging_dynamic"' in line:
        app_lines.insert(i, tab_content)
        break

# Find run_report routing
for i, line in enumerate(app_lines):
    if 'if rpt["id"] in ["perf_aging", "perf_aging_dynamic"]:' in line:
        app_lines.insert(i+2, '''    elif rpt["id"] == "perf_aging_dynamic_analytical":
        cols, rows = run_perf_aging_analytical(rpt, args)
''')
        break

with open('privet/onyx_reports/app.py', 'w', encoding='utf-8') as f:
    f.writelines(app_lines)
print('Updated app.py successfully')
