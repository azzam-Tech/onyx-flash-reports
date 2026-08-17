# -*- coding: utf-8 -*-
from database import get_conn

# SQL functions for AR reports
def get_balances_sql():
    return """
      SELECT p.C_CODE AS "كود العميل",
             MAX(c.C_A_NAME) AS "اسم العميل",
             MAX(c.REP_CODE) AS "المندوب",
             TO_CHAR(SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0)),'FM999,999,999,990.00') AS "الرصيد (مدين)"
      FROM IAS20261.IAS_POST_DTL p
      LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE=p.C_CODE
      WHERE p.C_CODE IS NOT NULL
        AND NVL(p.DOC_POST,0)=1
        AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        AND (:c_code IS NULL OR TO_CHAR(p.C_CODE) LIKE '%' || :c_code || '%' OR c.C_A_NAME LIKE '%' || :c_code || '%')
        AND (:rep_code IS NULL OR TO_CHAR(c.REP_CODE) = :rep_code)
      GROUP BY p.C_CODE
      HAVING SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0)) <> 0
      ORDER BY SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0)) DESC"""

def get_statement_sql():
    return """
       WITH open_bal AS (
         SELECT NVL(SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0)),0) as bal
         FROM IAS20261.IAS_POST_DTL
         WHERE C_CODE = :c_code AND NVL(DOC_POST,0)=1
           AND (DOC_DATE < TO_DATE(:date_from,'YYYY-MM-DD') OR NVL(DOC_TYPE,0) = 0)
       ),
       trans AS (
         SELECT p.DOC_DATE, NVL(d.JV_NAME, 'قيد يومية') AS jv_name, p.DOC_NO, p.DOC_DESC,
                NVL(p.DR_AMT,0) dr, NVL(p.CR_AMT,0) cr, p.DOC_SER
         FROM IAS20261.IAS_POST_DTL p
         LEFT JOIN IAS_SYS.IAS_DOCJV_TYPE_SYSTEMS d ON d.DOC_TYPE=p.DOC_TYPE AND d.JV_TYPE=1 AND d.LANG_NO=1
         WHERE p.C_CODE = :c_code AND NVL(p.DOC_POST,0)=1
           AND NVL(p.DOC_TYPE,0) <> 0
           AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
           AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       )
       SELECT "التاريخ","نوع المستند","رقم المستند","البيان","مدين","دائن","الرصيد" FROM (
         SELECT TO_CHAR(TO_DATE(:date_from,'YYYY-MM-DD')-1, 'YYYY-MM-DD') AS "التاريخ",
                'رصيد افتتاحي' AS "نوع المستند",
                NULL AS "رقم المستند",
                'رصيد ما قبل الفترة' AS "البيان",
                TO_CHAR(CASE WHEN bal>0 THEN bal ELSE 0 END,'FM999,999,990.00') AS "مدين",
                TO_CHAR(CASE WHEN bal<0 THEN -bal ELSE 0 END,'FM999,999,990.00') AS "دائن",
                TO_CHAR(NVL(bal,0),'FM999,999,990.00') AS "الرصيد",
                TO_DATE('1900-01-01','YYYY-MM-DD') s1, 0 s2, 0 s3
         FROM open_bal
         UNION ALL
         SELECT TO_CHAR(t.DOC_DATE,'YYYY-MM-DD'),
                t.jv_name,
                t.DOC_NO,
                t.DOC_DESC,
                TO_CHAR(t.dr,'FM999,999,990.00'),
                TO_CHAR(t.cr,'FM999,999,990.00'),
                TO_CHAR((SELECT NVL(bal,0) FROM open_bal) + SUM(t.dr-t.cr) OVER (ORDER BY t.DOC_DATE, t.DOC_NO, t.DOC_SER), 'FM999,999,990.00'),
                t.DOC_DATE s1, t.DOC_NO s2, t.DOC_SER s3
         FROM trans t
       ) ORDER BY s1, s2, s3"""

def get_statement_analytic_sql():
    return """
       WITH open_bal AS (
         SELECT NVL(SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0)),0) as bal
         FROM IAS20261.IAS_POST_DTL
         WHERE (AC_CODE_DTL = :ac_code_dtl OR C_V_CODE = :ac_code_dtl OR V_C_CODE = :ac_code_dtl) AND NVL(DOC_POST,0)=1
           AND (DOC_DATE < TO_DATE(:date_from,'YYYY-MM-DD') OR NVL(DOC_TYPE,0) = 0)
       ),
       trans AS (
         SELECT p.DOC_DATE, NVL(d.JV_NAME, 'قيد يومية') AS jv_name, p.DOC_NO, p.DOC_DESC, p.REF_NO,
                NVL(p.DR_AMT,0) dr, NVL(p.CR_AMT,0) cr, p.DOC_SER
         FROM IAS20261.IAS_POST_DTL p
         LEFT JOIN IAS_SYS.IAS_DOCJV_TYPE_SYSTEMS d ON d.DOC_TYPE=p.DOC_TYPE AND d.JV_TYPE=1 AND d.LANG_NO=1
         WHERE (p.AC_CODE_DTL = :ac_code_dtl OR p.C_V_CODE = :ac_code_dtl OR p.V_C_CODE = :ac_code_dtl) AND NVL(p.DOC_POST,0)=1
           AND NVL(p.DOC_TYPE,0) <> 0
           AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
           AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       )
       SELECT "التاريخ","نوع المستند","رقم المستند","البيان","رقم المرجع","مدين","دائن","الرصيد" FROM (
         SELECT NULL AS "التاريخ",
                NULL AS "نوع المستند",
                NULL AS "رقم المستند",
                'الرصيد الإفتتاحي' AS "البيان",
                NULL AS "رقم المرجع",
                TO_CHAR(CASE WHEN bal>0 THEN bal ELSE 0 END,'FM999,999,990.00') AS "مدين",
                TO_CHAR(CASE WHEN bal<0 THEN -bal ELSE 0 END,'FM999,999,990.00') AS "دائن",
                NULL AS "الرصيد",
                TO_DATE('1900-01-01','YYYY-MM-DD') s1, 0 s2, 0 s3
         FROM open_bal
         UNION ALL
         SELECT TO_CHAR(t.DOC_DATE,'YYYY-MM-DD'),
                t.jv_name,
                TO_CHAR(t.DOC_NO),
                t.DOC_DESC,
                t.REF_NO,
                TO_CHAR(t.dr,'FM999,999,990.00'),
                TO_CHAR(t.cr,'FM999,999,990.00'),
                TO_CHAR((SELECT NVL(bal,0) FROM open_bal) + SUM(t.dr-t.cr) OVER (ORDER BY t.DOC_DATE, t.DOC_NO, t.DOC_SER), 'FM999,999,990.00'),
                t.DOC_DATE s1, t.DOC_NO s2, t.DOC_SER s3
         FROM trans t
       ) ORDER BY s1, s2, s3"""

def get_dormant_sql():
    return """
     SELECT * FROM (
       SELECT c.C_CODE AS "كود العميل", c.C_A_NAME AS "اسم العميل", c.REP_CODE AS "المندوب",
              TO_CHAR(lb.last_bill,'YYYY-MM-DD') AS "آخر فاتورة",
              (TRUNC(TO_DATE(:as_of,'YYYY-MM-DD'))-TRUNC(lb.last_bill)) AS "أيام منذ آخر تعامل"
       FROM IAS20261.CUSTOMER c
       LEFT JOIN (SELECT C_CODE, MAX(BILL_DATE) last_bill FROM IAS20261.IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) GROUP BY C_CODE) lb ON lb.C_CODE=c.C_CODE
       WHERE NVL(c.INACTIVE,0)=0 AND (lb.last_bill IS NULL OR lb.last_bill < TO_DATE(:as_of,'YYYY-MM-DD') - :days)
       ORDER BY lb.last_bill NULLS FIRST
     ) """

