file_path = 'privet/onyx_reports/reports_config.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove duplicate
duplicate_str = 'AND (:i_code IS NULL OR mv.I_CODE = :i_code)\n              AND (:i_code IS NULL OR mv.I_CODE = :i_code)'
new_str = 'AND (:i_code IS NULL OR mv.I_CODE = :i_code)'
content = content.replace(duplicate_str, new_str)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
