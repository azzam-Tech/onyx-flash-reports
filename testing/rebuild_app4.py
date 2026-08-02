import os
import shutil
import glob

src = r"C:\Users\amarn\OneDrive\Desktop\onyxdb\privet\onyx_reports\app.py"
dst = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\app_rebuild4.py"
shutil.copy2(src, dst)

all_scripts = [
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
    r"privet\onyx_reports\revert_gross.py"
]

cutoff = os.path.getmtime(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\integrate_targets.py")

for script_path in glob.glob(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\*.py"):
    if os.path.getmtime(script_path) <= cutoff + 1:
        with open(script_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            if "app.py" in content and "rebuild" not in script_path and "debug" not in script_path and "recover" not in script_path:
                rel = os.path.relpath(script_path, r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity")
                if rel not in all_scripts:
                    all_scripts.append(rel)

all_scripts.sort(key=lambda x: os.path.getmtime(os.path.join(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity", x)))

orig_path_str = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"
orig_path_str2 = orig_path_str.replace("\\", "\\\\")
dst2 = dst.replace("\\", "\\\\")

print("Scripts to run:")
for s in all_scripts:
    print(s)

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

print(f"Done. Rebuilt app4 size: {os.path.getsize(dst)}")
