import sys

file_path = 'privet/onyx_reports/reports_config.py'
with open(file_path, 'r', encoding='utf-8') as f:
    c = f.read()

cb_str = '{"name":"vendor_link","label":"عميل مرتبط بمورد","type":"checkbox","default":"0"},'

# Add to aging
c = c.replace('"fn":"run_cust_aging","params":[', f'"fn":"run_cust_aging","params":[{cb_str}')
# Add to perf_aging_dynamic
c = c.replace('"fn":"run_perf_aging_fifo","params":[', f'"fn":"run_perf_aging_fifo","params":[{cb_str}')
# Add to perf_aging_dynamic_analytical
c = c.replace('"fn":"run_perf_aging_analytical","params":[', f'"fn":"run_perf_aging_analytical","params":[{cb_str}')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(c)
print('Added vendor_link checkbox to reports_config.py')
