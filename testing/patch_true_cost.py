import codecs
import re

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

# I will find the SQL block for true_income_statement and do string replacements.
idx = content.find('"id":"true_income_statement"')
end_idx = content.find('"""}', idx)

sql_block = content[idx:end_idx+4]

# Replace in inv_cogs
new_sql_block = sql_block.replace(
    'im.STK_COST', 'it.PRIMARY_COST'
).replace(
    'FROM IAS20261.ITEM_MOVEMENT im\n          JOIN IAS20261.IAS_BILL_MST m',
    'FROM IAS20261.ITEM_MOVEMENT im\n          JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE\n          JOIN IAS20261.IAS_BILL_MST m'
).replace(
    'FROM IAS20261.ITEM_MOVEMENT im\n          JOIN IAS20261.IAS_RT_BILL_MST r',
    'FROM IAS20261.ITEM_MOVEMENT im\n          JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE\n          JOIN IAS20261.IAS_RT_BILL_MST r'
)

# Apply replacement back to content
content = content.replace(sql_block, new_sql_block)

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)
print("Updated true_income_statement to use PRIMARY_COST")
