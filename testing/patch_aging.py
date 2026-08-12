import re

file_path = 'privet/onyx_reports/report_handlers.py'
with open(file_path, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update run_cust_aging
c = re.sub(
    r'rep_code = args\.get\("rep_code"\)\n\s+c_code = args\.get\("c_code"\)',
    'rep_code = args.get("rep_code")\n    c_code = args.get("c_code")\n    cc_code = args.get("cc_code")\n    grp_code = args.get("grp_code")\n    if cc_code: cc_code = cc_code.split(" - ")[0].strip()\n    if grp_code: grp_code = grp_code.split(" - ")[0].strip()',
    c, count=1
)

c = c.replace(
    'sql_cust = "SELECT TO_CHAR(C_CODE), MAX(C_A_NAME), MAX(TO_CHAR(REP_CODE)) FROM IAS20261.CUSTOMER GROUP BY TO_CHAR(C_CODE)"',
    'sql_cust = "SELECT TO_CHAR(C_CODE), MAX(C_A_NAME), MAX(TO_CHAR(REP_CODE)), MAX(TO_CHAR(C_GROUP_CODE)) FROM IAS20261.CUSTOMER GROUP BY TO_CHAR(C_CODE)"'
)
c = c.replace(
    'customers[row[0]] = {"name": row[1] or "", "rep": row[2] or ""}',
    'customers[row[0]] = {"name": row[1] or "", "rep": row[2] or "", "grp": row[3] or ""}'
)
c = c.replace(
    'binds["cst"] = c_code',
    'binds["cst"] = c_code\n            if cc_code:\n                filters.append("TO_CHAR(p.CC_CODE) = :cc")\n                binds["cc"] = cc_code'
)
c = c.replace(
    'if rep_code and customers.get(c_id, {}).get("rep") != rep_code: continue',
    'cust_info = customers.get(c_id, {})\n        if rep_code and cust_info.get("rep") != rep_code: continue\n        if grp_code and cust_info.get("grp") != grp_code: continue'
)

# 2. Update run_perf_aging_fifo
c = re.sub(
    r'rep_code = args\.get\("rep_code"\)\n\s+if is_dynamic:',
    'rep_code = args.get("rep_code")\n    cc_code = args.get("cc_code")\n    grp_code = args.get("grp_code")\n    if cc_code: cc_code = cc_code.split(" - ")[0].strip()\n    if grp_code: grp_code = grp_code.split(" - ")[0].strip()\n    if is_dynamic:',
    c, count=1
)
c = c.replace(
    'cur.execute("SELECT C_CODE, REP_CODE FROM IAS20261.CUSTOMER")\n            cust_rep = {str(c): str(r) for c, r in cur.fetchall()}',
    'cur.execute("SELECT C_CODE, REP_CODE, C_GROUP_CODE FROM IAS20261.CUSTOMER")\n            res_cust = cur.fetchall()\n            cust_rep = {str(c): (str(r) if r else "") for c, r, g in res_cust}\n            cust_grp = {str(c): (str(g) if g else "") for c, r, g in res_cust}'
)
# Modify SQL in run_perf_aging_fifo
c = c.replace(
    '''sql = """
                SELECT TO_CHAR(C_CODE), DOC_DATE, NVL(DR_AMT,0), NVL(CR_AMT,0), DOC_TYPE, TO_CHAR(REP_CODE)
                FROM IAS20261.IAS_POST_DTL
                WHERE (NVL(DOC_POST,0)=1 OR (NVL(DOC_POST,0)=0 AND DOC_TYPE=2))
                    AND C_CODE IS NOT NULL
                    AND DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1
            """
            cur.execute(sql, {"dt": date_to_str})''',
    '''
            binds = {"dt": date_to_str}
            filters = []
            if cc_code:
                filters.append("TO_CHAR(CC_CODE) = :cc")
                binds["cc"] = cc_code
            filter_str = " AND " + " AND ".join(filters) if filters else ""
            sql = f"""
                SELECT TO_CHAR(C_CODE), DOC_DATE, NVL(DR_AMT,0), NVL(CR_AMT,0), DOC_TYPE, TO_CHAR(REP_CODE)
                FROM IAS20261.IAS_POST_DTL
                WHERE (NVL(DOC_POST,0)=1 OR (NVL(DOC_POST,0)=0 AND DOC_TYPE=2))
                    AND C_CODE IS NOT NULL
                    AND DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1
                    {filter_str}
            """
            cur.execute(sql, binds)
'''
)
c = c.replace(
    'if rep_code and c_rep != rep_code: continue',
    'if rep_code and c_rep != rep_code: continue\n        if grp_code and cust_grp.get(c_id) != grp_code: continue'
)

# 3. Update run_perf_aging_analytical
c = re.sub(
    r'rep_code = args\.get\("rep_code"\)\n\s+if rep_code:',
    'rep_code = args.get("rep_code")\n    cc_code = args.get("cc_code")\n    grp_code = args.get("grp_code")\n    if cc_code: cc_code = cc_code.split(" - ")[0].strip()\n    if grp_code: grp_code = grp_code.split(" - ")[0].strip()\n    if rep_code:',
    c, count=1
)
# Modify SQL in run_perf_aging_analytical
c = c.replace(
    '''sql = """
                SELECT TO_CHAR(C_CODE), NVL(DR_AMT,0), NVL(CR_AMT,0)
                FROM IAS20261.IAS_POST_DTL
                WHERE (NVL(DOC_POST,0)=1 OR (NVL(DOC_POST,0)=0 AND DOC_TYPE=2))
                    AND C_CODE IS NOT NULL
                    AND DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1
            """
            cur.execute(sql, {"dt": date_to_str})''',
    '''
            binds = {"dt": date_to_str}
            filters = []
            if cc_code:
                filters.append("TO_CHAR(CC_CODE) = :cc")
                binds["cc"] = cc_code
            filter_str = " AND " + " AND ".join(filters) if filters else ""
            sql = f"""
                SELECT TO_CHAR(C_CODE), NVL(DR_AMT,0), NVL(CR_AMT,0)
                FROM IAS20261.IAS_POST_DTL
                WHERE (NVL(DOC_POST,0)=1 OR (NVL(DOC_POST,0)=0 AND DOC_TYPE=2))
                    AND C_CODE IS NOT NULL
                    AND DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1
                    {filter_str}
            """
            cur.execute(sql, binds)
'''
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(c)
print('Patched report_handlers.py successfully.')
