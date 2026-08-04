import re
file_path = 'privet/onyx_reports/templates/globals.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the table content
table_match = re.search(r'(<div style="overflow-x:auto; max-height: 70vh; margin-bottom: 20px; border-radius: 8px; border: 1px solid #e2e8f0">.*?</div>)', content, re.DOTALL)
table_content = table_match.group(1) if table_match else ''

# Clean up existing form content
content = re.sub(r'<form method="post" action="/globals">.*?</form>', '<!-- FORM_PLACEHOLDER -->', content, flags=re.DOTALL)

# Add CSS for tabs
css_tabs = """
.settings-tabs { display: flex; gap: 10px; margin-bottom: 20px; border-bottom: 2px solid #e2e8f0; }
.tab-btn { padding: 10px 20px; font-weight: 700; font-size: 15px; color: #64748b; background: none; border: none; cursor: pointer; border-bottom: 3px solid transparent; margin-bottom: -2px; transition: 0.2s; font-family: inherit; }
.tab-btn:hover { color: #4f46e5; }
.tab-btn.active { color: #4f46e5; border-bottom-color: #4f46e5; }
.tab-content { display: none; animation: fadeIn 0.3s; }
.tab-content.active { display: block; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }
"""
content = content.replace('</style>', css_tabs + '\n</style>')

# Build the new form with tabs
new_form = f"""
   <div class="settings-tabs">
     <button type="button" class="tab-btn active" onclick="switchTab('targets')">المتغيرات (أهداف المناديب)</button>
     <button type="button" class="tab-btn" onclick="switchTab('other')">إعدادات أخرى</button>
   </div>

   <form method="post" action="/globals">
     <div id="targets" class="tab-content active">
       {table_content}
     </div>
     
     <div id="other" class="tab-content">
       <div style="margin: 0 0 20px 0; padding: 20px; background: #fff; border-radius: 12px; border: 1px solid #e2e8f0; display: flex; align-items: center; gap: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
         <input type="checkbox" id="hide_profit" name="hide_profit" value="1" {{% if hide_profit %}}checked{{% endif %}} style="width: 22px; height: 22px; cursor: pointer; accent-color: #4f46e5;">
         <label for="hide_profit" style="font-size: 16px; font-weight: 700; color: #1e293b; cursor: pointer; margin: 0;">إخفاء الأرباح (يخفي مجمل وصافي الربح من جميع التقارير ولوحة القيادة)</label>
       </div>
       <div style="padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; text-align: center; color: #64748b; font-weight: 600;">
         سيتم إضافة إعدادات إضافية هنا مستقبلاً...
       </div>
     </div>
     
     <div style="text-align:left; margin-top:25px; border-top: 1px solid #e2e8f0; padding-top: 20px;">
         <button type="submit" style="background:#4f46e5;color:#fff;border:0;padding:12px 30px;border-radius:10px;font-weight:700;font-size:16px;cursor:pointer; box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3); transition: 0.3s;">حفظ الإعدادات والمتغيرات</button>
     </div>
   </form>

   <script>
   function switchTab(id) {{
       document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
       document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
       document.querySelector(`button[onclick="switchTab('${{id}}')"]`).classList.add('active');
       document.getElementById(id).classList.add('active');
   }}
   </script>
"""

content = content.replace('<!-- FORM_PLACEHOLDER -->', new_form)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added tabs to globals.html")
