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
      FROM IAS_POST_DTL d
      LEFT JOIN ACCOUNT a ON d.A_CODE = a.A_CODE
      LEFT JOIN COST_CENTERS cc ON d.CC_CODE = cc.CC_CODE
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
      FROM IAS_POST_DTL p
      LEFT JOIN CUSTOMER c ON c.C_CODE = p.C_CODE
      LEFT JOIN SALES_MAN sm ON sm.REPRS_CODE = p.REP_CODE
      LEFT JOIN ACCOUNT a ON a.A_CODE = p.A_CODE
      WHERE NVL(p.DOC_POST,0) = 1 
        AND p.DOC_TYPE = 1 
        AND p.JV_TYPE = 2 
        AND NVL(p.CR_AMT,0) > 0
        AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
        AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        AND (:rep_code IS NULL OR :rep_code = '' OR p.REP_CODE = :rep_code)
        AND (:c_code IS NULL OR :c_code = '' OR p.C_CODE = :c_code)
      GROUP BY TO_CHAR(p.DOC_DATE,'YYYY-MM-DD'), p.DOC_NO, p.C_CODE, p.REP_CODE, p.A_CODE
      ORDER BY TO_CHAR(p.DOC_DATE,'YYYY-MM-DD') DESC, p.DOC_NO DESC
    """

def get_item_prices_and_stock_sql():
    return """
        SELECT 
            G.G_A_NAME AS "المجموعة الرئيسية للصنف",
            I.I_CODE AS "كود الصنف",
            I.I_NAME AS "اسم الصنف",
            NVL((SELECT MAX(P.I_PRICE) FROM IAS_ITEM_PRICE P WHERE P.I_CODE = I.I_CODE AND P.LEV_NO = 1), 0) AS "التكلفة علينا",
            NVL((SELECT MAX(P.I_PRICE) FROM IAS_ITEM_PRICE P WHERE P.I_CODE = I.I_CODE AND P.LEV_NO = 2), 0) AS "الحد الادنى",
            NVL((SELECT SUM(M.I_QTY * NVL(M.IN_OUT, 1)) FROM ITEM_MOVEMENT M WHERE M.I_CODE = I.I_CODE AND M.W_CODE IN ('103','105','108')), 0) AS "الكمية (الرياض)",
            NVL((SELECT SUM(M.I_QTY * NVL(M.IN_OUT, 1)) FROM ITEM_MOVEMENT M WHERE M.I_CODE = I.I_CODE AND M.W_CODE = '118'), 0) AS "الكمية (الجنوب)",
            NVL((SELECT SUM(M.I_QTY * NVL(M.IN_OUT, 1)) FROM ITEM_MOVEMENT M WHERE M.I_CODE = I.I_CODE AND M.W_CODE = '122'), 0) AS "الكمية (الشمال)",
            NVL((SELECT SUM(M.I_QTY * NVL(M.IN_OUT, 1)) FROM ITEM_MOVEMENT M WHERE M.I_CODE = I.I_CODE AND M.W_CODE = '121'), 0) AS "الكمية (جدة)",
            NVL((SELECT SUM(M.I_QTY * NVL(M.IN_OUT, 1)) FROM ITEM_MOVEMENT M WHERE M.I_CODE = I.I_CODE AND M.W_CODE = '119'), 0) AS "الكمية (الدمام)"
        FROM IAS_ITM_MST I
        LEFT JOIN GROUP_DETAILS G ON G.G_CODE = I.G_CODE
        WHERE (:i_code IS NULL OR :i_code = '' OR I.I_CODE = :i_code)
          AND NVL(I.INACTIVE, 0) = 0
          AND NVL((SELECT SUM(M.I_QTY * NVL(M.IN_OUT, 1)) FROM ITEM_MOVEMENT M WHERE M.I_CODE = I.I_CODE AND M.W_CODE IN ('103','105','108','118','122','121','119')), 0) != 0
        ORDER BY I.G_CODE, I.I_CODE
    """
