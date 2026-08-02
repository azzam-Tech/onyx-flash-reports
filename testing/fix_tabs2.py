import codecs
import re

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

# 1. Fix global_vars and targets_ui in TABS
tabs_str = """    {
        "id": "global_vars",
        "title": " ",
        "icon": '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 0 0 2.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 0 0 1.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 0 0 -1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 0 0 -2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 0 0 -2.573 -1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 0 0 -1.065 -2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 0 0 1.066 -2.573c-.94-1.543.826-3.31 2.37-2.37.996.15 2.015-.267 2.572-1.065z" /><path d="M9 12a3 3 0 1 0 6 0a3 3 0 0 0 -6 0" />',
        "reports": [
            {
                "id": "targets_ui",
                "title": " ",
                "sql": "SELECT 1 FROM DUAL",
                "params": [],
                "cols": ["Dummy"]
            }
        ]
    }"""

tabs_new = """    {
        "id": "global_vars",
        "title": "المتغيرات العامة",
        "icon": "M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1zM12 15.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z",
        "reports": [
            {
                "id": "targets_ui",
                "title": "تارقت المناديب",
                "sql": "SELECT 1 FROM DUAL",
                "params": [],
                "cols": ["Dummy"]
            }
        ]
    }"""
content = content.replace(tabs_str, tabs_new)

# In case it failed because of mangled characters, fallback with regex
if "المتغيرات العامة" not in content:
    content = re.sub(r'\{\s*"id": "global_vars",.*?\]\s*\}', tabs_new, content, flags=re.DOTALL)


# 2. Inject the targets UI into PAGE
page_old = """     {% if error %}<div class="err">خطأ: {{error}}</div>
     {% else %}
       <div class="cnt">عدد الصفوف: {{rows|length}}</div>"""

page_new = """     {% if error %}<div class="err">خطأ: {{error}}</div>
     {% else %}
       {% if rpt.id == 'targets_ui' %}
         <style>
         .tw input[type=number] { width:70px; padding:6px; border:1px solid #cbd5e1; border-radius:6px; text-align:center; font-family:inherit; }
         .tw input[type=number]:focus { outline:none; border-color:#4f46e5; }
         .total-cell { font-weight:bold; color:#4f46e5; background:#f8fafc; }
         </style>
         <div class="rhead" style="justify-content:space-between">
           <select id="yearSelect" style="padding:8px; border-radius:6px; border:1px solid #cbd5e1; font-family:inherit; margin-bottom: 10px;">
             <option value="2024">2024</option>
             <option value="2025">2025</option>
             <option value="2026" selected>2026</option>
             <option value="2027">2027</option>
           </select>
           <button class="btn" onclick="saveTargets()" style="margin-bottom: 10px;">حفظ التعديلات</button>
         </div>
         <div class="tw" style="overflow-x:auto; max-height:70vh;">
           <table>
             <thead>
               <tr><th>كود</th><th style="min-width:150px;">المندوب</th><th>يناير</th><th>فبراير</th><th>مارس</th><th>أبريل</th><th>مايو</th><th>يونيو</th><th>يوليو</th><th>أغسطس</th><th>سبتمبر</th><th>أكتوبر</th><th>نوفمبر</th><th>ديسمبر</th><th>الإجمالي السنوي</th></tr>
             </thead>
             <tbody id="tbody"></tbody>
           </table>
         </div>
         <script>
          const backendData = {{ t_data | tojson | safe if t_data else '{}' }};
          const salesmen = {{ salesmen | tojson | safe if salesmen else '[]' }};
          const tbody = document.getElementById('tbody');
          const yearSelect = document.getElementById('yearSelect');
          
          function renderTable(year) {
            if(!tbody) return;
            tbody.innerHTML = '';
            const yearData = backendData[year] || {};
            
            salesmen.forEach(sm => {
              const tr = document.createElement('tr');
              const codeTd = document.createElement('td'); codeTd.textContent = sm.code; tr.appendChild(codeTd);
              const nameTd = document.createElement('td'); nameTd.textContent = sm.name; tr.appendChild(nameTd);
              
              const smData = yearData[sm.code] || {};
              let smTotal = 0;
              
              const inputs = [];
              for(let m=1; m<=12; m++) {
                const td = document.createElement('td');
                const input = document.createElement('input');
                input.type = 'number';
                input.dataset.code = sm.code;
                input.dataset.month = m;
                let val = smData[m] !== undefined ? smData[m] : 1000000;
                if(val > 0) input.value = val;
                smTotal += val;
                
                input.addEventListener('input', updateRowTotal);
                inputs.push(input);
                
                td.appendChild(input);
                tr.appendChild(td);
              }
              
              const totalTd = document.createElement('td');
              totalTd.className = 'total-cell';
              totalTd.textContent = smTotal.toLocaleString();
              tr.appendChild(totalTd);
              
              tr.inputs = inputs;
              tr.totalTd = totalTd;
              tbody.appendChild(tr);
            });
          }
          
          function updateRowTotal(e) {
            const tr = e.target.closest('tr');
            let sum = 0;
            tr.inputs.forEach(inp => {
              const v = parseFloat(inp.value);
              if(!isNaN(v)) sum += v;
            });
            tr.totalTd.textContent = sum.toLocaleString();
          }
          
          if(yearSelect) {
              yearSelect.addEventListener('change', () => renderTable(yearSelect.value));
              renderTable(yearSelect.value);
          }
          
          function saveTargets() {
            const year = yearSelect.value;
            const newData = { year: year, targets: {} };
            
            const rows = tbody.querySelectorAll('tr');
            rows.forEach(tr => {
              const inputs = tr.inputs;
              if(!inputs) return;
              inputs.forEach(inp => {
                const c = inp.dataset.code;
                const m = inp.dataset.month;
                const v = parseFloat(inp.value);
                if(!isNaN(v) && v > 0) {
                  if(!newData.targets[c]) newData.targets[c] = {};
                  newData.targets[c][m] = v;
                }
              });
            });
            
            fetch('/save_targets', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(newData)
            }).then(r => r.json()).then(res => {
              if(res.success) {
                alert('تم حفظ الأهداف بنجاح!');
                window.location.reload();
              } else {
                alert('خطأ: ' + res.error);
              }
            });
          }
         </script>
       {% else %}
       <div class="cnt">عدد الصفوف: {{rows|length}}</div>"""

# Just replace by regex since spaces could vary
import re
content = re.sub(r'\{%\s*if\s*error\s*%\}.*?\{%\s*else\s*%\}.*?<div class="cnt">', page_new.strip(), content, count=1, flags=re.DOTALL)

# Fix the endif tags at the end of the table
page_old2 = """       <tbody>{% for row in rows %}<tr>{% for cell in row %}<td>{{ '' if cell is none else cell }}</td>{% endfor %}</tr>{% endfor %}</tbody></table></div>
     {% endif %}
     {% endif %}
   </div>
 </div>"""

page_new2 = """       <tbody>{% for row in rows %}<tr>{% for cell in row %}<td>{{ '' if cell is none else cell }}</td>{% endfor %}</tr>{% endfor %}</tbody></table></div>
       {% endif %}
     {% endif %}
     {% endif %}
   </div>
 </div>"""

content = re.sub(r'<tbody>\{%\s*for\s*row\s*in\s*rows.*?\</div>\s*\{%\s*endif\s*%\}\s*\{%\s*endif\s*%\}\s*</div>\s*</div>', page_new2.strip(), content, count=1, flags=re.DOTALL)

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)
print("SUCCESS")
