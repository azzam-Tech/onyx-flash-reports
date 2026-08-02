def run_report(rpt, args):
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
            
        # Oracle throws ORA-01036 if we pass bind variables that aren't in the query.
        import re
        sql = rpt["sql"]
        
        # Dynamic Year Routing: Onyx stores data in schema per year, e.g. IAS20251 for 2025
        # So we dynamically replace the hardcoded IAS20261 with IAS[year]1
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

                
    sort_col = args.get('sort_col')
    sort_dir = args.get('sort_dir')
    if sort_col and sort_dir and rows:
        try:
            sort_idx = cols.index(sort_col)
            
            def sort_key(row):
                val = row[sort_idx]
                if val is None: return (-float('inf'), "")
                if isinstance(val, (int, float)): return (val, "")
                if isinstance(val, str):
                    try:
                        return (float(val.replace(',', '')), "")
                    except ValueError:
                        return (0, val)
                return (0, str(val))
                
            rows.sort(key=sort_key, reverse=(sort_dir == 'desc'))
        except ValueError:
            pass
            
    return add_total_row(cols, rows)

_JV_CACHE = None
def jv_options():
    global _JV_CACHE
    if _JV_CACHE is not None:
        return _JV_CACHE
    opts = [["","الكل"]]
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute("""SELECT p.JV_TYPE, MAX(j.JV_NAME) nm
                    FROM IAS20261.IAS_POST_DTL p
                    LEFT JOIN IAS20261.JV_TYPES j ON j.JV_TYPE=p.JV_TYPE
                    WHERE p.C_CODE IS NOT NULL AND NVL(p.DOC_POST,0)=1
                    GROUP BY p.JV_TYPE ORDER BY COUNT(*) DESC""")
                for t, nm in cur.fetchall():
                    if t is None: continue
                    code = str(int(t))
                    label = nm or ("بدون نوع" if int(t)==0 else "نوع "+code)
                    opts.append([code, label])
        _JV_CACHE = opts
        return _JV_CACHE
    except Exception:
        return [["","الكل"],["1","قيد يومية"],["2","قيود الشبكة"],["4","قيود دائنون"],["9","قيد ضريبي"],["11","رصيد افتتاحي للعملاء"],["0","بدون نوع"]]

_LK_CACHE = {}
def lookups(name):
    if name in _LK_CACHE:
        return _LK_CACHE[name]
    q = {
      "rep_code": "SELECT REPRS_CODE, REPRS_A_NAME FROM IAS20261.SALES_MAN WHERE REPRS_CODE IS NOT NULL ORDER BY REPRS_A_NAME",
      "c_code":   "SELECT C_CODE, C_A_NAME FROM IAS20261.CUSTOMER WHERE NVL(INACTIVE,0)=0 AND C_CODE IS NOT NULL ORDER BY C_A_NAME",
      "v_code":   "SELECT V_CODE, MAX(V_NAME) FROM IAS20261.IAS_PI_BILL_MST WHERE V_CODE IS NOT NULL GROUP BY V_CODE ORDER BY MAX(V_NAME)",
      "i_code":   "SELECT I_CODE, I_NAME FROM IAS20261.IAS_ITM_MST WHERE I_CODE IS NOT NULL ORDER BY I_NAME",
      "a_code":   "SELECT A_CODE, A_NAME FROM IAS20261.ACCOUNT WHERE A_CODE IS NOT NULL ORDER BY A_CODE",
    }.get(name)
    if not q:
        return []
    out = []
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute(q)
                for code, nm in cur.fetchall():
                    if code is None:
                        continue
                    out.append(("%s - %s" % (str(code).strip(), (nm or "").strip())).strip(" -"))
        _LK_CACHE[name] = out
        return out
    except Exception:
        return []

STYLE = """<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap');
:root {
  --bg: #f4f5f8;
  --sb-bg: #ffffff;
  --card-bg: #ffffff;
  --primary: #4f46e5;
  --primary-hover: #4338ca;
  --ink: #64748b;
  --ink-dark: #1e293b;
  --line: #f1f5f9;
  --sh: 0 10px 40px rgba(0,0,0,0.04);
}
body { background: var(--bg); color: var(--ink); font-family: 'Cairo', 'Inter', sans-serif; direction: rtl; margin:0; padding:0; box-sizing:border-box; }
* { box-sizing: border-box; margin:0; padding:0; }
a { text-decoration: none; }
.card { background: var(--card-bg); border-radius: 20px; padding: 24px; box-shadow: var(--sh); }
.app { display: flex; min-height: 100vh; padding: 20px; gap: 24px; }
.sb { width: 260px; background: var(--sb-bg); border-radius: 24px; display: flex; flex-direction: column; padding: 30px 20px; flex-shrink: 0; box-shadow: var(--sh); }
.brand { display: flex; align-items: center; gap: 12px; font-size: 24px; font-weight: 800; color: var(--ink-dark); margin-bottom: 40px; }
.brand svg { width: 32px; height: 32px; fill: var(--primary); }
.menu-lbl { font-size: 11px; font-weight: 700; color: #94a3b8; margin: 20px 10px 10px; letter-spacing: 1px; }
.sb a { display: flex; align-items: center; gap: 14px; padding: 14px 20px; border-radius: 16px; color: var(--ink); font-weight: 600; font-size: 15px; margin-bottom: 8px; transition: all 0.3s; }
.sb a:hover { background: #f8fafc; color: var(--ink-dark); }
.sb a.on { background: var(--primary); color: #fff; box-shadow: 0 10px 20px rgba(79, 70, 229, 0.25); }
.sb svg { width: 22px; height: 22px; stroke: currentColor; fill: none; stroke-width: 2; }
.sb a.on svg { stroke: #fff; }

.main { flex: 1; min-width: 0; display: flex; flex-direction: column; }
.top { display: flex; align-items: center; padding: 10px 0 30px; gap: 15px; }
.logo { display:none; }
.ttl { font-size: 26px; font-weight: 800; color: var(--ink-dark); }
.wrap { display: flex; flex-direction: column; gap: 24px; }

.pills { display: flex; gap: 12px; flex-wrap: wrap; }
.pill { background: var(--card-bg); border-radius: 12px; padding: 12px 24px; font-size: 14px; font-weight: 600; color: var(--ink); box-shadow: var(--sh); transition: 0.3s; }
.pill:hover { transform: translateY(-2px); color: var(--primary); }
.pill.on { background: var(--primary); color: #fff; box-shadow: 0 10px 20px rgba(79, 70, 229, 0.25); }

.filters { background: var(--card-bg); border-radius: 20px; padding: 24px; display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 20px; align-items: end; box-shadow: var(--sh); margin-bottom: 24px; }
.filters label { display: block; font-size: 13px; font-weight: 600; color: var(--ink); margin-bottom: 8px; }
.filters input, .filters select { width: 100%; padding: 12px 16px; border: 1px solid var(--line); border-radius: 12px; font-family: inherit; font-size: 14px; font-weight: 500; color: var(--ink-dark); background: #f8fafc; outline: none; transition: 0.3s; }
.filters input:focus, .filters select:focus { border-color: var(--primary); background: #fff; box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.1); }
.filters .btn { background: var(--primary); color: #fff; border: 0; padding: 14px 24px; border-radius: 12px; font-weight: 600; font-size: 14px; cursor: pointer; transition: 0.3s; height: 46px; }
.filters .btn:hover { background: var(--primary-hover); transform: translateY(-2px); box-shadow: 0 10px 20px rgba(79, 70, 229, 0.2); }

.tw { overflow-x: auto; background: var(--card-bg); border-radius: 20px; box-shadow: var(--sh); padding: 10px; }
table { border-collapse: collapse; width: 100%;  }
thead th { white-space: nowrap; color: var(--ink); padding: 8px 12px; text-align: right; font-size: 13px; font-weight: 600; border-bottom: 2px solid var(--line);  }
tbody td { white-space: nowrap; padding: 6px 12px; border-bottom: 1px solid var(--line); font-size: 13px; font-weight: 500; color: var(--ink-dark);  transition: 0.2s; }
tbody tr:hover td { background: #f8fafc; }

.rhead { display: flex; align-items: center; gap: 16px; margin-bottom: 10px; }
.rhead h1 { margin: 0; flex: 1; font-size: 20px; color: var(--ink-dark); font-weight: 800; border:0; padding:0; }
.rhead h1::before { display: none; }
.cnt { color: var(--ink); font-size: 13px; font-weight: 600; margin-bottom: 10px; }
.exps { display: flex; gap: 10px; }
.exp { border: 0; border-radius: 10px; padding: 10px 20px; font-weight: 600; font-size: 13px; color: #fff; cursor: pointer; transition: 0.3s; }
.exp:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
.exp.xl { background: #10b981; } .exp.pf { background: #ef4444; }
.err { background: #fef2f2; color: #b91c1c; padding: 16px; border-radius: 12px; font-weight: 600; }

.gdwrap { display: flex; flex-direction: column; gap: 24px; }
.gkpis { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }
.gk { background: var(--card-bg); border-radius: 24px; padding: 24px; display: flex; flex-direction: column; gap: 16px; box-shadow: var(--sh); position: relative; overflow: hidden; }
.gk:nth-child(1) { background: var(--primary); color: #fff; }
.gk:nth-child(1) .gl { color: rgba(255,255,255,0.8); }
.gk:nth-child(1) .gv { color: #fff; }
.gk .gic { width: 48px; height: 48px; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 20px; }
.gk:nth-child(1) .gic { background: rgba(255,255,255,0.2); }
.gk:nth-child(2) .gic { background: #dcfce7; color: #16a34a; }
.gk:nth-child(3) .gic { background: #ffedd5; color: #f97316; }
.gk:nth-child(4) .gic { background: #e0e7ff; color: #4f46e5; }
.gk:nth-child(5) .gic { background: #d1fae5; color: #059669; }
.gk:nth-child(6) .gic { background: #fee2e2; color: #dc2626; }
.gk:nth-child(7) .gic { background: #e0f2fe; color: #0284c7; }
.gk:nth-child(8) .gic { background: #fef3c7; color: #d97706; }
.gk .gl { font-size: 13px; font-weight: 600; color: var(--ink); margin-bottom: 4px; }
.gk .gv { font-size: 26px; font-weight: 800; color: var(--ink-dark); }
.gcharts { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
.gc { background: var(--card-bg); border-radius: 24px; padding: 24px; box-shadow: var(--sh); }
.gc h3 { font-size: 16px; font-weight: 700; margin: 0 0 20px; color: var(--ink-dark); }
.app-logo { color:#4f46e5; font-weight:900; font-size:26px; letter-spacing:-1px; }
.mobile-dropdown { display: none; }
.mobile-dropdown select { width: 100%; padding: 12px 16px; border: 2px solid var(--primary); border-radius: 12px; font-family: inherit; font-size: 15px; font-weight: 700; color: var(--primary); background: #f8fafc; outline: none; text-align: center; cursor: pointer; margin-bottom: 15px; box-shadow: var(--sh); }