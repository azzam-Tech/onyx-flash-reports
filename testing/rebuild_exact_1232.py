import os, glob, shutil

# Source baseline
base_file = r'c:\Users\amarn\OneDrive\Desktop\onyxdb\privet\onyx_reports\app.py'
dst_file = r'testing/app_1232.py'

shutil.copy(base_file, dst_file)

# Sequence of patch files up to 12:33 PM
patch_sequence = [
    r'privet\onyx_reports\patch.py',
    r'privet\onyx_reports\patch_dynamic.py',
    r'privet\onyx_reports\patch_sales.py',
    r'privet\onyx_reports\patch_sales_ext.py',
    r'privet\onyx_reports\patch_by_item.py',
    r'privet\onyx_reports\patch_sales_itm_disc.py',
    r'privet\onyx_reports\patch_style.py',
    r'privet\onyx_reports\patch_revert_style.py',
    r'privet\onyx_reports\patch_dealdeck.py',
    r'privet\onyx_reports\patch_charts.py',
    r'privet\onyx_reports\patch_secondary_pages.py',
    r'privet\onyx_reports\patch_final.py',
    r'privet\onyx_reports\patch_charts_size.py',
    r'privet\onyx_reports\patch_profit_sql.py',
    r'privet\onyx_reports\patch_auth.py',
    r'privet\onyx_reports\patch_cash_sales.py',
    r'privet\onyx_reports\patch_cash_box.py',
    r'privet\onyx_reports\patch_math.py',
    r'privet\onyx_reports\revert_gross.py',
    r'testing\patch_cc.py',
    r'testing\update_app.py',
    r'testing\inject.py',
    r'testing\fix_reports.py',
    r'testing\fix.py',
    r'testing\fix_bind.py',
    r'testing\fix_bind2.py',
    r'testing\fix_true_inc.py',
    r'testing\fix_true.py',
    r'testing\fix_syntax.py',
    r'testing\patch_print_model.py',
    r'testing\patch_print2.py',
    r'testing\get_true_sql.py',
    r'testing\patch_true_cost.py',
    r'testing\patch_padding.py',
    r'testing\patch_ui_padding.py',
    r'testing\patch_nowrap.py',
    r'testing\patch_minwidth.py',
    r'testing\patch_landscape.py',
    r'testing\patch_grouping.py',
    r'testing\patch_projection.py',
    r'testing\patch_ui_wrap.py',
    r'testing\patch_ui_wrap2.py',
    r'testing\patch_net_sales.py',
    r'testing\fix_ext_disc.py',
    r'testing\patch_net_sales_again.py',
    r'testing\insert_report.py',
    r'testing\update_app_params.py',
    r'testing\update_run_report.py',
    r'testing\inject_js.py',
    r'testing\fix_binds.py',
    r'testing\update_year_logic.py'
]

print(f"Starting rebuild of EXACT 12:32 PM state using {len(patch_sequence)} patches...")

for p in patch_sequence:
    if not os.path.exists(p):
        print(f"Skipping missing patch: {p}")
        continue
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        code = f.read()
    
    # Replace target file references inside patch script code to point to dst_file
    code = code.replace("privet/onyx_reports/app.py", dst_file)
    code = code.replace("privet\\onyx_reports\\app.py", dst_file)
    code = code.replace(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", dst_file)
    code = code.replace("app.py", dst_file)
    
    # Execute patch code in isolated namespace
    print(f"--- Running {p} ---")
    try:
        exec(code, {"__name__": "__main__"})
    except Exception as e:
        print(f"Exception in {p}: {e}")

print("Rebuild complete. Target size:", os.path.getsize(dst_file))
