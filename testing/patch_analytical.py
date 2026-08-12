import re

file_path = 'privet/onyx_reports/report_handlers.py'
with open(file_path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    'cur.execute("SELECT C_CODE, REP_CODE, C_A_NAME FROM IAS20261.CUSTOMER")',
    'cur.execute("SELECT C_CODE, REP_CODE, C_A_NAME, C_GROUP_CODE FROM IAS20261.CUSTOMER")'
)

c = c.replace(
    '''            for c, r, n in cur.fetchall():
                cust_rep[str(c)] = str(r)
                cust_names[str(c)] = str(n)''',
    '''            cust_grp = {}
            for c, r, n, g in cur.fetchall():
                cust_rep[str(c)] = str(r)
                cust_names[str(c)] = str(n)
                cust_grp[str(c)] = str(g) if g else ""'''
)

c = c.replace(
    'if rep_code and c_rep != rep_code: continue',
    'if rep_code and c_rep != rep_code: continue\n        if grp_code and cust_grp.get(c_id) != grp_code: continue'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(c)
print('Patched run_perf_aging_analytical successfully.')
