# -*- coding: utf-8 -*-
from database import get_conn

# SQL functions for TAX reports
def get_vat_decl_sql():
    return """
     SELECT PRD_NM AS "الفترة",
       TO_CHAR(-(SUM(CASE WHEN DOC_TYPE IN (4,5,15) THEN DOC_AMT_VAT ELSE 0 END)),'FM999,999,999,990.00') AS "المبيعات الخاضعة",
       TO_CHAR(-(SUM(CASE WHEN DOC_TYPE IN (4,5,15) THEN VAT_AMT ELSE 0 END)),'FM999,999,999,990.00') AS "ضريبة المخرجات",
       TO_CHAR(SUM(CASE WHEN DOC_TYPE IN (6,7,16) THEN DOC_AMT_VAT ELSE 0 END),'FM999,999,999,990.00') AS "المشتريات الخاضعة",
       TO_CHAR(SUM(CASE WHEN DOC_TYPE IN (6,7,16) THEN VAT_AMT ELSE 0 END),'FM999,999,999,990.00') AS "ضريبة المدخلات",
       TO_CHAR(SUM(CASE WHEN DOC_TYPE IN (1,3) THEN VAT_AMT ELSE 0 END),'FM999,999,999,990.00') AS "تعديلات",
       TO_CHAR(-(SUM(VAT_AMT)),'FM999,999,999,990.00') AS "صافي الضريبة المستحقة"
     FROM IAS20261.GNR_TAX_SUM_VW
     GROUP BY PRD_NO, PRD_NM ORDER BY PRD_NO"""

def get_vat_out_sql():
    return """
     SELECT PRD_NM AS "الفترة", DOC_TYP_NAME AS "نوع المستند",
       TO_CHAR(-(SUM(DOC_AMT_VAT)),'FM999,999,999,990.00') AS "الوعاء الخاضع",
       TO_CHAR(-(SUM(VAT_AMT)),'FM999,999,999,990.00') AS "الضريبة"
     FROM IAS20261.GNR_TAX_SUM_VW WHERE DOC_TYPE IN (4,5,15)
     GROUP BY PRD_NO, PRD_NM, DOC_TYPE, DOC_TYP_NAME ORDER BY PRD_NO, DOC_TYPE"""

def get_vat_in_sql():
    return """
     SELECT PRD_NM AS "الفترة", DOC_TYP_NAME AS "نوع المستند",
       TO_CHAR(SUM(DOC_AMT_VAT),'FM999,999,999,990.00') AS "الوعاء الخاضع",
       TO_CHAR(SUM(VAT_AMT),'FM999,999,999,990.00') AS "الضريبة"
     FROM IAS20261.GNR_TAX_SUM_VW WHERE DOC_TYPE IN (6,7,16,1,3)
     GROUP BY PRD_NO, PRD_NM, DOC_TYPE, DOC_TYP_NAME ORDER BY PRD_NO, DOC_TYPE"""

