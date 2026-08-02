import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

# Replace the incorrect sales/returns calculation in net_sales_cc
content = content.replace(
    'SUM(NVL(BILL_AMT,0) - (NVL(DISC_AMT,0) - NVL(ADD_DISC_AMT_MST,0))) as sales',
    'SUM(NVL(BILL_AMT,0)) as sales'
)
content = content.replace(
    'SUM(NVL(BILL_AMT,0) - (NVL(DISC_AMT,0) - NVL(ADD_DISC_AMT_MST,0))) as returns',
    'SUM(NVL(BILL_AMT,0)) as returns'
)

# Replace the incorrect sales/returns calculation in net_sales
content = content.replace(
    'SUM(NVL(BILL_AMT,0) - (NVL(DISC_AMT,0) - NVL(ADD_DISC_AMT_MST,0))) as val',
    'SUM(NVL(BILL_AMT,0)) as val'
)


with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)

print("Updated net sales query")
