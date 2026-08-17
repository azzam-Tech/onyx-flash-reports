# -*- coding: utf-8 -*-
from database import get_conn

# SQL functions for Finance reports
def get_trial_balance_sql():
    return """
     SELECT * FROM (
       SELECT p.A_CODE AS "رقم الحساب", MAX(a.A_NAME) AS "اسم الحساب",
              TO_CHAR(SUM(NVL(p.DR_AMT,0)),'FM999,999,999,990.00') AS "إجمالي مدين",
              TO_CHAR(SUM(NVL(p.CR_AMT,0)),'FM999,999,999,990.00') AS "إجمالي دائن",
              TO_CHAR(SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0)),'FM999,999,999,990.00') AS "الرصيد"
       FROM IAS20261.IAS_POST_DTL p LEFT JOIN IAS20261.ACCOUNT a ON a.A_CODE=p.A_CODE
       WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       GROUP BY p.A_CODE HAVING SUM(NVL(p.DR_AMT,0))<>0 OR SUM(NVL(p.CR_AMT,0))<>0
       ORDER BY p.A_CODE
     ) """

def get_income_statement_sql():
    return """
     SELECT NVL(pa.A_NAME, a.A_PARENT) AS "البند",
            TO_CHAR(SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)),'FM999,999,999,990.00') AS "الصافي"
     FROM IAS20261.IAS_POST_DTL p
     JOIN IAS20261.ACCOUNT a ON a.A_CODE=p.A_CODE
     LEFT JOIN IAS20261.ACCOUNT pa ON pa.A_CODE=a.A_PARENT
     WHERE NVL(p.DOC_POST,0)=1 AND a.A_REPORT=2
       AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
     GROUP BY a.A_PARENT, pa.A_NAME
     ORDER BY SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)) DESC"""

def get_cost_centers_sql():
    return """
     SELECT * FROM (
       SELECT p.CC_CODE AS "مركز التكلفة", MAX(cc.CC_A_NAME) AS "الاسم",
              TO_CHAR(SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)),'FM999,999,999,990.00') AS "صافي الربح/الخسارة"
       FROM IAS20261.IAS_POST_DTL p JOIN IAS20261.ACCOUNT a ON a.A_CODE=p.A_CODE
       LEFT JOIN IAS20261.COST_CENTERS cc ON cc.CC_CODE=p.CC_CODE
       WHERE NVL(p.DOC_POST,0)=1 AND a.A_REPORT=2
         AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       GROUP BY p.CC_CODE HAVING SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0))<>0
       ORDER BY SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)) DESC
     ) """

def get_journal_sql():
    return """
     SELECT * FROM (
       SELECT TO_CHAR(p.DOC_DATE,'YYYY-MM-DD') AS "التاريخ", d.JV_NAME AS "نوع القيد",
              p.DOC_NO AS "رقم المستند", p.A_CODE AS "رقم الحساب", a.A_NAME AS "اسم الحساب",
              p.DOC_DESC AS "البيان",
              TO_CHAR(NVL(p.DR_AMT,0),'FM999,999,990.00') AS "مدين",
              TO_CHAR(NVL(p.CR_AMT,0),'FM999,999,990.00') AS "دائن"
       FROM IAS20261.IAS_POST_DTL p
       LEFT JOIN IAS20261.ACCOUNT a ON a.A_CODE=p.A_CODE
       LEFT JOIN IAS20261.JV_TYPES d ON d.JV_TYPE=p.JV_TYPE
       WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND (:a_code IS NULL OR p.A_CODE = :a_code)
       ORDER BY p.DOC_DATE DESC, p.DOC_NO DESC, p.DOC_SER
     ) """

def get_perf_aging_dynamic_analytical_sql():
    return """
       -- This report dynamically processes valid collections via Python FIFO per customer
       SELECT 'Dynamic Analytical' as "Placeholder" FROM DUAL
       """

def get_perf_aging_dynamic_sql():
    return """
       -- This report dynamically processes valid collections via Python FIFO
       SELECT 'Dynamic' as "Placeholder" FROM DUAL
       """

def get_perf_aging_exact_sql():
    return """
     WITH cr AS (
       SELECT C_CODE,
         SUM(CASE WHEN PER_NO BETWEEN 0 AND 30   THEN DR_AMT ELSE 0 END) pos,
         SUM(CASE WHEN PER_NO BETWEEN -30 AND -1 THEN DR_AMT ELSE 0 END) neg,
         SUM(CASE WHEN PER_NO BETWEEN 31 AND 60  THEN DR_AMT ELSE 0 END) b2,
         SUM(CASE WHEN PER_NO BETWEEN 61 AND 90  THEN DR_AMT ELSE 0 END) b3,
         SUM(CASE WHEN PER_NO BETWEEN 91 AND 120 THEN DR_AMT ELSE 0 END) b4,
         SUM(CASE WHEN PER_NO > 120              THEN DR_AMT ELSE 0 END) b5,
         SUM(DR_AMT) crlim
       FROM IAS20261.IAS_CRLIMIT_TMP
       WHERE DOC_TYPE<>1 AND DOC_TYPE_REF IN (1,2)
         AND PAID_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND PAID_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       GROUP BY C_CODE),
     co AS (
       SELECT C_CODE, SUM(CR_AMT) col FROM IAS20261.IAS_COL_TMP
       WHERE DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       GROUP BY C_CODE),
     perc AS (
       SELECT cr.C_CODE,
         CASE WHEN cr.pos > 0 THEN cr.pos + cr.neg + GREATEST(0, NVL(co.col,0) - cr.crlim) ELSE 0 END b1,
         cr.b2, cr.b3, cr.b4, cr.b5
       FROM cr LEFT JOIN co ON co.C_CODE = cr.C_CODE)
     SELECT * FROM (
       SELECT c.REP_CODE AS "كود المندوب", MAX(sm.REPRS_A_NAME) AS "اسم المندوب",
              COUNT(DISTINCT perc.C_CODE) AS "عدد العملاء",
              TO_CHAR(SUM(perc.b1),'FM999,999,990.00') AS "0-30",
              TO_CHAR(SUM(perc.b2),'FM999,999,990.00') AS "31-60",
              TO_CHAR(SUM(perc.b3),'FM999,999,990.00') AS "61-90",
              TO_CHAR(SUM(perc.b4),'FM999,999,990.00') AS "91-120",
              TO_CHAR(SUM(perc.b5),'FM999,999,990.00') AS "أكثر من 120",
              TO_CHAR(SUM(perc.b1+perc.b2+perc.b3+perc.b4+perc.b5),'FM999,999,990.00') AS "إجمالي التحصيل"
       FROM perc JOIN IAS20261.CUSTOMER c ON c.C_CODE=perc.C_CODE
       LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=c.REP_CODE
       WHERE (:rep_code IS NULL OR c.REP_CODE = :rep_code)
       GROUP BY c.REP_CODE ORDER BY SUM(perc.b1+perc.b2+perc.b3+perc.b4+perc.b5) DESC
     ) """

