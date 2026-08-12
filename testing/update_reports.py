import sys
file_path = 'privet/onyx_reports/reports_config.py'
with open(file_path, 'r', encoding='utf-8') as f:
    c = f.read()

# Add to aging
c = c.replace('"fn":"run_cust_aging","params":[', '"fn":"run_cust_aging","params":[{"name":"grp_code","label":"مجموعة العملاء (اختياري)","type":"text","default":""},{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},')

# Add to perf_aging_dynamic
c = c.replace('"fn":"run_perf_aging_fifo","params":[', '"fn":"run_perf_aging_fifo","params":[{"name":"grp_code","label":"مجموعة العملاء (اختياري)","type":"text","default":""},{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},')

# Add to perf_aging_dynamic_analytical
c = c.replace('"fn":"run_perf_aging_analytical","params":[', '"fn":"run_perf_aging_analytical","params":[{"name":"grp_code","label":"مجموعة العملاء (اختياري)","type":"text","default":""},{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(c)
print('Parameters added to reports_config.py')
