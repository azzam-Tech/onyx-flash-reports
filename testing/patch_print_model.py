import codecs
import re

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

# Add a model parameter to /print and logic for Model 2
print_route_old = """@app.route("/print")
def printview():
    tab, rpt = find_report(request.args.get("tab", TABS[0]["id"]), request.args.get("report",""))
    try:
        cols, rows = run_report(rpt, request.args)
        filt = []
        for p in rpt.get("params", []):
            v = request.args.get(p["name"], p.get("default",""))
            if v not in ("", None): filt.append((p["label"], v))
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        return render_template_string(PRINT_PAGE, title=rpt["title"], cols=cols, rows=rows, filt=filt, now=now)
    except Exception as e:
        return f"<h1>Error</h1><p>{str(e)}</p>"
"""

print_route_new = """@app.route("/print")
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
                
                # Indexes: 
                # 0: code, 1: name
                # 2: rcpt, 3: unp_rcpt, 4: unp_unk, 5: rcp_unk, 6: net_jrn, 7: cash_sales, 8: inv_disc, 9: ext_notice, 10: cash_ret, 11: total
                tot_rcpt = parse_num(r[2]) + parse_num(r[3]) + parse_num(r[4])
                net_jrn = parse_num(r[6])
                net_cash = parse_num(r[7]) - parse_num(r[10])
                # Should we use the original total or sum these 3? We'll sum these 3 plus anything else they wanted, or just total_inc (11).
                # They didn't mention other things for the total, let's use the new total of these 3.
                final_tot = tot_rcpt + net_jrn + net_cash
                
                fmt = lambda x: f"{x:,.2f}" if x != 0 else "0.00"
                new_rows.append((r[0], r[1], fmt(tot_rcpt), fmt(net_jrn), fmt(net_cash), fmt(final_tot)))
            
            cols = new_cols
            rows = new_rows

        filt = []
        for p in rpt.get("params", []):
            v = request.args.get(p["name"], p.get("default",""))
            if v not in ("", None): filt.append((p["label"], v))
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        title = rpt["title"] + (" (نموذج 2)" if model == "2" else "")
        return render_template_string(PRINT_PAGE, title=title, cols=cols, rows=rows, filt=filt, now=now)
    except Exception as e:
        return f"<h1>Error</h1><p>{str(e)}</p>"
"""

content = content.replace(print_route_old, print_route_new)

# Update HTML for Export PDF Dropdown/Buttons
# In PAGE, we have:
# <div class="exps"><a class="exp xl" href="/export?{{qs}}&format=xlsx">Excel</a><a class="exp pf" href="/print?{{qs}}" target="_blank">PDF</a></div></div>
page_old = """<div class="rhead"><h1>{{ rpt.title }}</h1><div class="exps"><a class="exp xl" href="/export?{{qs}}&format=xlsx">Excel</a><a class="exp pf" href="/print?{{qs}}" target="_blank">PDF</a></div></div>"""

page_new = """<div class="rhead">
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

content = content.replace(page_old, page_new)

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)
print("Updated /print route and PDF buttons")
