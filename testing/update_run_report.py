import re
import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

replacement = """import calendar
from datetime import date

def calculate_dates(year, p_type, p_val):
    try: year = int(year)
    except: year = date.today().year
    
    try: p_val = int(p_val)
    except: p_val = 1
    
    if p_type == "month":
        start = date(year, p_val, 1)
        end = date(year, p_val, calendar.monthrange(year, p_val)[1])
    elif p_type == "quarter":
        start_month = (p_val - 1) * 3 + 1
        end_month = start_month + 2
        start = date(year, start_month, 1)
        end = date(year, end_month, calendar.monthrange(year, end_month)[1])
    elif p_type == "half":
        start_month = (p_val - 1) * 6 + 1
        end_month = start_month + 5
        start = date(year, start_month, 1)
        end = date(year, end_month, calendar.monthrange(year, end_month)[1])
    else: # year
        start = date(year, 1, 1)
        end = date(year, 12, 31)
    return start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")

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
        if "p_year" in binds and "p_type" in binds:
            d_from, d_to = calculate_dates(binds["p_year"], binds["p_type"], binds.get("p_val", 1))
            binds["date_from"] = d_from
            binds["date_to"] = d_to
            
        with get_conn() as con:"""

content = re.sub(
    r'def run_report\(rpt, args\):.*?with get_conn\(\) as con:',
    replacement,
    content,
    flags=re.DOTALL
)

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)
print("SUCCESS")
