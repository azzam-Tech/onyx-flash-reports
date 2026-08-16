import os

filepath = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\reports_config.py"

with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
target_str = '{"name":"vendor_link","label":"عميل مرتبط بمورد","type":"checkbox","default":"0"},'

for line in lines:
    if "perf_aging_dynamic" in line and target_str in line:
        line = line.replace(target_str, "")
    new_lines.append(line)

with open(filepath, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Done removing filter from perf_aging_dynamic reports.")
