import codecs
import re
import os

with codecs.open(r"privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

# 1. Update TABS array
new_global_vars = '''{
        "id": "global_vars",
        "title": "المتغيرات العامة",
        "icon": "M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 0 0 2.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 0 0 1.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 0 0 -1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 0 0 -2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 0 0 -2.573 -1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 0 0 -1.065 -2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 0 0 1.066 -2.573c-.94-1.543.826-3.31 2.37-2.37.996.15 2.015-.267 2.572-1.065z M9 12a3 3 0 1 0 6 0a3 3 0 0 0 -6 0",
        "reports": [
            {
                "id": "targets_ui",
                "title": "تارقت المناديب",
                "sql": "SELECT 1 FROM DUAL",
                "params": [],
                "cols": []
            }
        ]
    }'''

# Replace the old `global_vars` with the new one
content = re.sub(r'\{\s*"id":\s*"global_vars"[\s\S]*?"cols":\s*\[\]\s*\}\s*\]\s*\}', new_global_vars, content)
# Wait, in app_rebuild4, global_vars looks like:
# {"id": "global_vars", "title": " ", "icon": "<path .../>", "reports": [{"id": "targets_ui", ... "cols": []}]}
# I will use a simple approach: if "targets_ui" is inside "global_vars", I can just replace the title and icon.
content = content.replace('"title": " ",\n        "icon": \'<path', '"title": "المتغيرات العامة",\n        "icon": \'<path')
content = content.replace('\'<path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 0 0 2.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 0 0 1.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 0 0 -1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 0 0 -2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 0 0 -2.573 -1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 0 0 -1.065 -2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 0 0 1.066 -2.573c-.94-1.543.826-3.31 2.37-2.37.996.15 2.015-.267 2.572-1.065z" /><path d="M9 12a3 3 0 1 0 6 0a3 3 0 0 0 -6 0" />\'',
                          '"M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 0 0 2.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 0 0 1.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 0 0 -1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 0 0 -2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 0 0 -2.573 -1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 0 0 -1.065 -2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 0 0 1.066 -2.573c-.94-1.543.826-3.31 2.37-2.37.996.15 2.015-.267 2.572-1.065z M9 12a3 3 0 1 0 6 0a3 3 0 0 0 -6 0"')
content = content.replace('"title": " ",\n                "sql":', '"title": "تارقت المناديب",\n                "sql":')


# 2. Add backend logic
targets_backend = """
import json
import os
TARGETS_FILE = os.path.join(os.path.dirname(__file__), 'targets.json')

def _load_targets_raw():
    if os.path.exists(TARGETS_FILE):
        try:
            with open(TARGETS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_targets_to_file(data):
    with open(TARGETS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route("/save_targets", methods=["POST"])
def save_targets():
    try:
        data = request.json
        save_targets_to_file(data)
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500
"""
if "def save_targets():" not in content:
    content = content.replace("@app.route(\"/\")", targets_backend + "\n@app.route(\"/\")")


# 3. Update index()
if "t_data =" not in content:
    content = content.replace(
        "return render_template_string(PAGE, tabs=TABS",
        """
    t_data = {}
    salesmen = []
    if rpt["id"] == "targets_ui":
        t_data = _load_targets_raw()
        try:
            with get_conn() as con:
                with con.cursor() as cur:
                    cur.execute("SELECT REPRS_CODE, REPRS_A_NAME FROM IAS20261.SALES_MAN WHERE NVL(STOP_ACC, 0) = 0 ORDER BY REPRS_CODE")
                    salesmen = [{"code": str(r[0]), "name": r[1]} for r in cur.fetchall()]
        except Exception as e:
            error = str(e)
            
    return render_template_string(PAGE, t_data=t_data, salesmen=salesmen, tabs=TABS"""
    )


# 4. Safely inject into PAGE
page_ui_block = """{% if rpt.id == 'targets_ui' %}
         <style>
         .tw input[type=number] { width:80px; padding:6px; border:1px solid #cbd5e1; border-radius:6px; text-align:center; font-family:inherit; }
         .tw input[type=number]:focus { outline:none; border-color:#4f46e5; }
         .total-cell { font-weight:bold; color:#4f46e5; background:#f8fafc; }
         </style>
         <div class="rhead" style="justify-content:space-between">
           <select id="yearSelect" onchange="renderTable(this.value)" style="padding:8px; border-radius:6px; border:1px solid #cbd5e1; font-family:inherit; margin-bottom: 10px;">
             <option value="2024">2024</option>
             <option value="2025">2025</option>
             <option value="2026" selected>2026</option>
             <option value="2027">2027</option>
           </select>
           <button class="btn" onclick="saveTargets()" style="margin-bottom: 10px; background:#10b981;">حفظ التغييرات</button>
         </div>
         <div class="tw" style="overflow-x:auto; max-height:70vh;">
           <table>
             <thead>
               <tr><th>الكود</th><th style="min-width:150px;">الاسم</th>
               <th>يناير</th><th>فبراير</th><th>مارس</th><th>أبريل</th><th>مايو</th><th>يونيو</th>
               <th>يوليو</th><th>أغسطس</th><th>سبتمبر</th><th>أكتوبر</th><th>نوفمبر</th><th>ديسمبر</th>
               <th>الإجمالي</th></tr>
             </thead>
             <tbody id="tbody"></tbody>
           </table>
         </div>
         <script>
          let backendData = {{ t_data | tojson | safe if t_data else '{}' }};
          const salesmen = {{ salesmen | tojson | safe if salesmen else '[]' }};
          const tbody = document.getElementById('tbody');
          const yearSelect = document.getElementById('yearSelect');
          
          function renderTable(year) {
            if(!tbody) return;
            tbody.innerHTML = '';
            if(!backendData[year]) backendData[year] = {};
            const yearData = backendData[year];
            
            salesmen.forEach(sm => {
              const tr = document.createElement('tr');
              const codeTd = document.createElement('td'); codeTd.textContent = sm.code; tr.appendChild(codeTd);
              const nameTd = document.createElement('td'); nameTd.textContent = sm.name; tr.appendChild(nameTd);
              
              if(!yearData[sm.code]) yearData[sm.code] = {};
              const smData = yearData[sm.code];
              
              let smTotal = 0;
              const inputs = [];
              for(let m=1; m<=12; m++) {
                const td = document.createElement('td');
                const input = document.createElement('input');
                input.type = 'number';
                input.dataset.code = sm.code;
                input.dataset.month = m;
                let val = smData[m];
                if(val === undefined) { val = 1000000; smData[m] = val; }
                input.value = val;
                
                input.addEventListener('change', (e) => {
                   smData[m] = parseFloat(e.target.value) || 0;
                   updateTotals();
                });
                
                inputs.push(input);
                td.appendChild(input);
                tr.appendChild(td);
                smTotal += val;
              }
              const totalTd = document.createElement('td');
              totalTd.className = 'total-cell';
              totalTd.textContent = smTotal.toLocaleString();
              tr.dataset.code = sm.code;
              tr.appendChild(totalTd);
              tbody.appendChild(tr);
            });
          }
          
          function updateTotals() {
            const year = yearSelect.value;
            const yearData = backendData[year];
            Array.from(tbody.children).forEach(tr => {
               const code = tr.dataset.code;
               if(!code) return;
               let tot = 0;
               for(let m=1; m<=12; m++) {
                  tot += (yearData[code][m] || 0);
               }
               tr.querySelector('.total-cell').textContent = tot.toLocaleString();
            });
          }
          
          function saveTargets() {
            fetch('/save_targets', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(backendData)
            })
            .then(res => res.json())
            .then(data => {
              if(data.status === 'success') alert('تم حفظ البيانات بنجاح!');
              else alert('حدث خطأ: ' + data.message);
            })
            .catch(err => alert('حدث خطأ بالاتصال'));
          }
          
          document.addEventListener("DOMContentLoaded", () => {
             if(yearSelect) renderTable(yearSelect.value);
          });
         </script>
       {% else %}"""

if "{% if rpt.id == 'targets_ui' %}" not in content:
    # Safely replace the else block using regex to avoid exact character issues (like Arabic encoding)
    content = re.sub(
        r'(\{% else %\}\s*<div class="cnt">)', 
        page_ui_block + r'\n       <div class="cnt">', 
        content
    )
    # Add {% endif %} before the final </div> of the table block
    # We find the table block end which looks like </tbody></table></div>\n     {% endif %}
    content = re.sub(
        r'(</tbody></table></div>\s*\{% endif %\}\s*\{% endif %\}\s*</div>)',
        r'</tbody></table></div>\n       {% endif %}\n     {% endif %}\n     {% endif %}\n   </div>',
        content
    )

with codecs.open(r"privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)

print("Targets UI successfully applied!")
