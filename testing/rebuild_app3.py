import os
import shutil
import traceback

src = r"C:\Users\amarn\OneDrive\Desktop\onyxdb\privet\onyx_reports\app.py"
dst = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\app_rebuild3.py"
shutil.copy2(src, dst)

scripts = [
    r"privet\onyx_reports\patch.py",
    r"privet\onyx_reports\patch_auth.py",
    r"privet\onyx_reports\patch_by_item.py",
    r"privet\onyx_reports\patch_cash_box.py",
    r"privet\onyx_reports\patch_cash_sales.py",
    r"privet\onyx_reports\patch_charts.py",
    r"privet\onyx_reports\patch_charts_size.py",
    r"privet\onyx_reports\patch_dealdeck.py",
    r"privet\onyx_reports\patch_dynamic.py",
    r"privet\onyx_reports\patch_final.py",
    r"privet\onyx_reports\patch_math.py",
    r"privet\onyx_reports\patch_profit_sql.py",
    r"privet\onyx_reports\patch_revert_style.py",
    r"privet\onyx_reports\patch_sales.py",
    r"privet\onyx_reports\patch_sales_ext.py",
    r"privet\onyx_reports\patch_sales_itm_disc.py",
    r"privet\onyx_reports\patch_secondary_pages.py",
    r"privet\onyx_reports\patch_style.py",
    r"privet\onyx_reports\revert_gross.py",
    
    r"testing\patch_cc.py",
    r"testing\inject.py",
    r"testing\patch_print_model.py",
    r"testing\patch_print2.py",
    r"testing\patch_true_cost.py",
    r"testing\patch_padding.py",
    r"testing\patch_ui_padding.py",
    r"testing\patch_nowrap.py",
    r"testing\patch_minwidth.py",
    r"testing\patch_landscape.py",
    r"testing\patch_grouping.py",
    r"testing\patch_projection.py",
    r"testing\patch_ui_wrap.py",
    r"testing\patch_ui_wrap2.py",
    r"testing\patch_net_sales.py",
    r"testing\patch_net_sales_again.py",
    r"testing\insert_report.py",
    r"testing\inject_js.py",
    r"testing\inject_tabs.py",
    r"testing\fix_tabs.py",
    r"testing\inject_tabs2.py",
    r"testing\patch_target_ui.py",
    r"testing\integrate_targets.py"
]

all_scripts = []
for s in scripts:
    all_scripts.append(s)

all_scripts.sort(key=lambda x: os.path.getmtime(os.path.join(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity", x)))

orig_path_str = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"
orig_path_str2 = orig_path_str.replace("\\", "\\\\")

dst2 = dst.replace("\\", "\\\\")

for script_path in all_scripts:
    print(f"--- Running {script_path} ---")
    full_path = os.path.join(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity", script_path)
    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
        code = f.read()
    
    code = code.replace(orig_path_str, dst)
    code = code.replace(orig_path_str2, dst2)
    code = code.replace("privet/onyx_reports/app.py", dst.replace("\\", "/"))
    code = code.replace("'app.py'", f"'{dst2}'")
    code = code.replace('"app.py"', f'"{dst2}"')
    
    try:
        exec(code, globals(), locals())
    except Exception as e:
        print(f"Exception in {script_path}: {e}")

print(f"Done. Rebuilt app3 size: {os.path.getsize(dst)}")
