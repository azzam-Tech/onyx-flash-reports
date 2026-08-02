app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add dynamic month helpers near top of app.py
helper_code = """import calendar
from datetime import datetime

def get_current_month_range():
    now = datetime.now()
    year = now.year
    month = now.month
    last_day = calendar.monthrange(year, month)[1]
    return f"{year}-{month:02d}-01", f"{year}-{month:02d}-{last_day:02d}"

def get_default_date_from():
    return get_current_month_range()[0]

def get_default_date_to():
    return get_current_month_range()[1]
"""

if "def get_current_month_range():" not in content:
    idx = content.find("SETTINGS_FILE =")
    content = content[:idx] + helper_code + "\n" + content[idx:]
    print("Added dynamic month helper functions!")

# Update DFROM and DTO dictionary definitions to use callable dynamic functions or properties
content = content.replace('DFROM = {"name":"date_from","label":"من تاريخ","type":"date","default":"2026-07-01"}',
                          'DFROM = {"name":"date_from","label":"من تاريخ","type":"date","get_default": get_default_date_from}')

content = content.replace('DTO   = {"name":"date_to","label":"إلى تاريخ","type":"date","default":"2026-07-31"}',
                          'DTO   = {"name":"date_to","label":"إلى تاريخ","type":"date","get_default": get_default_date_to}')

# Update run_sql_report to dynamically execute get_default or fallback
old_binds_logic = """        if p.get("type") in ("date", "month"):
            val = val or ("2026-07-01" if "from" in pname else "2026-07-31")"""

new_binds_logic = """        if p.get("type") in ("date", "month"):
            if not val:
                if callable(p.get("get_default")):
                    val = p["get_default"]()
                elif p.get("default"):
                    val = p["default"]
                else:
                    val = get_default_date_from() if "from" in pname else get_default_date_to()"""

if old_binds_logic in content:
    content = content.replace(old_binds_logic, new_binds_logic)
    print("Updated run_sql_report to use dynamic month dates!")

with open(app_path, "w", encoding="utf-8") as f:
    f.write(content)

print("DYNAMIC MONTH DATES APPLIED SUCCESSFULLY TO APP.PY!")
