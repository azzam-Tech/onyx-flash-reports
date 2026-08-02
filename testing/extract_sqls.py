import re
with open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

m1 = re.search(r'"id":\s*"net_sales_cc".*?"sql":\s*"""(.*?)"""', content, re.DOTALL)
m2 = re.search(r'"id":\s*"collection_adopted".*?"sql":\s*"""(.*?)"""', content, re.DOTALL)

if m1 and m2:
    with open("testing/extracted_sqls.txt", "w", encoding="utf-8") as out:
        out.write("--- net_sales_cc ---\n")
        out.write(m1.group(1))
        out.write("\n\n--- collection_adopted ---\n")
        out.write(m2.group(1))
    print("Extracted SQLs to testing/extracted_sqls.txt")
else:
    print("Could not find one or both SQL queries.")
