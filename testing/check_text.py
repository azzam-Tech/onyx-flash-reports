import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

idx = content.find('"id":"true_income_statement"')
if idx != -1:
    idx2 = content.find('SELECT', content.find('all_data AS', idx))
    print(content[idx2:idx2+500].encode('utf-8'))
else:
    print("Not found")
