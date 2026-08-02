import sys
import re

app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove old CSS
css_removals = [
    ".filters .quick-dates { grid-column: 1 / -1; display: flex; gap: 8px; flex-wrap: wrap; background: #f8fafc; padding: 6px; border-radius: 14px; border: 1px solid var(--line); margin-bottom: 4px; }",
    ".filters .quick-dates .btn-sm { background: transparent; border: none; color: var(--ink); padding: 10px 16px; border-radius: 10px; font-size: 13.5px; font-weight: 700; cursor: pointer; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); flex: 1; text-align: center; }",
    ".filters .quick-dates .btn-sm:hover { color: var(--primary); background: rgba(79, 70, 229, 0.08); transform: translateY(-1px); }",
    ".filters .quick-dates .btn-sm:active, .filters .quick-dates .btn-sm.active { background: #fff; color: var(--primary); box-shadow: 0 4px 12px rgba(0,0,0,0.06); transform: none; }"
]
for c in css_removals:
    content = content.replace(c + '\n', '')
    content = content.replace(c, '')

# 2. Add New Beautiful Standalone CSS
new_css = """
.quick-dates { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 24px; align-items: center; }
.quick-dates .btn-sm { background: #ffffff; border: 1px solid #e2e8f0; color: var(--ink-dark); padding: 10px 20px; border-radius: 12px; font-size: 14px; font-weight: 700; cursor: pointer; transition: all 0.3s ease; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
.quick-dates .btn-sm:hover { background: #f8fafc; border-color: #cbd5e1; transform: translateY(-2px); box-shadow: 0 6px 12px rgba(0,0,0,0.05); color: var(--primary); }
.quick-dates .btn-sm:active, .quick-dates .btn-sm.active { background: var(--primary); border-color: var(--primary); color: #ffffff; transform: translateY(0); box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2); }
</style>
"""
if '.quick-dates {' not in content:
    content = content.replace('</style>', new_css, 1)

# 3. Clean up old HTML from inside the form
html_pattern = re.compile(r'       {% if rpt\.params and \'date_from\' in rpt\.params\|map\(attribute=\'name\'\) %}\n       <div class="quick-dates">.*?</script>\n       {% endif %}', re.DOTALL)
content = html_pattern.sub('', content)

# 4. Insert HTML after the form
html_to_insert = """
     {% if rpt.params and 'date_from' in rpt.params|map(attribute='name') %}
     <div class="quick-dates">
         <button type="button" class="btn-sm" onclick="setDates('today', this)">اليوم</button>
         <button type="button" class="btn-sm" onclick="setDates('this_week', this)">هذا الأسبوع</button>
         <button type="button" class="btn-sm" onclick="setDates('this_month', this)">هذا الشهر</button>
         <button type="button" class="btn-sm" onclick="setDates('last_month', this)">الشهر السابق</button>
         <button type="button" class="btn-sm" onclick="setDates('this_year', this)">هذه السنة</button>
         <button type="button" class="btn-sm" onclick="setDates('last_year', this)">السنة السابقة</button>
     </div>
     <script>
         function setDates(range, btn) {
             document.querySelectorAll('.quick-dates .btn-sm').forEach(b => b.classList.remove('active'));
             if(btn) btn.classList.add('active');
             
             const dFrom = document.querySelector('input[name="date_from"]');
             const dTo = document.querySelector('input[name="date_to"]');
             if(!dFrom || !dTo) return;
             
             const today = new Date();
             let from = new Date();
             let to = new Date();

             if(range === 'today') {
                 // keep today
             } else if (range === 'this_week') {
                 const day = today.getDay();
                 from.setDate(today.getDate() - day);
             } else if (range === 'this_month') {
                 from = new Date(today.getFullYear(), today.getMonth(), 1);
                 to = new Date(today.getFullYear(), today.getMonth() + 1, 0);
             } else if (range === 'last_month') {
                 from = new Date(today.getFullYear(), today.getMonth() - 1, 1);
                 to = new Date(today.getFullYear(), today.getMonth(), 0);
             } else if (range === 'this_year') {
                 from = new Date(today.getFullYear(), 0, 1);
                 to = new Date(today.getFullYear(), 11, 31);
             } else if (range === 'last_year') {
                 from = new Date(today.getFullYear() - 1, 0, 1);
                 to = new Date(today.getFullYear() - 1, 11, 31);
             }

             const fmt = d => {
                 const m = String(d.getMonth() + 1).padStart(2, '0');
                 const day = String(d.getDate()).padStart(2, '0');
                 return `${d.getFullYear()}-${m}-${day}`;
             };
             
             dFrom.value = fmt(from);
             dTo.value = fmt(to);
         }
     </script>
     {% endif %}"""

target_insertion = '     </form>\n     {% endif %}'
if 'class="quick-dates"' not in content:
    content = content.replace(target_insertion, target_insertion + html_to_insert)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Buttons moved below filters and redesigned.")
