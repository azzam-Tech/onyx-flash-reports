import re

filepath = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# We need to add cash_ret query right after sql_cash in app.py

old_block = r"""            # Get Cash Sales for the period \(no C_CODE needed\)
            sql_cash = \"\"\"
                SELECT TO_CHAR\(b\.REP_CODE\), SUM\(NVL\(p\.DR_AMT,0\)\)
                FROM IAS20261\.IAS_BILL_MST b
                JOIN IAS20261\.IAS_POST_DTL p ON p\.DOC_NO = b\.BILL_NO AND p\.DOC_SER = b\.BILL_SER AND p\.DOC_TYPE = 4 AND TO_CHAR\(p\.A_CODE\) LIKE '111%'
                WHERE b\.BILL_DOC_TYPE=1 AND NVL\(p\.DOC_POST,0\)=1 AND p\.DR_AMT > 0
                  AND b\.BILL_DATE >= TO_DATE\(:df,'YYYY-MM-DD'\) AND b\.BILL_DATE < TO_DATE\(:dt,'YYYY-MM-DD'\)\+1
                GROUP BY TO_CHAR\(b\.REP_CODE\)
            \"\"\"
            cur\.execute\(sql_cash, \{"df": date_from_str, "dt": date_to_str\}\)
            cash_sales_by_rep = \{r: float\(amt\) for r, amt in cur\.fetchall\(\) if r\}"""

new_block = """            # Get Cash Sales for the period (no C_CODE needed)
            sql_cash = \"\"\"
                SELECT TO_CHAR(b.REP_CODE), SUM(NVL(p.DR_AMT,0))
                FROM IAS20261.IAS_BILL_MST b
                JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
                WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
                  AND b.BILL_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
                GROUP BY TO_CHAR(b.REP_CODE)
            \"\"\"
            cur.execute(sql_cash, {"df": date_from_str, "dt": date_to_str})
            cash_sales_by_rep = {r: float(amt) for r, amt in cur.fetchall() if r}

            # Get Cash Returns without C_CODE
            sql_ret_null = \"\"\"
                SELECT NVL(TO_CHAR(REP_CODE), 'UNKNOWN'), SUM(NVL(CR_AMT,0))
                FROM IAS20261.IAS_POST_DTL
                WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND C_CODE IS NULL AND NVL(CR_AMT,0)>0
                  AND DOC_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
                GROUP BY TO_CHAR(REP_CODE)
            \"\"\"
            cur.execute(sql_ret_null, {"df": date_from_str, "dt": date_to_str})
            cash_ret_null_by_rep = {r: float(amt) for r, amt in cur.fetchall()}"""

content = re.sub(old_block, new_block, content)

# Now apply it at the bottom
old_add_cash = r"""    # Add cash sales
    if inc_cash:
        for r_code, c_sales in cash_sales_by_rep\.items\(\):
            if rep_code and r_code != rep_code: continue
            if c_sales > 0:
                rep_results\[r_code\]\["total"\] \+= c_sales
                rep_results\[r_code\]\["b"\]\[0\] \+= c_sales"""

new_add_cash = """    # Add cash sales
    if inc_cash:
        for r_code, c_sales in cash_sales_by_rep.items():
            if rep_code and r_code != rep_code: continue
            if c_sales > 0:
                rep_results[r_code]["total"] += c_sales
                rep_results[r_code]["b"][0] += c_sales

    # Subtract cash returns without C_CODE
    if inc_ret:
        for r_code, c_ret in cash_ret_null_by_rep.items():
            if rep_code and r_code != rep_code and r_code != 'UNKNOWN': continue
            if c_ret > 0:
                rep_results[r_code]["total"] -= c_ret
                rep_results[r_code]["b"][0] -= c_ret"""

content = re.sub(old_add_cash, new_add_cash, content)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated app.py to include cash_ret_null!")
