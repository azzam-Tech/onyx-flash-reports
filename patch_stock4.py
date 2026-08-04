file_path = 'privet/onyx_reports/reports_config.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re
# Find the exact w_code json block and the closing bracket
match = re.search(r'\{"name":"w_code".*?\]', content)
if match:
    old_str = match.group(0)
    # The string ends with } ]
    # We want to replace ] with ,{"name":"i_code","label":"رقم الصنف (اختياري)","type":"text","default":""}]
    new_str = old_str[:-1] + ',{"name":"i_code","label":"رقم الصنف (اختياري)","type":"text","default":""}]'
    
    # Also find the SQL string to inject the filter
    sql_match = re.search(r'AND \(:w_code IS NULL OR mv\.W_CODE = :w_code\)', content)
    
    if sql_match:
        sql_old = sql_match.group(0)
        sql_new = sql_old + '\n            AND (:i_code IS NULL OR mv.I_CODE = :i_code)'
        
        content = content.replace(old_str, new_str)
        content = content.replace(sql_old, sql_new)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Success!")
    else:
        print("SQL match not found")
else:
    print("w_code match not found")
