import codecs
import re

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

# 1. Remove custom_route from targets_ui
targets_ui_str = """                "title": "تارقت المناديب",
                "custom_route": "/targets_ui",
                "sql": "SELECT 1 FROM DUAL","""

targets_ui_new = """                "title": "تارقت المناديب",
                "sql": "SELECT 1 FROM DUAL","""
content = content.replace(targets_ui_str, targets_ui_new)

# 2. Add icon to global_vars if missing
icon_regex = r'("id": "global_vars",\s*"title": "المتغيرات العامة",\s*"icon": \').*?(\',)'
new_icon = r'\1<path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 0 0 2.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 0 0 1.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 0 0 -1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 0 0 -2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 0 0 -2.573 -1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 0 0 -1.065 -2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 0 0 1.066 -2.573c-.94-1.543.826-3.31 2.37-2.37.996.15 2.015-.267 2.572-1.065z" /><path d="M9 12a3 3 0 1 0 6 0a3 3 0 0 0 -6 0" />\2'
content = re.sub(icon_regex, new_icon, content, count=1, flags=re.DOTALL)

# 3. Update index() to fetch targets data and pass to template
index_str = """    error = None; cols=[]; rows=[]; dash=None
    if rpt.get("custom_route"):
        return redirect(rpt["custom_route"])
    if tab.get("dash"):"""

index_new = """    error = None; cols=[]; rows=[]; dash=None; t_data={}; salesmen=[]
    if rpt.get("custom_route"):
        return redirect(rpt["custom_route"])
    if rpt["id"] == "targets_ui":
        t_data = _load_targets_raw()
        try:
            with get_conn() as con:
                with con.cursor() as cur:
                    cur.execute("SELECT REPRS_CODE, REPRS_A_NAME FROM IAS20261.SALES_MAN ORDER BY TO_NUMBER(REPRS_CODE) ASC")
                    for r in cur.fetchall():
                        salesmen.append({"code": str(r[0]), "name": str(r[1])})
        except Exception as e:
            error = str(e)
    elif tab.get("dash"):"""
content = content.replace(index_str, index_new)

render_str = """    return render_template_string(PAGE, tabs=TABS, tab=tab, cur_tab=cur_tab, rpt=rpt,
                                  binds=display, cols=cols, rows=rows, error=error, qs=qs, dash=dash, hidden_tabs=hidden_tabs, hidden_reports=hidden_reports, hide_profit=request.args.get("hide_profit", "0")=="1")"""

render_new = """    return render_template_string(PAGE, tabs=TABS, tab=tab, cur_tab=cur_tab, rpt=rpt,
                                  binds=display, cols=cols, rows=rows, error=error, qs=qs, dash=dash, hidden_tabs=hidden_tabs, hidden_reports=hidden_reports, hide_profit=request.args.get("hide_profit", "0")=="1", t_data=t_data, salesmen=salesmen)"""
content = content.replace(render_str, render_new)

# 4. Modify PAGE to include targets UI
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
content = content.replace(page_old, page_new)

# 5. Make sure the endif matches the new if
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
content = content.replace(page_old2, page_new2)

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)
print("SUCCESS")
