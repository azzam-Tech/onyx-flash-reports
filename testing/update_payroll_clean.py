with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

old_report_block = """         {"id":"payroll_financial_summary","title":"كشف الرواتب والتأمينات والبدلات المالي","params":[DFROM,DTO,GRP],"sql":\"\"\"
         WITH raw_data AS (
           SELECT p.A_CODE, a.A_NAME,
                  CASE WHEN :grp_by = 'rep' THEN NVL(TO_CHAR(p.CC_CODE), 'عام') ELSE TO_CHAR(p.A_CODE) END AS grp_code,
                  NVL(p.DR_AMT, 0) AS dr,
                  NVL(p.CR_AMT, 0) AS cr
           FROM IAS20261.IAS_POST_DTL p
           JOIN IAS20261.ACCOUNT a ON a.A_CODE = p.A_CODE
           WHERE (p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%' OR p.A_CODE LIKE '11402%' OR p.A_CODE LIKE '21104%')
             AND NVL(p.DOC_POST, 0) = 1
             AND p.DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD')
             AND p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD') + 1
         )
         SELECT r.grp_code AS "الكود",
                MAX(CASE WHEN :grp_by = 'rep' THEN NVL(sm.REPRS_A_NAME, r.grp_code) ELSE r.A_NAME END) AS "اسم الحساب/المندوب",
                COUNT(*) AS "عدد الحركات",
                TO_CHAR(SUM(r.dr), 'FM999,999,990.00') AS "إجمالي الصرف والرواتب",
                TO_CHAR(SUM(r.cr), 'FM999,990.00') AS "إجمالي التسويات والدائن",
                TO_CHAR(SUM(r.dr - r.cr), 'FM999,999,990.00') AS "الصافي المالي"
         FROM raw_data r
         LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = r.grp_code
         GROUP BY r.grp_code
         ORDER BY SUM(r.dr) DESC
         \"\"\"},"""

new_report_block = """         {"id":"payroll_financial_summary","title":"كشف الرواتب والتأمينات والبدلات المالي","params":[DFROM,DTO],"sql":\"\"\"
         SELECT p.A_CODE AS "كود الحساب",
                a.A_NAME AS "اسم البند المحاسبي",
                COUNT(*) AS "عدد الحركات",
                TO_CHAR(SUM(NVL(p.DR_AMT,0)), 'FM999,999,990.00') AS "إجمالي الصرف والرواتب",
                TO_CHAR(SUM(NVL(p.CR_AMT,0)), 'FM999,999,990.00') AS "إجمالي التسويات والدائن",
                TO_CHAR(SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)), 'FM999,999,990.00') AS "الصافي المالي"
         FROM IAS20261.IAS_POST_DTL p
         JOIN IAS20261.ACCOUNT a ON a.A_CODE = p.A_CODE
         WHERE (p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%' OR p.A_CODE LIKE '11402%' OR p.A_CODE LIKE '21104%')
           AND NVL(p.DOC_POST, 0) = 1
           AND p.DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD')
           AND p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD') + 1
         GROUP BY p.A_CODE, a.A_NAME
         ORDER BY SUM(NVL(p.DR_AMT,0)) DESC
         \"\"\"},"""

if old_report_block in content:
    new_content = content.replace(old_report_block, new_report_block)
    with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully updated payroll_financial_summary report!")
else:
    print("Error: Could not find old_report_block in app.py")
