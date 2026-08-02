with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add "customer" option to grp_by select dropdown in TABS
old_grp_by_select = '["options":[["cc","مراكز التكلفة"],["rep","المناديب"],["period","الفترات الزمنية"]]]'
new_grp_by_select = '["options":[["cc","مراكز التكلفة"],["rep","المناديب"],["customer","العملاء"],["period","الفترات الزمنية"]]]'

if old_grp_by_select in content:
    content = content.replace(old_grp_by_select, new_grp_by_select)
    print("Updated grp_by select options in TABS!")
else:
    print("Warning: old_grp_by_select not found directly, checking fallback replacement.")

# 2. Add customer grouping to run_sales_collection_summary
old_sales_if = """    elif grp_by == "period":"""
new_sales_if = """    elif grp_by == "customer":
        grp_sales = "TO_CHAR(C_CODE)"
        grp_sales_b = "TO_CHAR(b.C_CODE)"
        grp_col = "TO_CHAR(C_CODE)"
        grp_ret = "TO_CHAR(C_CODE)"
        join_table = "LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = NVL(ns.grp_code, cs.grp_code)"
        name_expr = "MAX(c.C_A_NAME)"
        code_label = "كود العميل"
        name_label = "اسم العميل"
    elif grp_by == "period":"""

if old_sales_if in content:
    content = content.replace(old_sales_if, new_sales_if, 1)
    print("Updated run_sales_collection_summary with customer option!")

# 3. Add customer grouping to run_debt_movement_summary
old_debt_if = """    elif grp_by == "period":"""
new_debt_if = """    elif grp_by == "customer":
        grp_col = "TO_CHAR(p.C_CODE)"
        grp_sales = "TO_CHAR(C_CODE)"
        grp_sales_b = "TO_CHAR(p.C_CODE)"
        grp_ret = "TO_CHAR(C_CODE)"
        join_table = "LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = ac.grp_code"
        name_expr = "MAX(c.C_A_NAME)"
        code_label = "كود العميل"
        name_label = "اسم العميل"
    elif grp_by == "period":"""

# We replace the second occurrence for run_debt_movement_summary
parts = content.split('elif grp_by == "period":')
if len(parts) >= 3:
    content = parts[0] + 'elif grp_by == "customer":\n        grp_sales = "TO_CHAR(C_CODE)"\n        grp_sales_b = "TO_CHAR(b.C_CODE)"\n        grp_col = "TO_CHAR(C_CODE)"\n        grp_ret = "TO_CHAR(C_CODE)"\n        join_table = "LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = NVL(ns.grp_code, cs.grp_code)"\n        name_expr = "MAX(c.C_A_NAME)"\n        code_label = "كود العميل"\n        name_label = "اسم العميل"\n    elif grp_by == "period":' + parts[1] + 'elif grp_by == "customer":\n        grp_col = "TO_CHAR(p.C_CODE)"\n        grp_sales = "TO_CHAR(C_CODE)"\n        grp_sales_b = "TO_CHAR(p.C_CODE)"\n        grp_ret = "TO_CHAR(C_CODE)"\n        join_table = "LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = ac.grp_code"\n        name_expr = "MAX(c.C_A_NAME)"\n        code_label = "كود العميل"\n        name_label = "اسم العميل"\n    elif grp_by == "period":' + parts[2]
    print("Updated both functions with customer grouping!")

with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Finished patching customer grouping!")
