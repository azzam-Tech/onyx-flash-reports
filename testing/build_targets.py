import re
import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

# 1. Add TARGETS_FILE and load/save functions
targets_funcs = """
TARGETS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "targets.json")
def _load_targets_raw():
    try:
        with open(TARGETS_FILE, "r", encoding="utf-8") as f: return json.load(f)
    except Exception: return {}
def save_targets_to_file(data):
    with open(TARGETS_FILE, "w", encoding="utf-8") as f: json.dump(data, f, ensure_ascii=False)
"""
if "TARGETS_FILE =" not in content:
    content = content.replace("SETTINGS_FILE = ", targets_funcs + "\nSETTINGS_FILE = ")


# 2. Add /targets_ui and /save_targets routes
targets_routes = """
TARGETS_PAGE = \"\"\"<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
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
.btn-back { background:#64748b; margin-left:10px; text-decoration:none; display:inline-block; }
.btn-back:hover { background:#475569; }
table { width:100%; border-collapse:collapse; margin-top:20px; font-size:14px; }
th, td { border:1px solid #e2e8f0; padding:8px; text-align:center; }
th { background:#f8fafc; color:#475569; position:sticky; top:0; z-index:1; }
input[type=number] { width:80px; padding:6px; border:1px solid #cbd5e1; border-radius:6px; text-align:center; font-family:inherit; }
input[type=number]:focus { outline:none; border-color:#4f46e5; }
.total-cell { font-weight:bold; color:#4f46e5; background:#f8fafc; }
</style>
</head>
<body>
  <div class="card">
    <div class="header">
      <h2>تارقت المناديب</h2>
      <div>
        <select id="yearSelect">
          <option value="2024">2024</option>
          <option value="2025">2025</option>
          <option value="2026" selected>2026</option>
          <option value="2027">2027</option>
        </select>
        <button onclick="saveTargets()">حفظ التعديلات</button>
        <a href="/" class="btn-back button">عودة للرئيسية</a>
      </div>
    </div>
    
    <div style="overflow-x:auto; max-height:75vh;">
    <table>
      <thead>
        <tr>
          <th>كود</th>
          <th style="min-width:150px;">المندوب</th>
          <th>يناير</th><th>فبراير</th><th>مارس</th><th>أبريل</th><th>مايو</th><th>يونيو</th>
          <th>يوليو</th><th>أغسطس</th><th>سبتمبر</th><th>أكتوبر</th><th>نوفمبر</th><th>ديسمبر</th>
          <th>الإجمالي السنوي</th>
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
        let val = smData[m] || 0;
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
        alert('تم الحفظ بنجاح!');
      } else {
        alert('حدث خطأ أثناء الحفظ');
      }
    });
  }
  
  // init
  renderTable(yearSelect.value);
</script>
</body></html>\"\"\"

from flask import jsonify

@app.route("/targets_ui")
def targets_ui():
    hidden_tabs, _ = load_hidden()
    if "global_vars" in hidden_tabs: return "Access Denied"
    
    # Get all salesmen from onyx
    salesmen = []
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                # Dynamic year routing logic applies here if needed, but SALES_MAN is usually same across schemas.
                # Just query the 2026 schema for salesmen list.
                cur.execute("SELECT REPRS_CODE, REPRS_A_NAME FROM IAS20261.SALES_MAN ORDER BY TO_NUMBER(REPRS_CODE) ASC")
                for r in cur.fetchall():
                    salesmen.append({"code": str(r[0]), "name": str(r[1])})
    except Exception as e:
        print("Salesman fetch error:", e)
    
    t_data = _load_targets_raw()
    return render_template_string(TARGETS_PAGE, data=t_data, salesmen=salesmen)

@app.route("/save_targets", methods=["POST"])
def save_targets():
    try:
        data = request.json
        save_targets_to_file(data)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
"""
if "@app.route(\"/targets_ui\")" not in content:
    # insert before @app.route("/")
    content = content.replace('@app.route("/")', targets_routes + '\n@app.route("/")')

# 3. Add to TABS
global_vars_tab = """
 ,{"id":"global_vars","title":"المتغيرات العامة","icon":"M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4","reports":[
    {"id":"salesman_targets","title":"تارقت المناديب","custom_route":"/targets_ui"}
 ]}"""
if '"id":"global_vars"' not in content:
    # Add it after the sales tab or at the end of TABS list. Let's insert before the closing bracket of TABS.
    # We can replace ']\n\n# --- INDEX_PAGE ---' or just find the end of TABS
    content = re.sub(r'(\n\]\s*\n\s*DFROM =)', global_vars_tab + r'\1', content)
    # Wait, TABS is at the top or bottom? TABS is initialized after DFROM!
    # Let's just find the end of TABS array.
    # A safe way is to replace '\n]\n\n@app.before_request' if it exists.
    # Let's use a regex that matches the end of TABS.
    pass

# safer injection for TABS:
if '"id":"global_vars"' not in content:
    # Find the end of TABS list
    m = re.search(r'TABS\s*=\s*\[.*?(?=^@|^def|PAGE =|LOGIN_PAGE =|PRINT_PAGE =)', content, re.DOTALL | re.MULTILINE)
    if m:
        tabs_block = m.group(0)
        new_tabs_block = tabs_block.rstrip()
        if new_tabs_block.endswith(']'):
            new_tabs_block = new_tabs_block[:-1] + global_vars_tab + '\n]'
            content = content.replace(tabs_block, new_tabs_block)


# 4. Update index route to redirect custom_route
# find 'if tab.get("dash"):'
if 'elif rpt.get("custom_route"):' not in content:
    content = content.replace(
        'if tab.get("dash"):',
        'if rpt.get("custom_route"):\n        return redirect(rpt["custom_route"])\n    if tab.get("dash"):'
    )

# 5. Inject targets into sales_vs_collection rows
inject_logic = """
        if rpt["id"] == "sales_vs_collection" and rows:
            t_data = _load_targets_raw()
            year = str(target_year)
            ptype = str(binds.get("p_type", "month"))
            pval = str(binds.get("p_val", "1"))
            
            new_rows = []
            target_col_idx = cols.index("التارقت") if "التارقت" in cols else -1
            if target_col_idx != -1:
                for row in rows:
                    rep_code = str(row[0]).strip() if row[0] else ""
                    target_val = 0
                    if year in t_data and rep_code in t_data[year]:
                        rep_t = t_data[year][rep_code]
                        if ptype == "month":
                            target_val = rep_t.get(pval, 0)
                        elif ptype == "quarter":
                            q = int(pval)
                            months = [str((q-1)*3 + i) for i in (1,2,3)]
                            target_val = sum(rep_t.get(m, 0) for m in months)
                        elif ptype == "half":
                            h = int(pval)
                            months = [str((h-1)*6 + i) for i in (1,2,3,4,5,6)]
                            target_val = sum(rep_t.get(m, 0) for m in months)
                        elif ptype == "year":
                            target_val = sum(rep_t.get(str(m), 0) for m in range(1,13))
                    
                    fmt_target = "{:,.2f}".format(target_val) if target_val else ""
                    row_list = list(row)
                    row_list[target_col_idx] = fmt_target
                    new_rows.append(tuple(row_list))
                rows = new_rows
"""

if 'if rpt["id"] == "sales_vs_collection" and rows:' not in content:
    content = content.replace(
        'cur.execute(sql, filtered_binds)',
        'cur.execute(sql, filtered_binds)\n                cols = [d[0] for d in cur.description]\n                rows = cur.fetchall()'
    )
    # The original has:
    # cur.execute(sql, filtered_binds)
    # cols = [d[0] for d in cur.description]
    # rows = cur.fetchall()
    # Let's just append it after rows = cur.fetchall()
    
    find_str = "rows = cur.fetchall()"
    content = content.replace(find_str, find_str + inject_logic)


with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)
print("SUCCESS")
