import os
filepath = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the duplicate lines
bad_block = """              TO_CHAR(SUM(perc.b1+perc.b2+perc.b3+perc.b4+perc.b5),'FM999,999,990.00') AS "إجمالي التحصيل"
            TO_CHAR(SUM(perc.b1+perc.b2+perc.b3+perc.b4+perc.b5),'FM999,999,990.00') AS "إجمالي التحصيل"
       FROM perc JOIN IAS20261.CUSTOMER c ON c.C_CODE=perc.C_CODE
       LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=c.REP_CODE
       WHERE (:rep_code IS NULL OR c.REP_CODE = :rep_code)
     FROM perc JOIN IAS20261.CUSTOMER c ON c.C_CODE=perc.C_CODE
     LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=c.REP_CODE
     WHERE (:rep_code IS NULL OR c.REP_CODE = :rep_code)
     GROUP BY c.REP_CODE ORDER BY SUM(perc.b1+perc.b2+perc.b3+perc.b4+perc.b5) DESC"""

good_block = """              TO_CHAR(SUM(perc.b1+perc.b2+perc.b3+perc.b4+perc.b5),'FM999,999,990.00') AS "إجمالي التحصيل"
       FROM perc JOIN IAS20261.CUSTOMER c ON c.C_CODE=perc.C_CODE
       LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=c.REP_CODE
       WHERE (:rep_code IS NULL OR c.REP_CODE = :rep_code)
       GROUP BY c.REP_CODE ORDER BY SUM(perc.b1+perc.b2+perc.b3+perc.b4+perc.b5) DESC"""

if bad_block in content:
    content = content.replace(bad_block, good_block)
    print("Fixed bad block 1")

# Fix the cash sales block for collection_adopted
old_cash_block = """       UNION ALL
       SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
              0, 0, 0, NVL(DISC_AMT,0), 0, 0
       FROM IAS20261.IAS_BILL_MST
       WHERE BILL_DOC_TYPE=1
         AND BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       UNION ALL
       SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(b.CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(b.C_CODE),'UNKNOWN') ELSE TO_CHAR(b.REP_CODE) END,
              0, 0, NVL(p.DR_AMT,0), 0, 0, 0
       FROM IAS20261.IAS_BILL_MST b
       JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_TYPE IN (12, 13, 34) AND TO_CHAR(p.A_CODE) LIKE '111%'
       WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
         AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1"""

new_cash_block = """       UNION ALL
       SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
              0, 0, NVL(BILL_AMT,0) + NVL(VAT_AMT,0) + NVL(OTHR_AMT,0), NVL(DISC_AMT,0), 0, 0
       FROM IAS20261.IAS_BILL_MST
       WHERE BILL_DOC_TYPE=1
         AND BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1"""

if old_cash_block in content:
    content = content.replace(old_cash_block, new_cash_block)
    print("Fixed cash sales block in collection_adopted")

# There is a similar block for query 6 "rep_sales_stats"
old_cash_block_2 = """        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, NVL(DISC_AMT,0), 0, 0
        FROM IAS20261.IAS_BILL_MST
        WHERE BILL_DOC_TYPE=1
          AND BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(b.CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(b.C_CODE),'UNKNOWN') ELSE TO_CHAR(b.REP_CODE) END,
               0, 0, NVL(p.DR_AMT,0), 0, 0, 0
        FROM IAS20261.IAS_BILL_MST b
        JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_TYPE IN (12, 13, 34) AND TO_CHAR(p.A_CODE) LIKE '111%'
        WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
          AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1"""

new_cash_block_2 = """        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, NVL(BILL_AMT,0) + NVL(VAT_AMT,0) + NVL(OTHR_AMT,0), NVL(DISC_AMT,0), 0, 0
        FROM IAS20261.IAS_BILL_MST
        WHERE BILL_DOC_TYPE=1
          AND BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1"""

if old_cash_block_2 in content:
    content = content.replace(old_cash_block_2, new_cash_block_2)
    print("Fixed cash sales block in rep_sales_stats")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch complete.")
