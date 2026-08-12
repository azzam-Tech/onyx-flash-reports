import re

file_path = 'privet/onyx_reports/reports_config.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'\{\"id\":\"aging\",\"title\":\"أعمار الديون\".*?GROUP BY o.C_CODE ORDER BY SUM\(o.unpaid\) DESC\"\"\"\}'

new_config = """{"id":"aging","title":"أعمار الديون","fn":"run_cust_aging","params":[
     DTO,
     AGETR,
     {"name":"rep_code","label":"المندوب (اختياري)","type":"text","default":""},
     {"name":"c_code","label":"كود العميل (اختياري)","type":"text","default":""}
   ]}"""

content = re.sub(pattern, new_config, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated aging config in reports_config.py")
