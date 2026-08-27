import sys, re
with open('testing/new_pivot_sql.py', 'r', encoding='utf-8') as f:
    new_sql = f.read()
with open('privet/onyx_reports/modules/warehouses/repository.py', 'r', encoding='utf-8') as f:
    content = f.read()
old_pattern = r'def get_monthly_movement_pivot_sql\(\):[\s\S]*?ORDER BY ig\.main_grp, ig\.I_CODE\s*\"\"\"'
content = re.sub(old_pattern, new_sql.strip(), content)
with open('privet/onyx_reports/modules/warehouses/repository.py', 'w', encoding='utf-8') as f:
    f.write(content)
