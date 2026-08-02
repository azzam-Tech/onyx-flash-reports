import codecs
with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

idx = content.find("{% if rpt.id == 'targets_ui' %}")
if idx != -1:
    print(content[max(0, idx-100):idx+500])
else:
    print("NOT FOUND targets_ui check in PAGE")
