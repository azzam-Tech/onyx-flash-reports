import codecs
with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

idx = content.find('"id":"true_income_statement"')
end_idx = content.find('"""}', idx)
print("TRUE INCOME STATEMENT SQL:")
print(content[idx:end_idx+4])

print("PRINT_PAGE CSS:")
idx2 = content.find('PRINT_PAGE =')
end2 = content.find('</style>', idx2)
print(content[idx2:end2+8])
