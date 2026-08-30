# -*- coding: utf-8 -*-
from database import get_conn

# SQL functions for SUMMARY reports
def get_critical_debts_sql():
    return """
      WITH customer_balances AS (
          SELECT C_CODE, SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)) as balance
          FROM IAS_POST_DTL
          WHERE NVL(DOC_POST,0) = 1 AND C_CODE IS NOT NULL
          GROUP BY C_CODE
          HAVING SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)) > 1000
      ),
      last_activity AS (
          SELECT C_CODE,
                 MAX(CASE WHEN NVL(CR_AMT,0) > 0 THEN DOC_DATE END) as last_payment_date,
                 MAX(CASE WHEN NVL(DR_AMT,0) > 0 AND DOC_TYPE = 4 THEN DOC_DATE END) as last_invoice_date
          FROM IAS_POST_DTL
          WHERE NVL(DOC_POST,0) = 1 AND C_CODE IS NOT NULL
          GROUP BY C_CODE
      )
      SELECT c.C_CODE AS "كود العميل",
             MAX(cust.C_A_NAME) AS "اسم العميل",
             MAX(sm.REPRS_A_NAME) AS "المندوب",
             TO_CHAR(c.balance, 'FM999,999,990.00') AS "المديونية الحالية",
             TO_CHAR(la.last_payment_date, 'YYYY-MM-DD') AS "تاريخ آخر سداد",
             TRUNC(SYSDATE) - TRUNC(la.last_payment_date) AS "أيام التوقف عن السداد",
             TO_CHAR(la.last_invoice_date, 'YYYY-MM-DD') AS "تاريخ آخر سحب",
             TRUNC(SYSDATE) - TRUNC(la.last_invoice_date) AS "أيام التوقف عن السحب"
      FROM customer_balances c
      JOIN last_activity la ON c.C_CODE = la.C_CODE
      JOIN CUSTOMER cust ON c.C_CODE = cust.C_CODE
      LEFT JOIN SALES_MAN sm ON TO_CHAR(cust.REP_CODE) = TO_CHAR(sm.REPRS_CODE)
      WHERE (TRUNC(SYSDATE) - TRUNC(la.last_payment_date) >= :days_threshold OR la.last_payment_date IS NULL)
        AND (TRUNC(SYSDATE) - TRUNC(la.last_invoice_date) >= :days_threshold OR la.last_invoice_date IS NULL)
      GROUP BY c.C_CODE, c.balance, la.last_payment_date, la.last_invoice_date
      ORDER BY c.balance DESC
    """

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

def get_true_income_statement_sql():
    return """
        WITH gl_base AS (
          SELECT 
              A_CODE as acc_code,
              SUM(CASE WHEN DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(DR_AMT,0) ELSE 0 END) as op_dr,
              SUM(CASE WHEN DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(CR_AMT,0) ELSE 0 END) as op_cr,
              SUM(CASE WHEN DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(DR_AMT,0) ELSE 0 END) as mv_dr,
              SUM(CASE WHEN DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(CR_AMT,0) ELSE 0 END) as mv_cr
          FROM IAS_POST_DTL
          WHERE (:cc_code IS NULL OR CC_CODE = :cc_code)
            AND (
                A_CODE LIKE '31102%' OR A_CODE LIKE '31104%' OR A_CODE LIKE '31105%' OR A_CODE LIKE '31109%' OR A_CODE LIKE '31110%' OR
                A_CODE LIKE '32101%' OR A_CODE LIKE '32201%' OR A_CODE LIKE '32401%' OR A_CODE LIKE '32801%' OR
                A_CODE LIKE '41101%' OR A_CODE LIKE '41202%'
            )
          GROUP BY A_CODE
        ),
        inv_cogs AS (
          SELECT 
              '311010001' as acc_code,
              SUM(CASE WHEN m.BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(d.I_QTY,0) * NVL(d.I_PRICE_LEV_NO,0) ELSE 0 END) as op_dr,
              0 as op_cr,
              SUM(CASE WHEN m.BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(d.I_QTY,0) * NVL(d.I_PRICE_LEV_NO,0) ELSE 0 END) as mv_dr,
              0 as mv_cr
          FROM IAS_BILL_MST m
          JOIN IAS_BILL_DTL d ON m.BILL_DOC_TYPE = d.BILL_DOC_TYPE AND m.BILL_NO = d.BILL_NO AND m.BILL_SER = d.BILL_SER
          WHERE (:cc_code IS NULL OR m.CC_CODE = :cc_code)
        ),
        inv_cogs_ret AS (
          SELECT 
              '311030001' as acc_code,
              0 as op_dr,
              SUM(CASE WHEN r.RT_BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(d.I_QTY,0) * NVL(d.I_PRICE_LEV_NO,0) ELSE 0 END) as op_cr,
              0 as mv_dr,
              SUM(CASE WHEN r.RT_BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(d.I_QTY,0) * NVL(d.I_PRICE_LEV_NO,0) ELSE 0 END) as mv_cr
          FROM IAS_RT_BILL_MST r
          JOIN IAS_RT_BILL_DTL d ON r.RT_BILL_DOC_TYPE = d.RT_BILL_DOC_TYPE AND r.RT_BILL_NO = d.RT_BILL_NO AND r.RT_BILL_SER = d.RT_BILL_SER
          WHERE (:cc_code IS NULL OR r.CC_CODE = :cc_code)
            AND r.PREV_YEAR IS NULL
        ),
        inv_cogs_ret_prev AS (
          SELECT 
              '311060001' as acc_code,
              0 as op_dr,
              SUM(CASE WHEN r.RT_BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(d.I_QTY,0) * NVL(d.I_PRICE_LEV_NO,0) ELSE 0 END) as op_cr,
              0 as mv_dr,
              SUM(CASE WHEN r.RT_BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(d.I_QTY,0) * NVL(d.I_PRICE_LEV_NO,0) ELSE 0 END) as mv_cr
          FROM IAS_RT_BILL_MST r
          JOIN IAS_RT_BILL_DTL d ON r.RT_BILL_DOC_TYPE = d.RT_BILL_DOC_TYPE AND r.RT_BILL_NO = d.RT_BILL_NO AND r.RT_BILL_SER = d.RT_BILL_SER
          WHERE (:cc_code IS NULL OR r.CC_CODE = :cc_code)
            AND r.PREV_YEAR IS NOT NULL
        ),
        all_data AS (
          SELECT * FROM gl_base
          UNION ALL
          SELECT * FROM inv_cogs
          UNION ALL
          SELECT * FROM inv_cogs_ret
          UNION ALL
          SELECT * FROM inv_cogs_ret_prev
        )
        SELECT 
            d.acc_code AS "الرقم", 
            MAX(a.A_NAME) AS "الاسم",
            TO_CHAR(NULLIF(ROUND(NVL(SUM(d.op_dr),0),2), 0),'FM999,999,990.00') AS "الرصيد الافتتاحي مدين",
            TO_CHAR(NULLIF(ROUND(NVL(SUM(d.op_cr),0),2), 0),'FM999,999,990.00') AS "الرصيد الافتتاحي دائن",
            TO_CHAR(NULLIF(ROUND(NVL(SUM(d.mv_dr),0),2), 0),'FM999,999,990.00') AS "رصيد الحركة مدين",
            TO_CHAR(NULLIF(ROUND(NVL(SUM(d.mv_cr),0),2), 0),'FM999,999,990.00') AS "رصيد الحركة دائن",
            TO_CHAR(NULLIF(ROUND(
              CASE WHEN (NVL(SUM(d.op_dr),0) + NVL(SUM(d.mv_dr),0)) - (NVL(SUM(d.op_cr),0) + NVL(SUM(d.mv_cr),0)) > 0 
                   THEN (NVL(SUM(d.op_dr),0) + NVL(SUM(d.mv_dr),0)) - (NVL(SUM(d.op_cr),0) + NVL(SUM(d.mv_cr),0))
                   ELSE 0 END, 2), 0), 'FM999,999,990.00'
            ) AS "الأرصدة مدين",
            TO_CHAR(NULLIF(ROUND(
              CASE WHEN (NVL(SUM(d.op_cr),0) + NVL(SUM(d.mv_cr),0)) - (NVL(SUM(d.op_dr),0) + NVL(SUM(d.mv_dr),0)) > 0 
                   THEN (NVL(SUM(d.op_cr),0) + NVL(SUM(d.mv_cr),0)) - (NVL(SUM(d.op_dr),0) + NVL(SUM(d.mv_dr),0))
                   ELSE 0 END, 2), 0), 'FM999,999,990.00'
            ) AS "الأرصدة دائن"
        FROM all_data d
        LEFT JOIN ACCOUNT a ON a.A_CODE = d.acc_code
        GROUP BY d.acc_code
        ORDER BY d.acc_code
      """

def get_collection_adopted_sql():
    return """

      WITH 
      grp AS (
        SELECT 'rep' as typ, TO_CHAR(REPRS_CODE) as cd, MAX(REPRS_A_NAME) as nm FROM SALES_MAN GROUP BY TO_CHAR(REPRS_CODE)
        UNION ALL 
        SELECT 'cc' as typ, TO_CHAR(CC_CODE) as cd, MAX(CC_A_NAME) as nm FROM COST_CENTERS GROUP BY TO_CHAR(CC_CODE)
        UNION ALL
        SELECT 'cst' as typ, TO_CHAR(C_CODE) as cd, MAX(C_A_NAME) as nm FROM CUSTOMER GROUP BY TO_CHAR(C_CODE)
        UNION ALL
        SELECT 'cst' as typ, 'UNKNOWN' as cd, 'عميل نقدي عام' as nm FROM DUAL
      ),
      all_trans AS (
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END as grp_code,
               CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as inv_disc, 0 as cash_ret, 0 as ext_notice, 0 as rcpt_unknown, 0 as unposted_rcpt, 0 as unposted_unknown
        FROM IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, 0, 0, CR_AMT, 0
        FROM IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, 0, 0, 0, CR_AMT
        FROM IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, CR_AMT, 0, 0, 0, 0, 0, 0, 0
        FROM IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(b.CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(b.C_CODE),'UNKNOWN') ELSE TO_CHAR(b.REP_CODE) END,
               0, 0, NVL(p.DR_AMT,0), NVL(b.DISC_AMT,0), 0, 0, 0, 0, 0
        FROM IAS_BILL_MST b
        JOIN IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
        WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
          AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, CR_AMT, 0, 0, 0, 0
        FROM IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, CR_AMT, 0, 0, 0
        FROM IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=15 AND NVL(CR_AMT,0)>0
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, 0, CR_AMT, 0, 0
        FROM IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      ),
      base AS (
        SELECT grp_code,
               SUM(rcpt) rcpt, SUM(net_jrn) net_jrn, SUM(cash_sales) cash_sales, SUM(inv_disc) inv_disc, SUM(cash_ret) cash_ret, SUM(ext_notice) ext_notice, SUM(rcpt_unknown) rcpt_unknown, SUM(unposted_rcpt) unposted_rcpt, SUM(unposted_unknown) unposted_unknown,
               (CASE WHEN :inc_rcpt='1' THEN (SUM(rcpt) + SUM(unposted_rcpt) + SUM(unposted_unknown)) ELSE 0 END
              + CASE WHEN :inc_net='1'  THEN SUM(net_jrn) ELSE 0 END
              + CASE WHEN :inc_cash='1' THEN SUM(cash_sales) ELSE 0 END
              - CASE WHEN :inc_ret='1'  THEN SUM(cash_ret) ELSE 0 END
              ) total_inc
        FROM all_trans
        WHERE grp_code IS NOT NULL
          AND (:rep_code IS NULL OR (:grp_by = 'rep' AND grp_code = :rep_code))
        GROUP BY grp_code
      )
      SELECT * FROM (
        SELECT b.grp_code AS "الكود", NVL(MAX(g.nm), b.grp_code) AS "الجهة / الاسم",
               TO_CHAR(MAX(b.rcpt),'FM999,999,990.00')      AS "سندات القبض",
               TO_CHAR(MAX(b.unposted_rcpt),'FM999,999,990.00') AS "سندات غير مرحلة",
               TO_CHAR(MAX(b.unposted_unknown),'FM999,999,990.00') AS "غير مرحلة (بدون عميل)",
               TO_CHAR(MAX(b.rcpt_unknown),'FM999,999,990.00') AS "إيداعات وتسويات (بدون عميل)",
               TO_CHAR(MAX(b.net_jrn),'FM999,999,990.00')   AS "قيود الشبكة المنفصلة",
               TO_CHAR(MAX(b.cash_sales),'FM999,999,990.00') AS "المبيعات النقدية",
               TO_CHAR(MAX(b.inv_disc),'FM999,999,990.00')   AS "الخصم في الفاتورة",
               TO_CHAR(MAX(b.ext_notice),'FM999,999,990.00') AS "إشعار خصم مستقل (-)",
               TO_CHAR(MAX(b.cash_ret),'FM999,999,990.00')   AS "المرتجع النقدي (-)",
               TO_CHAR(MAX(b.total_inc),'FM999,999,990.00') AS "إجمالي التحصيل"
        FROM base b
        LEFT JOIN grp g ON g.cd = b.grp_code AND g.typ = :grp_by
        WHERE (b.rcpt > 0 OR b.net_jrn > 0 OR b.cash_sales > 0 OR b.cash_ret > 0 OR b.inv_disc > 0 OR b.ext_notice > 0 OR b.rcpt_unknown > 0 OR b.unposted_rcpt > 0 OR b.unposted_unknown > 0)
        GROUP BY b.grp_code
        ORDER BY MAX(b.total_inc) DESC
      ) 
"""

