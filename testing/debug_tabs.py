import codecs
with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

idx = content.find('"id": "global_vars"')
if idx != -1:
    print(content[max(0, idx-100):idx+1500])
else:
    print("NOT FOUND")
