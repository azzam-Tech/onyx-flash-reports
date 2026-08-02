with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add fn to sales_collection_summary
old_scs = '{"id":"sales_collection_summary","title":"صافي المبيعات وإجمالي التحصيل حسب الفترة","params":'
new_scs = '{"id":"sales_collection_summary","title":"صافي المبيعات وإجمالي التحصيل حسب الفترة","fn":"run_sales_collection_summary","params":'

if old_scs in content:
    content = content.replace(old_scs, new_scs)
    print("Added fn: run_sales_collection_summary to sales_collection_summary!")

# 2. Add fn to debt_movement_summary
old_dms = '{"id":"debt_movement_summary","title":"تقرير حركة المديونية والتحصيل الدوري","params":'
new_dms = '{"id":"debt_movement_summary","title":"تقرير حركة المديونية والتحصيل الدوري","fn":"run_debt_movement_summary","params":'

if old_dms in content:
    content = content.replace(old_dms, new_dms)
    print("Added fn: run_debt_movement_summary to debt_movement_summary!")

# 3. Add fn to main_wh_movement
old_mwm = '{"id":"main_wh_movement","title":"حركة الأصناف (7 مستودعات)","params":'
new_mwm = '{"id":"main_wh_movement","title":"حركة الأصناف (7 مستودعات)","fn":"run_main_wh_movement","params":'

if old_mwm in content:
    content = content.replace(old_mwm, new_mwm)
    print("Added fn: run_main_wh_movement to main_wh_movement!")

with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Finished adding fn properties to app.py TABS!")
