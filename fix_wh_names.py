import re

file_path = 'privet/onyx_reports/reports_config.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the incorrect aliases in the warehouse_rebalancing query
# 105: "خميس مشيط (105)" -> "الغنامية نصرالله (105)"
# 103: "الرياض (103)" -> "الغنامية عيظه (103)"
# 121: "جدة (121)" -> "جده (121)"
# 122: "الدمام (122)" -> "الشمال (122)"
# 118: "بريدة (118)" -> "الجنوب خميس مشيط (118)"
# 108: "مستودع المرتجعات (108)" -> "المنصورية 1 (108)"
# 119: "تبوك (119)" -> "الدمام (119)"

content = content.replace('"الرياض (103)"', '"الغنامية عيظه (103)"')
content = content.replace('"جدة (121)"', '"جده (121)"')
content = content.replace('"الدمام (122)"', '"الشمال (122)"')
content = content.replace('"خميس مشيط (105)"', '"الغنامية نصرالله (105)"')
content = content.replace('"بريدة (118)"', '"الجنوب خميس مشيط (118)"')
content = content.replace('"تبوك (119)"', '"الدمام (119)"')
content = content.replace('"مستودع المرتجعات (108)"', '"المنصورية 1 (108)"')

# Wait, there's another place: in the item_matrix AS ( SELECT ... )
content = content.replace('as "الرياض (103)"', 'as "الغنامية عيظه (103)"')
# actually wait, I didn't use Arabic names in the AS clause of the CTE, I used w_105, w_103...
# Oh yes, I did: SUM(CASE WHEN W_CODE = '105' THEN qty ELSE 0 END) as w_105
# Let me double check my add_rebalance_report.py
# Ah, I used w_103, w_105 etc in the CTE, and only used Arabic in the final SELECT!
# So the above simple replacements are sufficient!

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed warehouse names in reports_config.py!")
