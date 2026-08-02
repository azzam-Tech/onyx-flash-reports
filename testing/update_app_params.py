import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

new_params = """
PYEAR = {"name":"p_year","label":"السنة","type":"select","default":"2026","options":[["2024","2024"],["2025","2025"],["2026","2026"],["2027","2027"]]}
PTYPE = {"name":"p_type","label":"نوع التقرير","type":"select","default":"month","options":[["month","شهري"],["quarter","ربعي"],["half","نصفي"],["year","سنوي"]]}
PVAL  = {"name":"p_val","label":"الفترة","type":"select","default":"1","options":[[str(i),str(i)] for i in range(1,13)]}
"""

if 'PYEAR =' not in content:
    content = content.replace('BTYPE = {"name":"bill_type"', new_params.strip() + '\nBTYPE = {"name":"bill_type"')

# Update sales_vs_collection
content = content.replace(
    '{"id":"sales_vs_collection","title":"المبيعات مقابل التحصيل","params":[DFROM,DTO],"sql":',
    '{"id":"sales_vs_collection","title":"المبيعات مقابل التحصيل","params":[PYEAR,PTYPE,PVAL],"sql":'
)

# Update SQL for sales_vs_collection to add التارقت column
# It currently has: TO_CHAR(SUM(NVL(bc.total_inc, 0)), 'FM999,999,999,990.00') AS "إجمالي التحصيل"
# We want to add: NULL AS "التارقت"
old_select = """TO_CHAR(SUM(NVL(bc.total_inc, 0)), 'FM999,999,999,990.00') AS "إجمالي التحصيل"
     FROM net_sales ns"""
new_select = """TO_CHAR(SUM(NVL(bc.total_inc, 0)), 'FM999,999,999,990.00') AS "إجمالي التحصيل",
            NULL AS "التارقت"
     FROM net_sales ns"""
content = content.replace(old_select, new_select)

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)

print("SUCCESS")
