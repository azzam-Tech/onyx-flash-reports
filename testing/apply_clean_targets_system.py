import re

with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean TARGETS_PAGE string with proper UTF-8 Arabic text
targets_page_clean = '''TARGETS_PAGE = """<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<title>تارقت المناديب</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
body { margin:0; padding:20px; font-family:'Cairo',sans-serif; background:#f4f5f8; color:#1e293b; }
.card { background:#fff; padding:20px; border-radius:12px; box-shadow:0 5px 15px rgba(0,0,0,0.05); }
.header { display:flex; justify-content:space-between; align-items:center; margin-bottom:20px; }
h2 { margin:0; color:#4f46e5; }
select { padding:10px; border-radius:8px; border:1px solid #cbd5e1; font-family:inherit; outline:none; }
button { padding:10px 20px; background:#4f46e5; color:#fff; border:none; border-radius:8px; font-weight:bold; cursor:pointer; font-family:inherit; }
button:hover { background:#4338ca; }
.btn-back { background:#64748b; color:#fff; padding:10px 20px; border-radius:8px; text-decoration:none; display:inline-block; font-weight:bold; margin-right:10px; }
.btn-back:hover { background:#475569; }
table { width:100%; border-collapse:collapse; margin-top:20px; font-size:14px; }
th, td { border:1px solid #e2e8f0; padding:8px; text-align:center; }
th { background:#f8fafc; color:#475569; position:sticky; top:0; z-index:1; }
input[type=number] { width:90px; padding:6px; border:1px solid #cbd5e1; border-radius:6px; text-align:center; font-family:inherit; font-weight:600; }
input[type=number]:focus { outline:none; border-color:#4f46e5; }
.total-cell { font-weight:bold; color:#4f46e5; background:#f8fafc; }
</style>
</head>
<body>
  <div class="card">
    <div class="header">
      <h2>تارقت المناديب (المتغيرات العامة)</h2>
      <div>
        <select id="yearSelect">
          <option value="2024">2024</option>
          <option value="2025">2025</option>
          <option value="2026" selected>2026</option>
          <option value="2027">2027</option>
        </select>
        <button onclick="saveTargets()">حفظ البيانات</button>
        <a href="/" class="btn-back">الرجوع للرئيسية</a>
      </div>
    </div>
    
    <div style="overflow-x:auto; max-height:75vh;">
    <table>
      <thead>
        <tr>
          <th>الكود</th>
          <th style="min-width:160px;">اسم المندوب</th>
          <th>يناير</th><th>فبراير</th><th>مارس</th><th>أبريل</th><th>مايو</th><th>يونيو</th>
          <th>يوليو</th><th>أغسطس</th><th>سبتمبر</th><th>أكتوبر</th><th>نوفمبر</th><th>ديسمبر</th>
          <th>الإجمالي</th>
        </tr>
      </thead>
      <tbody id="tbody">
        <!-- populated by js -->
      </tbody>
    </table>
    </div>
  </div>

<script>
  const backendData = {{ data | tojson }};
  const salesmen = {{ salesmen | tojson }};
  const tbody = document.getElementById('tbody');
  const yearSelect = document.getElementById('yearSelect');
  
  function renderTable(year) {
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
  
  yearSelect.addEventListener('change', () => renderTable(yearSelect.value));
  
  function saveTargets() {
    const year = yearSelect.value;
    if(!backendData[year]) backendData[year] = {};
    
    Array.from(tbody.children).forEach(tr => {
      const code = tr.inputs[0].dataset.code;
      const smObj = {};
      let hasData = false;
      tr.inputs.forEach(inp => {
        const v = parseFloat(inp.value);
        if(!isNaN(v) && v > 0) {
          smObj[inp.dataset.month] = v;
          hasData = true;
        }
      });
      if(hasData) {
        backendData[year][code] = smObj;
      } else {
        delete backendData[year][code];
      }
    });
    
    fetch('/save_targets', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(backendData)
    }).then(r => r.json()).then(res => {
      if(res.success) {
        alert('تم حفظ البيانات بنجاح!');
      } else {
        alert('حدث خطأ في حفظ البيانات');
      }
    });
  }
  
  // init
  renderTable(yearSelect.value);
</script>
</body></html>"""'''

# 2. Replace TARGETS_PAGE definition in content
content = re.sub(r'TARGETS_PAGE\s*=\s*"""[\s\S]*?"""', targets_page_clean, content)


# 3. Clean up TABS global_vars entry
new_global_vars = '''    {
        "id": "global_vars",
        "title": "المتغيرات العامة",
        "icon": "M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 0 0 2.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 0 0 1.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 0 0 -1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 0 0 -2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 0 0 -2.573 -1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 0 0 -1.065 -2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 0 0 1.066 -2.573c-.94-1.543.826-3.31 2.37-2.37.996.15 2.015-.267 2.572-1.065z M9 12a3 3 0 1 0 6 0a3 3 0 0 0 -6 0",
        "reports": [
            {
                "id": "targets_ui",
                "title": "تارقت المناديب",
                "custom_route": "/targets_ui",
                "params": [],
                "sql": ""
            }
        ]
    }'''

# Replace the TABS entry for global_vars
content = re.sub(r'\{\s*"id":\s*"global_vars"[\s\S]*?\n\s*\}', new_global_vars, content)


# 4. Remove any duplicate or injected Jinja code from PAGE if present
# Ensure PAGE has standard Jinja syntax
if "{% if rpt.id == 'targets_ui' %}" in content:
    # Remove the inline injection so that it relies purely on custom_route redirection
    content = content.replace("{% if rpt.id == 'targets_ui' %}", "")

with open(r'privet\onyx_reports\app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Targets System successfully cleaned and restored!")
