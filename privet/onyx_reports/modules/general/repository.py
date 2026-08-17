# -*- coding: utf-8 -*-
from database import get_conn

# SQL functions for GENERAL reports
def get_daily_expenses_sql():
    return """
      SELECT TO_CHAR(d.DOC_DATE, 'YYYY-MM-DD') AS "التاريخ",
             d.DOC_NO AS "رقم المستند",
             CASE d.DOC_TYPE 
               WHEN 1 THEN 'قيد يومية'
               WHEN 2 THEN 'سند قبض'
               WHEN 3 THEN 'سند صرف'
               ELSE TO_CHAR(d.DOC_TYPE)
             END AS "نوع المستند",
             d.A_CODE AS "رقم الحساب",
             MAX(a.A_NAME) AS "اسم الحساب",
             MAX(d.DOC_DESC) AS "البيان / الشرح",
             TO_CHAR(d.DR_AMT, 'FM999,999,990.00') AS "المبلغ",
             TO_CHAR(d.CC_CODE) AS "مركز التكلفة",
             MAX(cc.CC_A_NAME) AS "اسم مركز التكلفة"
      FROM IAS20261.IAS_POST_DTL d
      LEFT JOIN IAS20261.ACCOUNT a ON d.A_CODE = a.A_CODE
      LEFT JOIN IAS20261.COST_CENTERS cc ON d.CC_CODE = cc.CC_CODE
      WHERE d.DR_AMT > 0 
        AND d.A_CODE LIKE '3%'
        AND d.DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD')
        AND d.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD') + 1
        AND (:ac_code IS NULL OR :ac_code = '' OR d.A_CODE = :ac_code)
        AND (:text_search IS NULL OR :text_search = '' OR d.DOC_DESC LIKE '%' || :text_search || '%')
      GROUP BY d.DOC_DATE, d.DOC_NO, d.DOC_TYPE, d.A_CODE, d.DR_AMT, d.CC_CODE
      ORDER BY d.DOC_DATE DESC, d.DOC_NO DESC
    """

def get_detailed_net_jrn_sql():
    return """
      SELECT TO_CHAR(p.DOC_DATE,'YYYY-MM-DD') AS "التاريخ",
             p.DOC_NO AS "رقم القيد",
             p.C_CODE AS "كود العميل",
             MAX(c.C_A_NAME) AS "اسم العميل",
             p.REP_CODE AS "كود المندوب",
             MAX(sm.REPRS_A_NAME) AS "اسم المندوب",
             p.A_CODE AS "كود الحساب",
             MAX(a.A_NAME) AS "اسم الحساب",
             MAX(p.DOC_DESC) AS "البيان",
             TO_CHAR(SUM(NVL(p.CR_AMT,0)),'FM999,999,990.00') AS "المبلغ"
      FROM IAS20261.IAS_POST_DTL p
      LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
      LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE = p.REP_CODE
      LEFT JOIN IAS20261.ACCOUNT a ON a.A_CODE = p.A_CODE
      WHERE NVL(p.DOC_POST,0) = 1 
        AND p.DOC_TYPE = 1 
        AND p.JV_TYPE = 2 
        AND NVL(p.CR_AMT,0) > 0
        AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
        AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        AND (:rep_code IS NULL OR p.REP_CODE = :rep_code)
        AND (:c_code IS NULL OR p.C_CODE = :c_code)
      GROUP BY p.DOC_DATE, p.DOC_NO, p.C_CODE, p.REP_CODE, p.A_CODE
      ORDER BY p.DOC_DATE DESC, p.DOC_NO DESC
    """

