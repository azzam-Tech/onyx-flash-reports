import re
import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

replacement = """def run_report(rpt, args):
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
        if "p_year" in binds and "p_type" in binds:
            d_from, d_to = calculate_dates(binds["p_year"], binds["p_type"], binds.get("p_val", 1))
            binds["date_from"] = d_from
            binds["date_to"] = d_to
            
        # Oracle throws ORA-01036 if we pass bind variables that aren't in the query.
        import re
        sql = rpt["sql"]
        used_binds = set(re.findall(r':([a-zA-Z0-9_]+)', sql))
        filtered_binds = {k: v for k, v in binds.items() if k in used_binds}
            
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute(sql, filtered_binds)"""

content = re.sub(
    r'def run_report\(rpt, args\):.*?cur\.execute\(rpt\["sql"\], binds\)',
    replacement,
    content,
    flags=re.DOTALL
)

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)
print("SUCCESS")
