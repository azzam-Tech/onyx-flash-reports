with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add ITM definition
old_cst_def = 'CST   = {"name":"c_code","label":"العميل (اختياري)","type":"text","default":""}'
new_cst_def = 'CST   = {"name":"c_code","label":"العميل (اختياري)","type":"text","default":""}\nITM   = {"name":"i_code","label":"الصنف (اختياري)","type":"text","default":""}'

if old_cst_def in content:
    content = content.replace(old_cst_def, new_cst_def)
    print("Added ITM definition to app.py!")

with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Finished patching ITM in app.py!")
