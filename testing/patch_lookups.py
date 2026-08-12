import re

# 1. Update report_handlers.py
file_path = 'privet/onyx_reports/report_handlers.py'
with open(file_path, 'r', encoding='utf-8') as f:
    c = f.read()

new_lookups = """      "v_code":   "SELECT V_CODE, MAX(V_NAME) FROM IAS20261.IAS_PI_BILL_MST WHERE V_CODE IS NOT NULL GROUP BY V_CODE ORDER BY MAX(V_NAME)",
      "cc_code":  "SELECT CC_CODE, CC_A_NAME FROM IAS20261.COST_CENTERS WHERE CC_CODE IS NOT NULL ORDER BY CC_A_NAME",
      "grp_code": "SELECT C_GROUP_CODE, C_GROUP_A_NAME FROM IAS20261.CUSTOMER_GROUP WHERE C_GROUP_CODE IS NOT NULL ORDER BY C_GROUP_A_NAME","""

c = c.replace(
    '      "v_code":   "SELECT V_CODE, MAX(V_NAME) FROM IAS20261.IAS_PI_BILL_MST WHERE V_CODE IS NOT NULL GROUP BY V_CODE ORDER BY MAX(V_NAME)",',
    new_lookups
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(c)

# 2. Update app.py
app_path = 'privet/onyx_reports/app.py'
with open(app_path, 'r', encoding='utf-8') as f:
    c_app = f.read()

c_app = c_app.replace(
    'if _p["name"] in ("rep_code","c_code","v_code","i_code","a_code"): _p["_list"] = lookups(_p["name"])',
    'if _p["name"] in ("rep_code","c_code","v_code","i_code","a_code","cc_code","grp_code"): _p["_list"] = lookups(_p["name"])'
)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(c_app)

print("Patched dropdown lists!")
