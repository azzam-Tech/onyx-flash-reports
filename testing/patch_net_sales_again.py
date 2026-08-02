import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

# Replace for sales
content = content.replace(
    'SUM(NVL(BILL_AMT,0)) as sales',
    'SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as sales'
)

# Replace for returns
content = content.replace(
    'SUM(NVL(BILL_AMT,0)) as returns',
    'SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as returns'
)

# For net_sales report if it uses 'as val' or something... wait, in net_sales it uses 'as sales' and 'as returns' too!
# Just to be safe, I'll print if it found and replaced
print("Replaced 'as sales' count:", content.count('SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as sales'))
print("Replaced 'as returns' count:", content.count('SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as returns'))

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)
