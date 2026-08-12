import re

file_path = 'privet/onyx_reports/reports_config.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace FROM ITEM_MOVEMENT to add alias dt
old_from = "FROM IAS20261.ITEM_MOVEMENT\n            WHERE W_CODE IN (105, 103, 121, 122, 118, 108, 119)"
new_from = "FROM IAS20261.ITEM_MOVEMENT dt\n            WHERE dt.W_CODE IN (105, 103, 121, 122, 118, 108, 119)"
content = content.replace(old_from, new_from)

# Replace all column names with dt. prefix
content = content.replace("W_CODE =", "dt.W_CODE =")
content = content.replace("IN_OUT", "dt.IN_OUT")
content = content.replace("I_DATE", "dt.I_DATE")
content = content.replace("I_QTY", "dt.I_QTY")
content = content.replace("SELECT \n                I_CODE,", "SELECT \n                dt.I_CODE,")

# Now replace the specific sales_qty and pur_qty lines
old_sales = "SUM(CASE WHEN dt.I_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND dt.I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND dt.IN_OUT = -1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as sales_qty,"
new_sales = """SUM(CASE WHEN dt.I_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND dt.I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND dt.IN_OUT = -1 
                  AND NOT EXISTS (
                    SELECT 1 FROM IAS20261.ITEM_MOVEMENT t2 
                    WHERE t2.DOC_NO = dt.DOC_NO AND t2.DOC_SER = dt.DOC_SER AND t2.I_CODE = dt.I_CODE AND t2.IN_OUT = 1 
                    AND t2.W_CODE IN (105, 103, 121, 122, 118, 108, 119)
                  ) THEN NVL(dt.I_QTY,0) ELSE 0 END) as sales_qty,"""
content = content.replace(old_sales, new_sales)

old_pur = "SUM(CASE WHEN dt.I_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND dt.I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND dt.IN_OUT = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as pur_qty,"
new_pur = """SUM(CASE WHEN dt.I_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND dt.I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND dt.IN_OUT = 1 
                  AND NOT EXISTS (
                    SELECT 1 FROM IAS20261.ITEM_MOVEMENT t2 
                    WHERE t2.DOC_NO = dt.DOC_NO AND t2.DOC_SER = dt.DOC_SER AND t2.I_CODE = dt.I_CODE AND t2.IN_OUT = -1 
                    AND t2.W_CODE IN (105, 103, 121, 122, 118, 108, 119)
                  ) THEN NVL(dt.I_QTY,0) ELSE 0 END) as pur_qty,"""
content = content.replace(old_pur, new_pur)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("reports_config.py patched successfully again.")
