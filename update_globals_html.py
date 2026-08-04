import re
file_path = 'privet/onyx_reports/templates/globals.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add the hide_profit checkbox right before the save button
checkbox_html = """
     </div>
     <div style="margin: 20px 0; padding: 15px; background: #fff; border-radius: 8px; border: 1px solid #e2e8f0; display: flex; align-items: center; gap: 10px;">
       <input type="checkbox" id="hide_profit" name="hide_profit" value="1" {% if hide_profit %}checked{% endif %} style="width: 20px; height: 20px; cursor: pointer;">
       <label for="hide_profit" style="font-size: 15px; font-weight: 700; color: #1e293b; cursor: pointer;">إخفاء الأرباح (يخفي مجمل وصافي الربح من جميع التقارير ولوحة القيادة)</label>
     </div>
"""

# The original has a closing div for the table wrapper before the button.
# Let's just find the button and insert before it.
content = content.replace(
    '<div style="text-align:left; margin-top:15px">',
    checkbox_html + '\n     <div style="text-align:left; margin-top:15px">'
)

content = content.replace('حفظ المتغيرات', 'حفظ الإعدادات والمتغيرات')
content = content.replace('>المتغيرات العامة<', '>الإعدادات والمتغيرات العامة<')
content = content.replace('المتغيرات العامة (التارجت)', 'الإعدادات والمتغيرات العامة')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated globals.html")
