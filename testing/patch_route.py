app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'
with open(app_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

route_logic = """
@app.route("/globals", methods=["GET","POST"])
def globals_page():
    if not session.get("set_ok"):
        if request.method == "POST" and request.form.get("pin") is not None:
            if request.form.get("pin") == SETTINGS_PIN:
                session["set_ok"] = True
            else:
                return render_template_string(PIN_PAGE, error=True)
        else:
            return render_template_string(PIN_PAGE, error=False)
            
    saved = False
    targets_data = load_globals()
    if not targets_data: targets_data = {}
    
    if request.method == "POST":
        for key in request.form:
            if key.startswith("target_2026_"):
                parts = key.split("_")
                if len(parts) == 4:
                    year = parts[1]
                    rep_code = parts[2]
                    month = parts[3]
                    try:
                        val = float(request.form[key])
                        if year not in targets_data: targets_data[year] = {}
                        if rep_code not in targets_data[year]: targets_data[year][rep_code] = {}
                        targets_data[year][rep_code][month] = val
                    except ValueError:
                        pass
        save_globals(targets_data)
        saved = True
        
    reps = []
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute("SELECT REPRS_CODE, REPRS_A_NAME FROM IAS20261.SALES_MAN ORDER BY REPRS_CODE")
                for c, n in cur.fetchall():
                    reps.append({"code": str(c), "name": n or str(c)})
    except Exception as e:
        print("Error loading reps:", e)
        
    return render_template_string(GLOBALS_PAGE, reps=reps, targets=targets_data.get("2026", {}), saved=saved)
"""

for i, line in enumerate(lines):
    if line.startswith('DASHBOARD_PAGE = '):
        lines.insert(i, route_logic + '\n\n')
        break

with open(app_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
