import re

file_path = 'privet/onyx_reports/reports_config.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Original params:
# "params":[{"name":"as_of","label":"إلى تاريخ","type":"date","default":"2026-07-31"},{"name":"w_code","label":"رقم المستودع (اختياري)","type":"text","default":""}]

# Find the stock_bal report block and inject the new parameter i_code
old_params = '{"id":"stock_bal","title":"أرصدة الأصناف","params":[{"name":"as_of","label":"إلى تاريخ","type":"date","default":"2026-07-31"},{"name":"w_code","label":"رقم المستودع (اختياري)","type":"text","default":""}]'
new_params = '{"id":"stock_bal","title":"أرصدة الأصناف","params":[{"name":"as_of","label":"إلى تاريخ","type":"date","default":"2026-07-31"},{"name":"w_code","label":"رقم المستودع (اختياري)","type":"text","default":""},{"name":"i_code","label":"رقم الصنف (اختياري)","type":"text","default":""}]'

content = content.replace(old_params, new_params)

# Inject the SQL condition: AND (:i_code IS NULL OR mv.I_CODE = :i_code)
# right after: AND (:w_code IS NULL OR mv.W_CODE = :w_code)
# Note: we need to find that in the stock_bal SQL.
sql_search = 'AND (:w_code IS NULL OR mv.W_CODE = :w_code)'
sql_replace = sql_search + '\n            AND (:i_code IS NULL OR mv.I_CODE = :i_code)'

# since there's only one stock_bal, but wait, w_code could be elsewhere?
# Let's verify we're replacing only one occurrence or all relevant ones (they should be identical).
content = content.replace(sql_search, sql_replace)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("stock_bal patched!")
