import re

file_path = 'privet/onyx_reports/report_handlers.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('"105": "خميس مشيط"', '"105": "الغنامية / نصر الله"')
content = content.replace('"103": "الرياض"', '"103": "الغنامية عيظه"')
content = content.replace('"121": "جدة"', '"121": "جده"')
content = content.replace('"122": "الدمام"', '"122": "الشمال"')
content = content.replace('"118": "بريدة"', '"118": "الجنوب خميس مشيط"')
content = content.replace('"108": "مستودع المرتجعات"', '"108": "المنصورية 1"')
content = content.replace('"119": "تبوك"', '"119": "الدمام"')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed warehouse names in report_handlers.py!")
