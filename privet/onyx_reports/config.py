import os
import json

SETTINGS_PIN = os.environ.get("SETTINGS_PIN", "00900")
APP_PIN = os.environ.get("APP_PIN", "00900")

SETTINGS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings.json")
# كل ما يخص الربح: يُخفى عند تفعيل "إخفاء الربح"
PROFIT_TABS = {"prof"}
PROFIT_REPORTS = {"fin/income_statement", "fin/cost_centers"}
def _load_raw():
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}
def load_hidden_raw():
    d = _load_raw()
    return set(d.get("tabs", [])), set(d.get("reports", []))
def load_hide_profit():
    return bool(_load_raw().get("hide_profit"))
def load_hidden():
    """المجموعات الفعّالة المطبَّقة على الواجهة (تشمل إخفاء الربح إن كان مفعّلاً)."""
    tabs, reps = load_hidden_raw()
    if load_hide_profit():
        tabs = tabs | PROFIT_TABS
        reps = reps | PROFIT_REPORTS
    return tabs, reps
def save_hidden(tabs, reports, hide_profit=False):
    try:
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump({"tabs": list(tabs), "reports": list(reports),
                       "hide_profit": bool(hide_profit)}, f, ensure_ascii=False)
    except Exception as e:
        print("settings save error:", e)

GLOBALS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "globals.json")

def load_globals():
    try:
        with open(GLOBALS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_globals(data):
    try:
        with open(GLOBALS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("globals save error:", e)

USERS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.json")

def load_users():
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_users(data):
    try:
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("users save error:", e)

def check_permission(username, tab_id, report_id=None):
    users = load_users()
    user = users.get(username)
    if not user:
        return False
    if user.get("role") == "admin":
        return True
    
    allowed_tabs = user.get("allowed_tabs", [])
    allowed_reports = user.get("allowed_reports", [])

    if report_id:
        # Only grant access if the specific report is allowed.
        # This allows the user to grant access to a tab but hide specific reports inside it.
        if "*" in allowed_reports or f"{tab_id}/{report_id}" in allowed_reports:
            return True
        return False
    else:
        # If checking for just the tab
        if "*" in allowed_tabs or tab_id in allowed_tabs:
            return True
        # Implicitly allow the tab if ANY report within this tab is allowed
        if "*" in allowed_reports:
            return True
        for rep in allowed_reports:
            if rep.startswith(tab_id + "/"):
                return True
        return False



def resolve_period_from_code(c_code, period_type):
    c = str(c_code)
    if period_type == "monthly":
        try:
            if "-" in c: return [int(c.split("-")[1])]
        except: pass
    elif period_type == "quarterly":
        try:
            q = int(c.replace("Q", ""))
            return [q*3 - 2, q*3 - 1, q*3]
        except: pass
    elif period_type == "semi_annual":
        if "H1" in c or "الأول" in c: return [1,2,3,4,5,6]
        if "H2" in c or "الثاني" in c: return [7,8,9,10,11,12]
    return []


def get_target_amount(year_val, period_type, period_val, grp_by, row_code=None):
    if grp_by not in ("rep", "cc", "period"):
        return 0.0
    
    globals_data = load_globals()
    year_targets = globals_data.get(year_val, {})
    if not year_targets:
        return 0.0
        
    months_to_sum = []
    if grp_by == "period":
        months_to_sum = resolve_period_from_code(row_code, period_type)
    else:
        if period_val == "all":
            months_to_sum = list(range(1, 13))
        else:
            if period_type == "monthly":
                try: months_to_sum = [int(period_val)]
                except: pass
            elif period_type == "quarterly":
                try:
                    q = int(period_val)
                    months_to_sum = [q*3 - 2, q*3 - 1, q*3]
                except: pass
            elif period_type == "semi_annual":
                if period_val == "1": months_to_sum = [1, 2, 3, 4, 5, 6]
                elif period_val == "2": months_to_sum = [7, 8, 9, 10, 11, 12]
            
    total_target = 0.0
    if grp_by in ("rep", "cc") and row_code:
        rep_targets = year_targets.get(str(row_code), {})
        for m in months_to_sum:
            total_target += float(rep_targets.get(str(m), 0.0))
    elif grp_by == "period":
        for r_code, rep_targets in year_targets.items():
            for m in months_to_sum:
                total_target += float(rep_targets.get(str(m), 0.0))
                
    return total_target
