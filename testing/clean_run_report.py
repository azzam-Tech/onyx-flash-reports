import re
import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

correct_run_report = """def run_report(rpt, args):
    if rpt["id"] in ["perf_aging", "perf_aging_dynamic"]:
        cols, rows = run_perf_aging_fifo(rpt, args)
    elif rpt["id"] == "perf_aging_dynamic_analytical":
        cols, rows = run_perf_aging_analytical(rpt, args)
    elif rpt["id"] == "main_wh_movement":
        cols, rows = run_main_wh_movement(rpt, args)
    else:
        binds = {}
        for p in rpt["params"]:
            v = args.get(p["name"], p.get("default",""))
            if p["type"] == "number":
                try: v = int(v)
                except: v = 0
                binds[p["name"]] = v
            else:
                if p["name"] in ("rep_code","c_code","v_code","i_code","a_code","w_code") and v:
                    v = v.split(" - ")[0].strip()
                binds[p["name"]] = v if v != "" else None
        
        # Inject dynamic dates if this report uses dynamic period params
        target_year = "2026" # fallback
        if "p_year" in binds and "p_type" in binds:
            target_year = str(binds["p_year"])
            d_from, d_to = calculate_dates(binds["p_year"], binds["p_type"], binds.get("p_val", 1))
            binds["date_from"] = d_from
            binds["date_to"] = d_to
        elif "date_from" in binds and binds["date_from"]:
            target_year = str(binds["date_from"])[:4]
            
        import re
        sql = rpt["sql"]
        
        if target_year.isdigit() and len(target_year) == 4:
            sql = sql.replace('IAS20261', f'IAS{target_year}1')
            
        used_binds = set(re.findall(r':([a-zA-Z0-9_]+)', sql))
        filtered_binds = {k: v for k, v in binds.items() if k in used_binds}
            
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute(sql, filtered_binds)
                cols = [d[0] for d in cur.description]
                rows = cur.fetchall()

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

    sort_col = args.get('sort_col')"""

# The original content has 'sort_col = args.get('sort_col')'
# We will match from 'def run_report' up to 'sort_col = args.get('sort_col')'
content = re.sub(
    r'def run_report\(rpt, args\):.*?sort_col = args\.get\(\'sort_col\'\)',
    correct_run_report,
    content,
    flags=re.DOTALL
)

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)
print("SUCCESS")
