import sys
import re

app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS
css_to_add = """
.quick-dates { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 24px; justify-content: center; background: var(--card-bg); padding: 16px; border-radius: 20px; box-shadow: var(--sh); }
.quick-dates .btn-sm { background: #f8fafc; border: 1px solid var(--line); color: var(--ink-dark); padding: 8px 16px; border-radius: 12px; font-size: 13px; font-weight: 700; cursor: pointer; transition: 0.2s; }
.quick-dates .btn-sm:hover { background: var(--primary); border-color: var(--primary); color: #fff; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(79,70,229,0.2); }
</style>"""

if '.quick-dates' not in content:
    content = content.replace('</style>', css_to_add)

# 2. Add HTML & JS
html_to_add = """      </form>
      {% endif %}
      
      {% if rpt.params and 'date_from' in rpt.params|map(attribute='name') %}
        <div class="quick-dates">
           <button class="btn-sm" onclick="setDates('today')">اليوم</button>
           <button class="btn-sm" onclick="setDates('this_week')">هذا الأسبوع</button>
           <button class="btn-sm" onclick="setDates('this_month')">هذا الشهر</button>
           <button class="btn-sm" onclick="setDates('last_month')">الشهر السابق</button>
           <button class="btn-sm" onclick="setDates('this_year')">هذه السنة</button>
           <button class="btn-sm" onclick="setDates('last_year')">السنة السابقة</button>
        </div>
        <script>
           function setDates(range) {
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
                   // Sunday as start of week (0), if week starts on Monday, adjust logic.
                   // Let's use standard Date math
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

if 'class="quick-dates"' not in content:
    content = content.replace('      </form>\n      {% endif %}', html_to_add)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Quick Date filters added successfully.")
