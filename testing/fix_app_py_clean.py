with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

# We want to replace from `  {"id":"hr",` (which appears around line 993) to `TABMAP = {t["id"]: t for t in TABS}`
hr_clean_code = """  {"id":"hr","title":"الموظفين والرواتب","icon":"M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z","reports":[
         {"id":"payroll_financial_summary","title":"كشف الرواتب والتأمينات والبدلات المالي","params":[DFROM,DTO,GRP],"sql":\"\"\"
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
         \"\"\"},
         {"id":"employee_advances_loans","title":"كشف حركة ذمم وسلف الموظفين والمناديب","params":[DFROM,DTO,REP],"sql":\"\"\"
         SELECT TO_CHAR(p.DOC_DATE, 'YYYY-MM-DD') AS "التاريخ",
                p.DOC_NO AS "رقم المستند",
                CASE p.DOC_TYPE WHEN 1 THEN 'قيد يومية' WHEN 2 THEN 'سند قبض' WHEN 3 THEN 'سند صرف' ELSE 'قيد أونكس' END AS "نوع المستند",
                NVL(sm.REPRS_A_NAME, TO_CHAR(p.CC_CODE)) AS "المندوب / مركز التكلفة",
                p.A_CODE AS "حساب الذمم",
                TO_CHAR(NVL(p.DR_AMT, 0), 'FM999,999,990.00') AS "سلفة / مدين",
                TO_CHAR(NVL(p.CR_AMT, 0), 'FM999,999,990.00') AS "سداد / دائن",
                NVL(p.DOC_DESC, 'قيد تلقائي') AS "البيان / الشرح"
         FROM IAS20261.IAS_POST_DTL p
         LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(p.CC_CODE)
         WHERE p.A_CODE LIKE '11402%'
           AND NVL(p.DOC_POST, 0) = 1
           AND p.DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD')
           AND p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD') + 1
           AND (:rep_code IS NULL OR TO_CHAR(p.CC_CODE) = :rep_code)
         ORDER BY p.DOC_DATE DESC, p.DOC_NO DESC
         FETCH FIRST 300 ROWS ONLY
         \"\"\"},
         {"id":"emp_directory","title":"دليل أسماء الموظفين والسجلات الإدارية","params":[EMPST,EMPSRCH],"sql":\"\"\"
         SELECT e.EMP_NO AS "كود الموظف",
                TRIM(e.EMP_L_NM) AS "اسم الموظف",
                TO_CHAR(e.STRT_WRK_DATE, 'YYYY-MM-DD') AS "تاريخ المباشرة",
                CASE WHEN NVL(e.INACTIVE, 0) = 0 THEN 'نشط' ELSE 'موقوف/مستقيل' END AS "حالة الموظف",
                CASE WHEN NVL(e.SLRY_CALC, 0) = 1 THEN 'شهري' WHEN NVL(e.SLRY_CALC, 0) = 2 THEN 'يومي' ELSE 'معياري' END AS "احتساب الراتب",
                TO_CHAR(NVL(e.WRK_HRS_DY, 8)) AS "ساعات العمل/يوم",
                TO_CHAR(NVL(e.WRK_DY_MNTH, 30)) AS "أيام العمل/شهر"
         FROM IAS20261.S_EMP e
         WHERE (:emp_status IS NULL OR (:emp_status = '1' AND NVL(e.INACTIVE, 0) = 0) OR (:emp_status = '0' AND NVL(e.INACTIVE, 0) = 1))
           AND (:emp_search IS NULL OR TO_CHAR(e.EMP_NO) LIKE '%' || :emp_search || '%' OR e.EMP_L_NM LIKE '%' || :emp_search || '%')
         ORDER BY e.EMP_NO
         \"\"\"},
         {"id":"salesmen_hr_link","title":"ربط المناديب بسجل الموظفين","params":[REP],"sql":\"\"\"
         SELECT sm.REPRS_CODE AS "كود المندوب",
                sm.REPRS_A_NAME AS "اسم المندوب في المبيعات",
                NVL(e.EMP_NO, sm.REPRS_CODE) AS "كود الموظف المربوط",
                NVL(TRIM(e.EMP_L_NM), 'غير موصول برقم موظف') AS "اسم الموظف في HR",
                CASE WHEN e.EMP_NO IS NOT NULL THEN 'مربوط بسجل HR' ELSE 'غير مربوط' END AS "حالة الربط"
         FROM IAS20261.SALES_MAN sm
         LEFT JOIN IAS20261.S_EMP e ON e.EMP_NO = sm.REPRS_CODE
         WHERE (:rep_code IS NULL OR sm.REPRS_CODE = :rep_code)
         ORDER BY sm.REPRS_CODE
         \"\"\"}
  ]},
]

"""

start_pos = content.find('  {"id":"hr",')
end_pos = content.find('TABMAP = {t["id"]: t for t in TABS}')

if start_pos != -1 and end_pos != -1:
    new_content = content[:start_pos] + hr_clean_code + content[end_pos:]
    with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully replaced HR section cleanly!")
else:
    print(f"Error: start_pos={start_pos}, end_pos={end_pos}")
