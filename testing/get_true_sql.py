import codecs
with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()
idx = content.find('"id":"true_income_statement"')
print(content[idx:idx+2500])
