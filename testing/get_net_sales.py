import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

idx = content.find('"id":"net_sales_cc"')
end_idx = content.find('"""}', idx)
print(content[idx:end_idx+4])
