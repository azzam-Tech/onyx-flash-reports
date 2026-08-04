import re

file_path = 'privet/onyx_reports/reports_config.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the params list
old_params = '{"id":"smart_replenishment","title":"ذكاء المشتريات (تغطية المخزون)","params":[{"name":"as_of","label":"إلى تاريخ","type":"date","default":"2026-07-31"},{"name":"days","label":"فترة سحب المبيعات (أيام)","type":"number","default":"90"}]'
new_params = '{"id":"smart_replenishment","title":"ذكاء المشتريات (تغطية المخزون)","params":[{"name":"as_of","label":"إلى تاريخ","type":"date","default":"2026-07-31"},{"name":"days","label":"فترة سحب المبيعات (أيام)","type":"number","default":"90"},{"name":"i_code","label":"رقم الصنف (اختياري)","type":"text","default":""}]'
content = content.replace(old_params, new_params)

# 2. Update the stock CTE
old_stock_where = "WHERE mv.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1"
new_stock_where = "WHERE mv.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1\n            AND (:i_code IS NULL OR mv.I_CODE = :i_code)"

# To be safe, only replace the one inside smart_replenishment
# We can use regex to target it or just replace it (but wait, stock_bal also has a similar WHERE, but stock_bal has w_code).
# Yes, smart_replenishment doesn't have w_code.
# Wait, let's find the exact block for smart_replenishment.
start_idx = content.find('"id":"smart_replenishment"')
end_idx = content.find('"id":"stock_bal"')

if start_idx != -1 and end_idx != -1:
    block = content[start_idx:end_idx]
    
    # replace stock where
    block = block.replace(old_stock_where, new_stock_where)
    
    # replace sales where
    old_sales_where = "AND I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1"
    new_sales_where = "AND I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1\n              AND (:i_code IS NULL OR I_CODE = :i_code)"
    block = block.replace(old_sales_where, new_sales_where)
    
    content = content[:start_idx] + block + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Smart Replenishment patched with i_code filter!")
