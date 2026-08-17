# -*- coding: utf-8 -*-
from database import get_conn

# SQL functions for Sales reports
def get_bills_sql():
    return """
    WITH sales_invoices AS (
      SELECT CASE b.BILL_DOC_TYPE 
               WHEN 1 THEN 'مبيعات نقدية' 
               WHEN 4 THEN 'مبيعات آجلة' 
               ELSE 'مبيعات أخرى' 
             END AS doc_type_name,
             b.BILL_DOC_TYPE as doc_type,
             b.BILL_NO as bill_no,
             b.BILL_DATE as bill_date,
             TO_CHAR(b.C_CODE) as c_code,
             c.C_A_NAME as c_name,
             TO_CHAR(b.REP_CODE) as rep_code,
             sm.REPRS_A_NAME as rep_name,
             NVL(b.BILL_AMT,0) as gross_amt,
             NVL(b.DISC_AMT,0) as disc_amt,
             NVL(b.VAT_AMT,0) as vat_amt,
             (NVL(b.BILL_AMT,0) - NVL(b.DISC_AMT,0) + NVL(b.VAT_AMT,0) + NVL(b.OTHR_AMT,0)) as net_amt,
             NVL(b.BILL_POST,0) as bill_post
      FROM IAS20261.IAS_BILL_MST b
      LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = b.C_CODE
      LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(b.REP_CODE)
      WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
        AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        AND b.BILL_DOC_TYPE IN (1,4,8)
        AND (:bill_type IS NULL OR TO_CHAR(b.BILL_DOC_TYPE) = :bill_type)
        AND (:rep_code IS NULL OR TO_CHAR(b.REP_CODE) = :rep_code)
        AND (:c_code IS NULL OR TO_CHAR(b.C_CODE) = :c_code OR c.C_A_NAME LIKE '%' || :c_code || '%')
    ),
    return_invoices AS (
      SELECT CASE r.RT_BILL_DOC_TYPE 
               WHEN 1 THEN 'مرتجع مبيعات نقدي' 
               WHEN 4 THEN 'مرتجع مبيعات آجل' 
               ELSE 'مرتجع مبيعات' 
             END AS doc_type_name,
             r.RT_BILL_DOC_TYPE as doc_type,
             r.RT_BILL_NO as bill_no,
             r.RT_BILL_DATE as bill_date,
             TO_CHAR(r.C_CODE) as c_code,
             c.C_A_NAME as c_name,
             TO_CHAR(r.REP_CODE) as rep_code,
             sm.REPRS_A_NAME as rep_name,
             -NVL(r.BILL_AMT,0) as gross_amt,
             -NVL(r.DISC_AMT_MST,0) as disc_amt,
             -NVL(r.VAT_AMT,0) as vat_amt,
             -(NVL(r.BILL_AMT,0) - NVL(r.DISC_AMT_MST,0) + NVL(r.VAT_AMT,0)) as net_amt,
             NVL(r.RT_BILL_POST,0) as bill_post
      FROM IAS20261.IAS_RT_BILL_MST r
      LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = r.C_CODE
      LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(r.REP_CODE)
      WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
        AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        AND r.RT_BILL_DOC_TYPE IN (1,4,8)
        AND (:bill_type IS NULL OR TO_CHAR(r.RT_BILL_DOC_TYPE) = :bill_type OR (:bill_type = '2' AND r.RT_BILL_DOC_TYPE = 1) OR (:bill_type = '5' AND r.RT_BILL_DOC_TYPE = 4))
        AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code)
        AND (:c_code IS NULL OR TO_CHAR(r.C_CODE) = :c_code OR c.C_A_NAME LIKE '%' || :c_code || '%')
    ),
    all_bills AS (
      SELECT * FROM sales_invoices
      UNION ALL
      SELECT * FROM return_invoices
    )
    SELECT doc_type_name AS "نوع المستند",
           bill_no AS "رقم الفاتورة",
           TO_CHAR(bill_date,'YYYY-MM-DD') AS "التاريخ",
           NVL(c_code, 'مباشر') AS "كود العميل",
           NVL(c_name, 'عميل نقدي') AS "اسم العميل",
           NVL(rep_name, rep_code) AS "المندوب",
           TO_CHAR(gross_amt,'FM999,999,990.00') AS "المبلغ قبل الخصم",
           TO_CHAR(disc_amt,'FM999,990.00') AS "الخصم",
           TO_CHAR(vat_amt,'FM999,999,990.00') AS "الضريبة",
           TO_CHAR(net_amt,'FM999,999,990.00') AS "الصافي شامل الضريبة",
           CASE bill_post WHEN 1 THEN 'مرحّلة' ELSE 'غير مرحّلة' END AS "الحالة"
    FROM all_bills
    ORDER BY bill_date DESC, bill_no DESC"""

def get_by_item_sql():
    return """
    WITH dtl_disc_sum AS (
        SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
        FROM IAS20261.IAS_BILL_DTL
        GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
    ),
    rt_dtl_disc_sum AS (
        SELECT RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
        FROM IAS20261.IAS_RT_BILL_DTL
        GROUP BY RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER
    ),
    item_sales AS (
        SELECT dt.I_CODE as item_code,
               NVL(dt.I_QTY,0) as sale_qty,
               0 as return_qty,
               (NVL(dt.I_QTY,0) * NVL(dt.I_PRICE,0)) as gross_amt,
               NVL(dt.DIS_AMT,0) as item_disc,
               CASE WHEN NVL(b.BILL_AMT,0) > 0 THEN
                   ((NVL(dt.I_QTY,0) * NVL(dt.I_PRICE,0)) / b.BILL_AMT) * GREATEST(0, NVL(b.DISC_AMT,0) - NVL(dds.tot_dtl_disc,0))
               ELSE 0 END as extra_header_disc
        FROM IAS20261.IAS_BILL_DTL dt
        JOIN IAS20261.IAS_BILL_MST b 
          ON b.BILL_DOC_TYPE = dt.BILL_DOC_TYPE AND b.BILL_NO = dt.BILL_NO AND b.BILL_SER = dt.BILL_SER
        LEFT JOIN dtl_disc_sum dds 
          ON dds.BILL_DOC_TYPE = dt.BILL_DOC_TYPE AND dds.BILL_NO = dt.BILL_NO AND dds.BILL_SER = dt.BILL_SER
        LEFT JOIN IAS20261.IAS_ITM_MST m ON TO_CHAR(m.I_CODE) = TO_CHAR(dt.I_CODE)
        WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND b.BILL_DOC_TYPE IN (1,4,8)
          AND (:i_code IS NULL OR TO_CHAR(dt.I_CODE) = :i_code OR m.I_NAME LIKE '%' || :i_code || '%')
          AND (:rep_code IS NULL OR TO_CHAR(b.REP_CODE) = :rep_code)
    ),
    item_returns AS (
        SELECT rdt.I_CODE as item_code,
               0 as sale_qty,
               NVL(rdt.I_QTY,0) as return_qty,
               -(NVL(rdt.I_QTY,0) * NVL(rdt.I_PRICE,0)) as gross_amt,
               -NVL(rdt.DIS_AMT,0) as item_disc,
               -CASE WHEN NVL(r.BILL_AMT,0) > 0 THEN
                   ((NVL(rdt.I_QTY,0) * NVL(rdt.I_PRICE,0)) / r.BILL_AMT) * GREATEST(0, NVL(r.DISC_AMT_MST,0) - NVL(rdds.tot_dtl_disc,0))
               ELSE 0 END as extra_header_disc
        FROM IAS20261.IAS_RT_BILL_DTL rdt
        JOIN IAS20261.IAS_RT_BILL_MST r 
          ON r.RT_BILL_DOC_TYPE = rdt.RT_BILL_DOC_TYPE AND r.RT_BILL_NO = rdt.RT_BILL_NO AND r.RT_BILL_SER = rdt.RT_BILL_SER
        LEFT JOIN rt_dtl_disc_sum rdds 
          ON rdds.RT_BILL_DOC_TYPE = rdt.RT_BILL_DOC_TYPE AND rdds.RT_BILL_NO = rdt.RT_BILL_NO AND rdds.RT_BILL_SER = rdt.RT_BILL_SER
        LEFT JOIN IAS20261.IAS_ITM_MST m ON TO_CHAR(m.I_CODE) = TO_CHAR(rdt.I_CODE)
        WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND r.RT_BILL_DOC_TYPE IN (1,4,8)
          AND (:i_code IS NULL OR TO_CHAR(rdt.I_CODE) = :i_code OR m.I_NAME LIKE '%' || :i_code || '%')
          AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code)
    ),
    all_item_trans AS (
        SELECT * FROM item_sales
        UNION ALL
        SELECT * FROM item_returns
    )
    SELECT t.item_code AS "كود الصنف",
           MAX(m.I_NAME) AS "اسم الصنف",
           TO_CHAR(SUM(t.sale_qty),'FM999,999,990.00') AS "كمية المبيعات",
           TO_CHAR(SUM(t.return_qty),'FM999,999,990.00') AS "كمية المردودات (-)",
           TO_CHAR(SUM(t.sale_qty - t.return_qty),'FM999,999,990.00') AS "صافي الكمية المباعة",
           TO_CHAR(SUM(t.gross_amt),'FM999,999,990.00') AS "إجمالي قيمة المبيعات",
           TO_CHAR(SUM(t.item_disc + t.extra_header_disc),'FM999,999,990.00') AS "إجمالي الخصومات (-)",
           TO_CHAR(SUM(t.gross_amt - t.item_disc - t.extra_header_disc),'FM999,999,990.00') AS "الصافي بدون الضريبة"
    FROM all_item_trans t
    LEFT JOIN IAS20261.IAS_ITM_MST m ON TO_CHAR(m.I_CODE) = TO_CHAR(t.item_code)
    GROUP BY t.item_code
    ORDER BY SUM(t.gross_amt - t.item_disc - t.extra_header_disc) DESC"""

def get_by_customer_sql():
    return """
    WITH sales_mst AS (
        SELECT TO_CHAR(b.C_CODE) as c_code,
               TO_CHAR(b.REP_CODE) as rep_code,
               1 as is_sale,
               0 as is_ret,
               NVL(b.BILL_AMT,0) as gross_amt,
               NVL(b.DISC_AMT,0) as disc_amt,
               0 as ext_disc,
               NVL(b.VAT_AMT,0) as vat_amt,
               NVL(b.OTHR_AMT,0) as othr_amt
        FROM IAS20261.IAS_BILL_MST b
        LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = b.C_CODE
        WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND b.BILL_DOC_TYPE IN (1,4,8)
          AND b.C_CODE IS NOT NULL
          AND (:c_code IS NULL OR TO_CHAR(b.C_CODE) = :c_code OR c.C_A_NAME LIKE '%' || :c_code || '%')
          AND (:rep_code IS NULL OR TO_CHAR(b.REP_CODE) = :rep_code)
    ),
    returns_mst AS (
        SELECT TO_CHAR(r.C_CODE) as c_code,
               TO_CHAR(r.REP_CODE) as rep_code,
               0 as is_sale,
               1 as is_ret,
               NVL(r.BILL_AMT,0) as gross_amt,
               NVL(r.DISC_AMT_MST,0) as disc_amt,
               0 as ext_disc,
               NVL(r.VAT_AMT,0) as vat_amt,
               0 as othr_amt
        FROM IAS20261.IAS_RT_BILL_MST r
        LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = r.C_CODE
        WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND r.RT_BILL_DOC_TYPE IN (1,4,8)
          AND r.C_CODE IS NOT NULL
          AND (:c_code IS NULL OR TO_CHAR(r.C_CODE) = :c_code OR c.C_A_NAME LIKE '%' || :c_code || '%')
          AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code)
    ),
    ext_disc_notes AS (
        SELECT TO_CHAR(p.C_CODE) as c_code,
               TO_CHAR(p.REP_CODE) as rep_code,
               0 as is_sale,
               0 as is_ret,
               0 as gross_amt,
               0 as disc_amt,
               NVL(p.CR_AMT,0) as ext_disc,
               0 as vat_amt,
               0 as othr_amt
        FROM IAS20261.IAS_POST_DTL p
        LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
        WHERE p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND p.DOC_TYPE = 15 AND NVL(p.CR_AMT,0) > 0 AND NVL(p.DOC_POST,0) = 1
          AND p.C_CODE IS NOT NULL
          AND (:c_code IS NULL OR TO_CHAR(p.C_CODE) = :c_code OR c.C_A_NAME LIKE '%' || :c_code || '%')
          AND (:rep_code IS NULL OR TO_CHAR(p.REP_CODE) = :rep_code)
    ),
    all_cust_trans AS (
        SELECT * FROM sales_mst
        UNION ALL
        SELECT * FROM returns_mst
        UNION ALL
        SELECT * FROM ext_disc_notes
    )
    SELECT t.c_code AS "كود العميل",
           MAX(c.C_A_NAME) AS "اسم العميل",
           MAX(sm.REPRS_A_NAME) AS "المندوب",
           SUM(t.is_sale) AS "فواتير مبيعات",
           SUM(t.is_ret) AS "فواتير مرتجعات",
           TO_CHAR(SUM(t.gross_amt * t.is_sale),'FM999,999,999,990.00') AS "المبيعات",
           TO_CHAR(SUM(t.gross_amt * t.is_ret),'FM999,999,999,990.00') AS "المردودات (-)",
           TO_CHAR(SUM(t.disc_amt * t.is_sale - t.disc_amt * t.is_ret),'FM999,999,999,990.00') AS "خصم الفواتير والأصناف (-)",
           TO_CHAR(SUM(t.ext_disc),'FM999,999,999,990.00') AS "إشعار خصم مستقل (-)",
           TO_CHAR(SUM((t.gross_amt - t.disc_amt) * t.is_sale - (t.gross_amt - t.disc_amt) * t.is_ret - t.ext_disc),'FM999,999,999,990.00') AS "الصافي قبل الضريبة",
           TO_CHAR(SUM((t.gross_amt - t.disc_amt + t.vat_amt + t.othr_amt) * t.is_sale - (t.gross_amt - t.disc_amt + t.vat_amt) * t.is_ret - t.ext_disc),'FM999,999,999,990.00') AS "الإجمالي بالضريبة"
    FROM all_cust_trans t
    LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = TO_CHAR(t.c_code)
    LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(t.rep_code)
    GROUP BY t.c_code
    ORDER BY SUM((t.gross_amt - t.disc_amt) * t.is_sale - (t.gross_amt - t.disc_amt) * t.is_ret - t.ext_disc) DESC"""

def get_by_salesman_sql():
    return """
    WITH sales_mst AS (
        SELECT TO_CHAR(b.REP_CODE) as rep_code,
               TO_CHAR(b.C_CODE) as c_code,
               1 as is_sale,
               0 as is_ret,
               NVL(b.BILL_AMT,0) as gross_amt,
               NVL(b.DISC_AMT,0) as disc_amt,
               0 as ext_disc,
               NVL(b.VAT_AMT,0) as vat_amt,
               NVL(b.OTHR_AMT,0) as othr_amt
        FROM IAS20261.IAS_BILL_MST b
        LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(b.REP_CODE)
        WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND b.BILL_DOC_TYPE IN (1,4,8)
          AND b.REP_CODE IS NOT NULL
          AND (:rep_code IS NULL OR TO_CHAR(b.REP_CODE) = :rep_code OR sm.REPRS_A_NAME LIKE '%' || :rep_code || '%')
    ),
    returns_mst AS (
        SELECT TO_CHAR(r.REP_CODE) as rep_code,
               TO_CHAR(r.C_CODE) as c_code,
               0 as is_sale,
               1 as is_ret,
               NVL(r.BILL_AMT,0) as gross_amt,
               NVL(r.DISC_AMT_MST,0) as disc_amt,
               0 as ext_disc,
               NVL(r.VAT_AMT,0) as vat_amt,
               0 as othr_amt
        FROM IAS20261.IAS_RT_BILL_MST r
        LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(r.REP_CODE)
        WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND r.RT_BILL_DOC_TYPE IN (1,4,8)
          AND r.REP_CODE IS NOT NULL
          AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code OR sm.REPRS_A_NAME LIKE '%' || :rep_code || '%')
    ),
    ext_disc_notes AS (
        SELECT TO_CHAR(p.REP_CODE) as rep_code,
               TO_CHAR(p.C_CODE) as c_code,
               0 as is_sale,
               0 as is_ret,
               0 as gross_amt,
               0 as disc_amt,
               NVL(p.CR_AMT,0) as ext_disc,
               0 as vat_amt,
               0 as othr_amt
        FROM IAS20261.IAS_POST_DTL p
        LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(p.REP_CODE)
        WHERE p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND p.DOC_TYPE = 15 AND NVL(p.CR_AMT,0) > 0 AND NVL(p.DOC_POST,0) = 1
          AND p.REP_CODE IS NOT NULL
          AND (:rep_code IS NULL OR TO_CHAR(p.REP_CODE) = :rep_code OR sm.REPRS_A_NAME LIKE '%' || :rep_code || '%')
    ),
    all_rep_trans AS (
        SELECT * FROM sales_mst
        UNION ALL
        SELECT * FROM returns_mst
        UNION ALL
        SELECT * FROM ext_disc_notes
    )
    SELECT t.rep_code AS "كود المندوب",
           MAX(sm.REPRS_A_NAME) AS "اسم المندوب",
           COUNT(DISTINCT t.c_code) AS "عدد العملاء",
           SUM(t.is_sale) AS "فواتير مبيعات",
           SUM(t.is_ret) AS "فواتير مرتجعات",
           TO_CHAR(SUM(t.gross_amt * t.is_sale),'FM999,999,999,990.00') AS "المبيعات",
           TO_CHAR(SUM(t.gross_amt * t.is_ret),'FM999,999,999,990.00') AS "المردودات (-)",
           TO_CHAR(SUM(t.disc_amt * t.is_sale - t.disc_amt * t.is_ret),'FM999,999,999,990.00') AS "خصم الفواتير والأصناف (-)",
           TO_CHAR(SUM(t.ext_disc),'FM999,999,999,990.00') AS "إشعار خصم مستقل (-)",
           TO_CHAR(SUM((t.gross_amt - t.disc_amt) * t.is_sale - (t.gross_amt - t.disc_amt) * t.is_ret - t.ext_disc),'FM999,999,999,990.00') AS "الصافي قبل الضريبة",
           TO_CHAR(SUM((t.gross_amt - t.disc_amt + t.vat_amt + t.othr_amt) * t.is_sale - (t.gross_amt - t.disc_amt + t.vat_amt) * t.is_ret - t.ext_disc),'FM999,999,999,990.00') AS "الإجمالي بالضريبة"
    FROM all_rep_trans t
    LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(t.rep_code)
    GROUP BY t.rep_code
    ORDER BY SUM((t.gross_amt - t.disc_amt) * t.is_sale - (t.gross_amt - t.disc_amt) * t.is_ret - t.ext_disc) DESC"""

def get_net_sales_cc_sql():
    return """
       WITH sales_data AS (
           SELECT CC_CODE,
                  SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as sales
           FROM IAS20261.IAS_BILL_MST
           WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
             AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
             AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
           GROUP BY CC_CODE
       ),
       returns_data AS (
           SELECT CC_CODE,
                  SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as returns
           FROM IAS20261.IAS_RT_BILL_MST
           WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
             AND RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
             AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
           GROUP BY CC_CODE
       ),
       discount_notice AS (
           SELECT CC_CODE, ROUND(SUM(NVL(CR_AMT,0)) / 1.15, 2) as ext_disc
           FROM IAS20261.IAS_POST_DTL
           WHERE DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
             AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
             AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
           GROUP BY CC_CODE
       )
       SELECT NVL(NVL(s.CC_CODE, r.CC_CODE), d.CC_CODE) AS "رقم مركز التكلفة",
              MAX(cc.CC_A_NAME) AS "اسم مركز التكلفة",
              TO_CHAR(SUM(NVL(s.sales, 0)),'FM999,999,999,990.00') AS "إجمالي المبيعات",
              TO_CHAR(SUM(NVL(r.returns, 0)),'FM999,999,999,990.00') AS "مردود المبيعات (-)",
              TO_CHAR(CASE WHEN :inc_ext = '1' THEN SUM(NVL(d.ext_disc, 0)) ELSE 0 END,'FM999,999,999,990.00') AS "إشعار خصم مستقل (-)",
              TO_CHAR(
                SUM(NVL(s.sales, 0)) - SUM(NVL(r.returns, 0)) - (CASE WHEN :inc_ext = '1' THEN SUM(NVL(d.ext_disc, 0)) ELSE 0 END),
                'FM999,999,999,990.00'
              ) AS "صافي المبيعات"
       FROM sales_data s
       FULL OUTER JOIN returns_data r ON s.CC_CODE = r.CC_CODE
       FULL OUTER JOIN discount_notice d ON NVL(s.CC_CODE, r.CC_CODE) = d.CC_CODE
       LEFT JOIN IAS20261.COST_CENTERS cc ON cc.CC_CODE = NVL(NVL(s.CC_CODE, r.CC_CODE), d.CC_CODE)
       WHERE (:cc_code IS NULL OR NVL(NVL(s.CC_CODE, r.CC_CODE), d.CC_CODE) = :cc_code)
       GROUP BY NVL(NVL(s.CC_CODE, r.CC_CODE), d.CC_CODE)
       HAVING (SUM(NVL(s.sales, 0)) <> 0 OR SUM(NVL(r.returns, 0)) <> 0 OR SUM(NVL(d.ext_disc, 0)) <> 0)
       ORDER BY SUM(NVL(s.sales, 0)) - SUM(NVL(r.returns, 0)) - (CASE WHEN :inc_ext = '1' THEN SUM(NVL(d.ext_disc, 0)) ELSE 0 END) DESC
    """

