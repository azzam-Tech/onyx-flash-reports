with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

target = "def jv_options():"

replacement = """def run_sql_report(rpt, args):
    sql = rpt["sql"]
    binds = {}
    for p in rpt["params"]:
        pname = p["name"]
        raw = args.get(pname, p.get("default", ""))
        val = str(raw).split(" - ")[0].strip() if raw else ""
        if p.get("type") in ("date", "month"):
            val = val or ("2026-01-01" if "from" in pname else "2026-12-31")
        binds[pname] = val
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute(sql, binds)
            cols = [d[0] for d in cur.description] if cur.description else []
            rows = cur.fetchall()
            sort_col = args.get("sort_col")
            sort_dir = args.get("sort_dir", "desc")
            if sort_col and sort_col in cols and rows:
                col_idx = cols.index(sort_col)
                def parse_sort_val(r):
                    v = r[col_idx]
                    if v is None: return float('-inf') if sort_dir == 'asc' else float('inf')
                    if isinstance(v, (int, float)): return v
                    if isinstance(v, str):
                        try: return float(v.replace(',', ''))
                        except: return v
                    return str(v)
                rows.sort(key=parse_sort_val, reverse=(sort_dir == 'desc'))
            return cols, rows

def run_report(rpt, args):
    if "fn" in rpt:
        func = globals().get(rpt["fn"])
        if func:
            cols, rows = func(rpt, args)
            return add_total_row(cols, rows)
    if not rpt.get("sql"):
        return [], []
    cols, rows = run_sql_report(rpt, args)
    return add_total_row(cols, rows)

def jv_options():"""

if target in content and "def run_report(rpt, args):" not in content:
    content = content.replace(target, replacement)
    with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully restored run_sql_report and run_report in app.py!")
else:
    print("Already exists or target not found.")
