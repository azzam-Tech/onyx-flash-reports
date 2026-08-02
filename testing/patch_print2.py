import codecs
import re

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

print_func = """@app.route("/print")
def printview():
    tab, rpt = find_report(request.args.get("tab", TABS[0]["id"]), request.args.get("report",""))
    try:
        cols, rows = run_report(rpt, request.args)
        model = request.args.get("model", "1")
        if model == "2" and rpt["id"] == "collection_adopted":
            new_cols = ["الرمز", "الاسم / الوصف", "إجمالي السندات", "قيود الشبكة المنفصلة", "صافي المبيعات النقدية", "الإجمالي النهائي"]
            new_rows = []
            for r in rows:
                def parse_num(v):
                    if not v: return 0.0
                    if isinstance(v, str):
                        try: return float(v.replace(',',''))
                        except: return 0.0
                    return float(v)
                
                tot_rcpt = parse_num(r[2]) + parse_num(r[3]) + parse_num(r[4])
                net_jrn = parse_num(r[6])
                net_cash = parse_num(r[7]) - parse_num(r[10])
                final_tot = tot_rcpt + net_jrn + net_cash
                
                fmt = lambda x: f"{x:,.2f}" if x != 0 else "0.00"
                new_rows.append((r[0], r[1], fmt(tot_rcpt), fmt(net_jrn), fmt(net_cash), fmt(final_tot)))
            
            cols = new_cols
            rows = new_rows

    except Exception as e:
        return "خطأ: " + str(e), 500
    filt = []
    for p in rpt["params"]:
        v = request.args.get(p["name"], p.get("default",""))
        if v not in ("", None): filt.append((p["label"], v))
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    title = rpt["title"] + (" (نموذج 2)" if request.args.get("model") == "2" else "")
    return render_template_string(PRINT_PAGE, title=title, cols=cols, rows=rows, filt=filt, now=now)"""

# replace old printview
content = re.sub(r'@app\.route\("/print"\)[\s\S]*?return render_template_string\(PRINT_PAGE, title=rpt\["title"\], cols=cols, rows=rows, filt=filt, now=now\)', print_func, content)

page_old_part = """<div class="rhead">
  <h1>{{ rpt.title }}</h1>
  <div class="exps">
    <a class="exp xl" href="/export?{{qs}}&format=xlsx">Excel</a>
    {% if rpt.id == 'collection_adopted' %}
      <a class="exp pf" href="/print?{{qs}}&model=1" target="_blank">PDF نموذج 1</a>
      <a class="exp pf" style="background:#059669;" href="/print?{{qs}}&model=2" target="_blank">PDF نموذج 2</a>
    {% else %}
      <a class="exp pf" href="/print?{{qs}}" target="_blank">PDF</a>
    {% endif %}
  </div>
</div>"""

# Revert my previous mistake and add dropdown.
# For the dropdown we can do a simple select element and a button next to it. Or a simple button that opens a small menu.
# It's easiest to just make a <select> if it's collection_adopted and a <button> that triggers window.open.
# Let's write the HTML for it:

dropdown_html = """<div class="rhead">
  <h1>{{ rpt.title }}</h1>
  <div class="exps">
    <a class="exp xl" href="/export?{{qs}}&format=xlsx">Excel</a>
    {% if rpt.id == 'collection_adopted' %}
      <select id="pdfModel" style="padding:4px 8px; border:1px solid #cbd5e1; border-radius:4px; margin-left:4px; font-family:inherit; font-size:13px;">
        <option value="1">PDF (النموذج الافتراضي)</option>
        <option value="2">PDF (نموذج 2)</option>
      </select>
      <button class="exp pf" style="border:none; cursor:pointer;" onclick="window.open('/print?{{qs|safe}}&model=' + document.getElementById('pdfModel').value, '_blank')">طباعة</button>
    {% else %}
      <a class="exp pf" href="/print?{{qs}}" target="_blank">PDF</a>
    {% endif %}
  </div>
</div>"""

content = content.replace(page_old_part, dropdown_html)

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)

print("Patch applied")
