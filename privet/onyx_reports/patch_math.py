import os
filepath = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Revert cash_sales to include - NVL(DISC_AMT,0)
old_formula = 'NVL(BILL_AMT,0) + NVL(VAT_AMT,0) + NVL(OTHR_AMT,0)'
new_formula = 'NVL(BILL_AMT,0) - NVL(DISC_AMT,0) + NVL(VAT_AMT,0) + NVL(OTHR_AMT,0)'
content = content.replace(old_formula, new_formula)
# Also fix the one in rep_sales_stats which might have been changed
old_formula_plus = 'NVL(BILL_AMT,0)+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)'
new_formula_plus = 'NVL(BILL_AMT,0)-NVL(DISC_AMT,0)+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)'
content = content.replace(old_formula_plus, new_formula_plus)

# 2. Add A_CODE LIKE '111%' to DOC_TYPE=15
old_ext_notice = """  SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
         0, 0, 0, 0, 0, CR_AMT
  FROM IAS20261.IAS_POST_DTL
  WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=15 AND NVL(CR_AMT,0)>0"""

new_ext_notice = """  SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
         0, 0, 0, 0, 0, CR_AMT
  FROM IAS20261.IAS_POST_DTL
  WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=15 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0"""

if old_ext_notice in content:
    content = content.replace(old_ext_notice, new_ext_notice)
    print("Fixed ext_notice")
else:
    print("Could not find ext_notice block")
    # Let's do a more robust regex or simple replace
    content = content.replace("AND DOC_TYPE=15 AND NVL(CR_AMT,0)>0", "AND DOC_TYPE=15 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0")
    print("Force replaced DOC_TYPE=15")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Patch complete.")
