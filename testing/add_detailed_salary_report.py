with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

old_hr_header = """  {"id":"hr","title":"الموظفين والرواتب","icon":"M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z","reports":["""

new_hr_header = """  {"id":"hr","title":"الموظفين والرواتب","icon":"M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z","reports":[
         {"id":"employee_salaries_detailed","title":"كشف رواتب ومستحقات الموظفين التفصيلي","params":[DFROM,DTO,EMPSRCH],"sql":\"\"\"
         SELECT e.EMP_NO AS "كود الموظف",
                TRIM(e.EMP_L_NM) AS "اسم الموظف",
                CASE WHEN NVL(e.INACTIVE, 0) = 0 THEN 'نشط' ELSE 'موقوف/مستقيل' END AS "حالة الموظف",
                TO_CHAR(SUM(CASE WHEN p.A_CODE = '321010003' THEN NVL(p.DR_AMT,0) ELSE 0 END), 'FM999,999,990.00') AS "رواتب التأمينات",
                TO_CHAR(SUM(CASE WHEN p.A_CODE = '321010004' THEN NVL(p.DR_AMT,0) ELSE 0 END), 'FM999,999,990.00') AS "رواتب مؤقتة وعقود",
                TO_CHAR(SUM(CASE WHEN p.A_CODE LIKE '324%' THEN NVL(p.DR_AMT,0) ELSE 0 END), 'FM999,999,990.00') AS "البدلات والمزايا",
                TO_CHAR(SUM(CASE WHEN p.A_CODE LIKE '11402%' THEN NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0) ELSE 0 END), 'FM999,999,990.00') AS "رصيد الذمم والسلف",
                TO_CHAR(SUM(CASE WHEN p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%' THEN NVL(p.DR_AMT,0) ELSE 0 END), 'FM999,999,990.00') AS "إجمالي المستحقات"
         FROM IAS20261.S_EMP e
         LEFT JOIN IAS20261.IAS_POST_DTL p ON (p.EMP_NO = e.EMP_NO OR p.CC_CODE = e.EMP_NO) AND NVL(p.DOC_POST,0)=1
            AND p.DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD')
            AND p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD') + 1
         WHERE (:emp_search IS NULL OR TO_CHAR(e.EMP_NO) LIKE '%' || :emp_search || '%' OR e.EMP_L_NM LIKE '%' || :emp_search || '%')
         GROUP BY e.EMP_NO, e.EMP_L_NM, NVL(e.INACTIVE, 0)
         HAVING (SUM(CASE WHEN p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%' THEN NVL(p.DR_AMT,0) ELSE 0 END) > 0 OR SUM(CASE WHEN p.A_CODE LIKE '11402%' THEN NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0) ELSE 0 END) <> 0)
         ORDER BY SUM(CASE WHEN p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%' THEN NVL(p.DR_AMT,0) ELSE 0 END) DESC
         \"\"\"},"""

if old_hr_header in content:
    new_content = content.replace(old_hr_header, new_hr_header)
    with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully added employee_salaries_detailed report to app.py!")
else:
    print("Error: Could not find old_hr_header in app.py")
