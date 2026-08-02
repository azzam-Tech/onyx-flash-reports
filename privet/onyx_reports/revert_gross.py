import os
filepath = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_formula1 = 'NVL(BILL_AMT,0) - NVL(DISC_AMT,0) + NVL(VAT_AMT,0) + NVL(OTHR_AMT,0)'
new_formula1 = 'NVL(BILL_AMT,0) + NVL(VAT_AMT,0) + NVL(OTHR_AMT,0)'

old_formula2 = 'NVL(BILL_AMT,0)-NVL(DISC_AMT,0)+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)'
new_formula2 = 'NVL(BILL_AMT,0)+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)'

content = content.replace(old_formula1, new_formula1)
content = content.replace(old_formula2, new_formula2)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Reverted to 155,410.01")
