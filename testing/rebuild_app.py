import os
import shutil
import glob
import traceback

src = r"C:\Users\amarn\OneDrive\Desktop\onyxdb\privet\onyx_reports\app.py"
dst = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\app_rebuild.py"
shutil.copy2(src, dst)

scripts = [
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

orig_path_str = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"
orig_path_str2 = orig_path_str.replace("\\", "\\\\")

for script_path in scripts:
    print(f"--- Running {script_path} ---")
    with open(script_path, "r", encoding="utf-8", errors="ignore") as f:
        code = f.read()
    
    # Replace hardcoded paths in the scripts so they modify app_rebuild.py instead
    code = code.replace(orig_path_str, dst)
    code = code.replace(orig_path_str2, dst.replace("\\", "\\\\"))
    
    try:
        exec(code, globals(), locals())
    except Exception as e:
        print(f"Exception in {script_path}: {e}")
        traceback.print_exc()

print(f"Done. Rebuilt app size: {os.path.getsize(dst)}")
