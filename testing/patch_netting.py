import sys

file_path = 'privet/onyx_reports/report_handlers.py'
with open(file_path, 'r', encoding='utf-8') as f:
    c = f.read()

netting_code = """
            if str(args.get("vendor_link", "0")) == "1":
                cur.execute("SELECT TO_CHAR(C_CODE), TO_CHAR(C_VENDOR) FROM IAS20261.CUSTOMER WHERE C_VENDOR IS NOT NULL")
                cust_vendor_map = {c: v for c, v in cur.fetchall()}
                cur.execute("SELECT TO_CHAR(V_CODE), SUM(NVL(CR_AMT,0) - NVL(DR_AMT,0)) FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND V_CODE IS NOT NULL AND DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1 GROUP BY TO_CHAR(V_CODE)", {"dt": date_to_str})
                vendor_balances = {v: float(bal) for v, bal in cur.fetchall()}
                for c_id, v_id in cust_vendor_map.items():
                    if c_id in by_cust and v_id in vendor_balances and vendor_balances[v_id] > 0:
                        by_cust[c_id]["credits"] += vendor_balances[v_id]
"""

# Patch run_cust_aging
target1 = """
                if dr > 0:
                    by_cust[c_id]["debits"].append((d, dr))
"""
c = c.replace(target1, target1 + netting_code)

# Patch run_perf_aging_fifo
target2 = """
                if dr > 0:
                    by_cust[c_id]["debits"].append((d, dr, dtype))
"""
c = c.replace(target2, target2 + netting_code)

# Patch run_perf_aging_analytical
target3 = """
            for c_id, dr, cr in cur.fetchall():
                by_cust[c_id]["debits"] += float(dr)
                by_cust[c_id]["credits"] += float(cr)
"""
c = c.replace(target3, target3 + netting_code)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(c)
print('Applied netting block to handlers!')
