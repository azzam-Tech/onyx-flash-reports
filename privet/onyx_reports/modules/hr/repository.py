# -*- coding: utf-8 -*-
from database import get_conn

# SQL functions for HR reports
def get_emp_directory_sql():
    return """
         SELECT e.EMP_NO AS "كود الموظف",
                TRIM(e.EMP_L_NM) AS "اسم الموظف والوظيفة",
                TO_CHAR(e.STRT_WRK_DATE, 'YYYY-MM-DD') AS "تاريخ المباشرة",
                CASE WHEN NVL(e.INACTIVE, 0) = 0 THEN 'نشط' ELSE 'موقوف/مستقيل' END AS "حالة الموظف",
                CASE WHEN e.SLRY_PAY_WAY = 2 THEN 'تحويل بنكي' WHEN e.SLRY_PAY_WAY = 1 THEN 'تسليم نقدي' ELSE 'غير محدد' END AS "طريقة استلام الراتب",
                CASE WHEN NVL(e.SLRY_CALC, 0) = 1 THEN 'شهري' WHEN NVL(e.SLRY_CALC, 0) = 2 THEN 'يومي' ELSE 'معياري' END AS "احتساب الراتب",
                TO_CHAR(NVL(e.WRK_HRS_DY, 8)) AS "ساعات العمل/يوم",
                TO_CHAR(NVL(e.WRK_DY_MNTH, 30)) AS "أيام العمل/شهر"
         FROM S_EMP e
         WHERE (:emp_status IS NULL OR (:emp_status = '1' AND NVL(e.INACTIVE, 0) = 0) OR (:emp_status = '0' AND NVL(e.INACTIVE, 0) = 1))
           AND (:emp_search IS NULL OR TO_CHAR(e.EMP_NO) LIKE '%' || :emp_search || '%' OR e.EMP_L_NM LIKE '%' || :emp_search || '%')
         ORDER BY e.EMP_NO
         """

def get_payroll_financial_summary_sql():
    return """
         SELECT p.A_CODE AS "كود الحساب",
                a.A_NAME AS "اسم البند المحاسبي",
                COUNT(*) AS "عدد الحركات",
                TO_CHAR(SUM(NVL(p.DR_AMT,0)), 'FM999,999,990.00') AS "إجمالي الصرف والرواتب",
                TO_CHAR(SUM(NVL(p.CR_AMT,0)), 'FM999,999,990.00') AS "إجمالي التسويات والدائن",
                TO_CHAR(SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)), 'FM999,999,990.00') AS "الصافي المالي"
         FROM IAS_POST_DTL p
         JOIN ACCOUNT a ON a.A_CODE = p.A_CODE
         WHERE (p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%' OR p.A_CODE LIKE '11402%' OR p.A_CODE LIKE '21104%')
           AND NVL(p.DOC_POST, 0) = 1
           AND p.DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD')
           AND p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD') + 1
         GROUP BY p.A_CODE, a.A_NAME
         ORDER BY SUM(NVL(p.DR_AMT,0)) DESC
         """

def get_employee_advances_loans_sql():
    return """
         SELECT TO_CHAR(p.DOC_DATE, 'YYYY-MM-DD') AS "التاريخ",
                p.DOC_NO AS "رقم المستند",
                CASE p.DOC_TYPE WHEN 1 THEN 'قيد يومية' WHEN 2 THEN 'سند قبض' WHEN 3 THEN 'سند صرف' ELSE 'قيد أونكس' END AS "نوع المستند",
                NVL(sm.REPRS_A_NAME, TO_CHAR(p.CC_CODE)) AS "الجهة / مركز التكلفة",
                TO_CHAR(NVL(p.DR_AMT, 0), 'FM999,999,990.00') AS "سلفة / راتب / مدين",
                TO_CHAR(NVL(p.CR_AMT, 0), 'FM999,999,990.00') AS "سداد / تسوية / دائن",
                NVL(p.DOC_DESC, 'قيد تلقائي') AS "اسم الموظف / البيان والتفاصيل"
         FROM IAS_POST_DTL p
         LEFT JOIN SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(p.CC_CODE)
         WHERE (p.A_CODE LIKE '11402%' OR p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%')
           AND NVL(p.DOC_POST, 0) = 1
           AND p.DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD')
           AND p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD') + 1
           AND (:min_amt IS NULL OR NVL(p.DR_AMT, 0) >= TO_NUMBER(:min_amt) OR NVL(p.CR_AMT, 0) >= TO_NUMBER(:min_amt))
           AND (:max_amt IS NULL OR (NVL(p.DR_AMT, 0) <= TO_NUMBER(:max_amt) AND NVL(p.CR_AMT, 0) <= TO_NUMBER(:max_amt)))
           AND (:text_search IS NULL OR p.DOC_DESC LIKE '%' || :text_search || '%' OR sm.REPRS_A_NAME LIKE '%' || :text_search || '%')
         ORDER BY p.DOC_DATE DESC, p.DOC_NO DESC
         """

def get_salesmen_hr_link_sql():
    return """
         SELECT sm.REPRS_CODE AS "كود المندوب",
                sm.REPRS_A_NAME AS "اسم المندوب في المبيعات",
                NVL(e.EMP_NO, sm.REPRS_CODE) AS "كود الموظف المربوط",
                NVL(TRIM(e.EMP_L_NM), 'غير موصول برقم موظف') AS "اسم الموظف في HR",
                CASE WHEN e.EMP_NO IS NOT NULL THEN 'مربوط بسجل HR' ELSE 'غير مربوط' END AS "حالة الربط"
         FROM SALES_MAN sm
         LEFT JOIN S_EMP e ON e.EMP_NO = sm.REPRS_CODE
         WHERE (:rep_code IS NULL OR sm.REPRS_CODE = :rep_code)
         ORDER BY sm.REPRS_CODE
         """

