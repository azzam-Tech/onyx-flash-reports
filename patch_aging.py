import re

filepath = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Patch sql_cash
old_sql_cash = r"""            # Get Cash Sales for the period \(no C_CODE needed\)
            sql_cash = \"\"\"
                SELECT TO_CHAR\(REP_CODE\), SUM\(NVL\(BILL_AMT,0\)-NVL\(DISC_AMT,0\)\+NVL\(VAT_AMT,0\)\+NVL\(OTHR_AMT,0\)\)
                FROM IAS20261\.IAS_BILL_MST
                WHERE BILL_DOC_TYPE=1
                  AND BILL_DATE >= TO_DATE\(:df,'YYYY-MM-DD'\) AND BILL_DATE < TO_DATE\(:dt,'YYYY-MM-DD'\)\+1
                GROUP BY TO_CHAR\(REP_CODE\)
            \"\"\""""

new_sql_cash = """            # Get Cash Sales for the period (no C_CODE needed)
            sql_cash = \"\"\"
                SELECT TO_CHAR(b.REP_CODE), SUM(NVL(p.DR_AMT,0))
                FROM IAS20261.IAS_BILL_MST b
                JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
                WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
                  AND b.BILL_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
                GROUP BY TO_CHAR(b.REP_CODE)
            \"\"\""""

content = re.sub(old_sql_cash, new_sql_cash, content)

# 2. Patch aging logic
old_aging = r"""                    if idate > d:
                        j = bisect\.bisect_right\(ddates, d\) - 1
                        eff = ddates\[j\] if j >= 0 else d
                        age = \(d - eff\)\.days
                    else:
                        age = \(d - idate\)\.days"""

new_aging = """                    if idate > d:
                        age = 0
                    else:
                        age = (d - idate).days"""

content = re.sub(old_aging, new_aging, content)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated perf_aging_dynamic logic!")
