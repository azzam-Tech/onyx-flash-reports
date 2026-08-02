import os, re

app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'
with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

helpers = """
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
    if grp_by not in ("rep", "period"):
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
    if grp_by == "rep" and row_code:
        rep_targets = year_targets.get(str(row_code), {})
        for m in months_to_sum:
            total_target += float(rep_targets.get(str(m), 0.0))
    elif grp_by == "period":
        for r_code, rep_targets in year_targets.items():
            for m in months_to_sum:
                total_target += float(rep_targets.get(str(m), 0.0))
                
    return total_target
"""

if "def get_target_amount" not in content:
    content = content.replace('DFROM = {"name":"date_from"', helpers + '\nDFROM = {"name":"date_from"')

# Patch run_sales_collection_summary
sales_loop_find = """            for c_code, c_name, ns, col in cur.fetchall():
                ns_val = float(ns or 0.0)
                ns_vat_val = ns_val * 1.15
                col_val = float(col or 0.0)
                diff = ns_val - col_val
                ratio_str = f"{(col_val / ns_val * 100):.1f}%" if ns_val > 0 else "0.0%"
                
                rows.append((
                    c_code,
                    c_name or str(c_code),
                    f"{ns_val:,.2f}",
                    f"{ns_vat_val:,.2f}",
                    f"{col_val:,.2f}",
                    f"{diff:,.2f}",
                    ratio_str,
                    ""
                ))"""

sales_loop_repl = """            for c_code, c_name, ns, col in cur.fetchall():
                ns_val = float(ns or 0.0)
                ns_vat_val = ns_val * 1.15
                col_val = float(col or 0.0)
                diff = ns_val - col_val
                ratio_str = f"{(col_val / ns_val * 100):.1f}%" if ns_val > 0 else "0.0%"
                
                target_val = get_target_amount(year_val, period_type, period_val, grp_by, c_code)
                target_str = f"{target_val:,.2f}" if target_val > 0 else ""
                
                rows.append((
                    c_code,
                    c_name or str(c_code),
                    f"{ns_val:,.2f}",
                    f"{ns_vat_val:,.2f}",
                    f"{col_val:,.2f}",
                    f"{diff:,.2f}",
                    ratio_str,
                    target_str
                ))"""

content = content.replace(sales_loop_find, sales_loop_repl)

# Patch run_debt_movement_summary
debt_loop_find = """                rows.append((
                    c_code,
                    c_name or str(c_code),
                    f"{ob_val:,.2f}",
                    f"{ns_vat_val:,.2f}",
                    f"{col_val:,.2f}",
                    f"{col_ratio:,.2f}%",
                    f"{closing_val:,.2f}",
                    f"{ns_no_vat_val:,.2f}",
                    ""
                ))"""

debt_loop_repl = """                target_val = get_target_amount(year_val, period_type, period_val, grp_by, c_code)
                target_str = f"{target_val:,.2f}" if target_val > 0 else ""
                
                rows.append((
                    c_code,
                    c_name or str(c_code),
                    f"{ob_val:,.2f}",
                    f"{ns_vat_val:,.2f}",
                    f"{col_val:,.2f}",
                    f"{col_ratio:,.2f}%",
                    f"{closing_val:,.2f}",
                    f"{ns_no_vat_val:,.2f}",
                    target_str
                ))"""

content = content.replace(debt_loop_find, debt_loop_repl)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)
