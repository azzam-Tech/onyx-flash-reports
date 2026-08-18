# -*- coding: utf-8 -*-
from database import get_conn

# SQL functions for PROF reports
def get_prof_summary_sql():
    return """
      WITH dtl_disc_sum AS (
          SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS_BILL_DTL GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
      ),
      rt_dtl_disc_sum AS (
          SELECT RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS_RT_BILL_DTL GROUP BY RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER
      ),
      sales_lines AS (
          SELECT NVL(d.I_QTY,0) as qty,
                 (NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) as gross_rev,
                 NVL(d.DIS_AMT,0) as line_disc,
                 CASE WHEN NVL(m.BILL_AMT,0) > 0 THEN
                     ((NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) / m.BILL_AMT) * GREATEST(0, NVL(m.DISC_AMT,0) - NVL(dds.tot_dtl_disc,0))
                 ELSE 0 END as extra_header_disc,
                 (NVL(d.I_QTY,0) * NVL(d.STK_COST,0)) as cost
          FROM IAS_BILL_DTL d
          JOIN IAS_BILL_MST m ON m.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND m.BILL_NO=d.BILL_NO AND m.BILL_SER=d.BILL_SER
          LEFT JOIN dtl_disc_sum dds ON dds.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND dds.BILL_NO=d.BILL_NO AND dds.BILL_SER=d.BILL_SER
          WHERE m.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND m.BILL_DOC_TYPE IN (1,4,8)
            AND (:rep_code IS NULL OR TO_CHAR(m.REP_CODE) = :rep_code)
      ),
      return_lines AS (
          SELECT -NVL(rd.I_QTY,0) as qty,
                 -(NVL(rd.I_QTY,0) * NVL(rd.I_PRICE,0)) as gross_rev,
                 -NVL(rd.DIS_AMT,0) as line_disc,
                 -CASE WHEN NVL(r.BILL_AMT,0) > 0 THEN
                     ((NVL(rd.I_QTY,0) * NVL(rd.I_PRICE,0)) / r.BILL_AMT) * GREATEST(0, NVL(r.DISC_AMT_MST,0) - NVL(rdds.tot_dtl_disc,0))
                 ELSE 0 END as extra_header_disc,
                 -(NVL(rd.I_QTY,0) * NVL(rd.STK_COST,0)) as cost
          FROM IAS_RT_BILL_DTL rd
          JOIN IAS_RT_BILL_MST r ON r.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND r.RT_BILL_NO=rd.RT_BILL_NO AND r.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN rt_dtl_disc_sum rdds ON rdds.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND rdds.RT_BILL_NO=rd.RT_BILL_NO AND rdds.RT_BILL_SER=rd.RT_BILL_SER
          WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND r.RT_BILL_DOC_TYPE IN (1,4,8)
            AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code)
      ),
      ext_disc_notes AS (
          SELECT SUM(NVL(CR_AMT,0)) as ext_disc
          FROM IAS_POST_DTL
          WHERE DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
            AND (:rep_code IS NULL OR TO_CHAR(REP_CODE) = :rep_code)
      ),
      all_lines AS (
          SELECT * FROM sales_lines
          UNION ALL
          SELECT * FROM return_lines
      ),
      totals AS (
          SELECT SUM(gross_rev - line_disc - extra_header_disc) as net_bill_rev,
                 SUM(cost) as total_cogs
          FROM all_lines
      )
      SELECT TO_CHAR(t.net_bill_rev - NVL(e.ext_disc,0),'FM999,999,999,990.00') AS "المبيعات (بلا ضريبة)",
             TO_CHAR(t.total_cogs,'FM999,999,999,990.00') AS "تكلفة المبيعات",
             TO_CHAR((t.net_bill_rev - NVL(e.ext_disc,0)) - t.total_cogs,'FM999,999,999,990.00') AS "مجمل الربح",
             TO_CHAR(ROUND(100 * ((t.net_bill_rev - NVL(e.ext_disc,0)) - t.total_cogs) / NULLIF(t.net_bill_rev - NVL(e.ext_disc,0), 0), 1), 'FM990.0') || ' %' AS "الهامش"
      FROM totals t
      CROSS JOIN ext_disc_notes e"""

def get_net_profit_sql():
    return """
      SELECT
        TO_CHAR(SUM(CASE WHEN nt>0 THEN nt ELSE 0 END),'FM999,999,999,990.00') AS "الإيرادات",
        TO_CHAR(SUM(CASE WHEN nt<0 THEN -nt ELSE 0 END),'FM999,999,999,990.00') AS "المصاريف",
        TO_CHAR(SUM(nt),'FM999,999,999,990.00') AS "صافي الربح"
      FROM (SELECT p.A_CODE, SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)) nt
            FROM IAS_POST_DTL p JOIN ACCOUNT a ON a.A_CODE=p.A_CODE
            WHERE NVL(p.DOC_POST,0)=1 AND a.A_REPORT=2
              AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            GROUP BY p.A_CODE)"""

def get_prof_item_sql():
    return """
      WITH dtl_disc_sum AS (
          SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS_BILL_DTL GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
      ),
      rt_dtl_disc_sum AS (
          SELECT RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS_RT_BILL_DTL GROUP BY RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER
      ),
      sales_lines AS (
          SELECT d.I_CODE as item_code,
                 NVL(d.I_QTY,0) as qty,
                 (NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) as gross_rev,
                 NVL(d.DIS_AMT,0) as line_disc,
                 CASE WHEN NVL(m.BILL_AMT,0) > 0 THEN
                     ((NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) / m.BILL_AMT) * GREATEST(0, NVL(m.DISC_AMT,0) - NVL(dds.tot_dtl_disc,0))
                 ELSE 0 END as extra_header_disc,
                 (NVL(d.I_QTY,0) * NVL(d.STK_COST,0)) as cost
          FROM IAS_BILL_DTL d
          JOIN IAS_BILL_MST m ON m.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND m.BILL_NO=d.BILL_NO AND m.BILL_SER=d.BILL_SER
          LEFT JOIN dtl_disc_sum dds ON dds.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND dds.BILL_NO=d.BILL_NO AND dds.BILL_SER=d.BILL_SER
          LEFT JOIN IAS_ITM_MST im ON TO_CHAR(im.I_CODE) = TO_CHAR(d.I_CODE)
          WHERE m.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND m.BILL_DOC_TYPE IN (1,4,8)
            AND (:i_code IS NULL OR TO_CHAR(d.I_CODE) = :i_code OR im.I_NAME LIKE '%' || :i_code || '%')
            AND (:rep_code IS NULL OR TO_CHAR(m.REP_CODE) = :rep_code)
      ),
      return_lines AS (
          SELECT rd.I_CODE as item_code,
                 -NVL(rd.I_QTY,0) as qty,
                 -(NVL(rd.I_QTY,0) * NVL(rd.I_PRICE,0)) as gross_rev,
                 -NVL(rd.DIS_AMT,0) as line_disc,
                 -CASE WHEN NVL(r.BILL_AMT,0) > 0 THEN
                     ((NVL(rd.I_QTY,0) * NVL(rd.I_PRICE,0)) / r.BILL_AMT) * GREATEST(0, NVL(r.DISC_AMT_MST,0) - NVL(rdds.tot_dtl_disc,0))
                 ELSE 0 END as extra_header_disc,
                 -(NVL(rd.I_QTY,0) * NVL(rd.STK_COST,0)) as cost
          FROM IAS_RT_BILL_DTL rd
          JOIN IAS_RT_BILL_MST r ON r.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND r.RT_BILL_NO=rd.RT_BILL_NO AND r.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN rt_dtl_disc_sum rdds ON rdds.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND rdds.RT_BILL_NO=rd.RT_BILL_NO AND rdds.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN IAS_ITM_MST im ON TO_CHAR(im.I_CODE) = TO_CHAR(rd.I_CODE)
          WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND r.RT_BILL_DOC_TYPE IN (1,4,8)
            AND (:i_code IS NULL OR TO_CHAR(rd.I_CODE) = :i_code OR im.I_NAME LIKE '%' || :i_code || '%')
            AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code)
      ),
      all_lines AS (
          SELECT * FROM sales_lines
          UNION ALL
          SELECT * FROM return_lines
      )
      SELECT * FROM (
        SELECT t.item_code AS "كود الصنف",
               MAX(im.I_NAME) AS "اسم الصنف",
               TO_CHAR(SUM(t.qty),'FM999,999,990.00') AS "الكمية المباعة",
               TO_CHAR(SUM(t.gross_rev - t.line_disc - t.extra_header_disc),'FM999,999,999,990.00') AS "المبيعات",
               TO_CHAR(SUM(t.cost),'FM999,999,999,990.00') AS "التكلفة",
               TO_CHAR(SUM(t.gross_rev - t.line_disc - t.extra_header_disc) - SUM(t.cost),'FM999,999,999,990.00') AS "الربح",
               TO_CHAR(ROUND(100 * (SUM(t.gross_rev - t.line_disc - t.extra_header_disc) - SUM(t.cost)) / NULLIF(SUM(t.gross_rev - t.line_disc - t.extra_header_disc), 0), 1), 'FM990.0') || ' %' AS "هامش"
        FROM all_lines t
        LEFT JOIN IAS_ITM_MST im ON TO_CHAR(im.I_CODE) = TO_CHAR(t.item_code)
        GROUP BY t.item_code
        ORDER BY SUM(t.gross_rev - t.line_disc - t.extra_header_disc) - SUM(t.cost) DESC
      ) """

def get_prof_cust_sql():
    return """
      WITH dtl_disc_sum AS (
          SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS_BILL_DTL GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
      ),
      rt_dtl_disc_sum AS (
          SELECT RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS_RT_BILL_DTL GROUP BY RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER
      ),
      sales_lines AS (
          SELECT TO_CHAR(m.C_CODE) as c_code,
                 (NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) as gross_rev,
                 NVL(d.DIS_AMT,0) as line_disc,
                 CASE WHEN NVL(m.BILL_AMT,0) > 0 THEN
                     ((NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) / m.BILL_AMT) * GREATEST(0, NVL(m.DISC_AMT,0) - NVL(dds.tot_dtl_disc,0))
                 ELSE 0 END as extra_header_disc,
                 0 as ext_disc,
                 (NVL(d.I_QTY,0) * NVL(d.STK_COST,0)) as cost
          FROM IAS_BILL_DTL d
          JOIN IAS_BILL_MST m ON m.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND m.BILL_NO=d.BILL_NO AND m.BILL_SER=d.BILL_SER
          LEFT JOIN dtl_disc_sum dds ON dds.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND dds.BILL_NO=d.BILL_NO AND dds.BILL_SER=d.BILL_SER
          LEFT JOIN CUSTOMER c ON TO_CHAR(c.C_CODE) = TO_CHAR(m.C_CODE)
          WHERE m.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND m.BILL_DOC_TYPE IN (1,4,8)
            AND (:c_code IS NULL OR TO_CHAR(m.C_CODE) = :c_code OR c.C_A_NAME LIKE '%' || :c_code || '%')
            AND (:rep_code IS NULL OR TO_CHAR(m.REP_CODE) = :rep_code)
      ),
      return_lines AS (
          SELECT TO_CHAR(r.C_CODE) as c_code,
                 -(NVL(rd.I_QTY,0) * NVL(rd.I_PRICE,0)) as gross_rev,
                 -NVL(rd.DIS_AMT,0) as line_disc,
                 -CASE WHEN NVL(r.BILL_AMT,0) > 0 THEN
                     ((NVL(rd.I_QTY,0) * NVL(rd.I_PRICE,0)) / r.BILL_AMT) * GREATEST(0, NVL(r.DISC_AMT_MST,0) - NVL(rdds.tot_dtl_disc,0))
                 ELSE 0 END as extra_header_disc,
                 0 as ext_disc,
                 -(NVL(rd.I_QTY,0) * NVL(rd.STK_COST,0)) as cost
          FROM IAS_RT_BILL_DTL rd
          JOIN IAS_RT_BILL_MST r ON r.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND r.RT_BILL_NO=rd.RT_BILL_NO AND r.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN rt_dtl_disc_sum rdds ON rdds.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND rdds.RT_BILL_NO=rd.RT_BILL_NO AND rdds.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN CUSTOMER c ON TO_CHAR(c.C_CODE) = TO_CHAR(r.C_CODE)
          WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND r.RT_BILL_DOC_TYPE IN (1,4,8)
            AND (:c_code IS NULL OR TO_CHAR(r.C_CODE) = :c_code OR c.C_A_NAME LIKE '%' || :c_code || '%')
            AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code)
      ),
      ext_disc_notes AS (
          SELECT TO_CHAR(p.C_CODE) as c_code,
                 0 as gross_rev,
                 0 as line_disc,
                 0 as extra_header_disc,
                 NVL(p.CR_AMT,0) as ext_disc,
                 0 as cost
          FROM IAS_POST_DTL p
          LEFT JOIN CUSTOMER c ON TO_CHAR(c.C_CODE) = TO_CHAR(p.C_CODE)
          WHERE p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND p.DOC_TYPE = 15 AND NVL(p.CR_AMT,0) > 0 AND NVL(p.DOC_POST,0) = 1
            AND (:c_code IS NULL OR TO_CHAR(p.C_CODE) = :c_code OR c.C_A_NAME LIKE '%' || :c_code || '%')
            AND (:rep_code IS NULL OR TO_CHAR(p.REP_CODE) = :rep_code)
      ),
      all_lines AS (
          SELECT * FROM sales_lines
          UNION ALL
          SELECT * FROM return_lines
          UNION ALL
          SELECT * FROM ext_disc_notes
      )
      SELECT * FROM (
        SELECT NVL(t.c_code, 'مباشر') AS "كود العميل",
               NVL(MAX(c.C_A_NAME), 'عميل نقدي') AS "اسم العميل",
               TO_CHAR(SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc),'FM999,999,999,990.00') AS "المبيعات",
               TO_CHAR(SUM(t.cost),'FM999,999,999,990.00') AS "التكلفة",
               TO_CHAR(SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc) - SUM(t.cost),'FM999,999,999,990.00') AS "الربح",
               TO_CHAR(ROUND(100 * (SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc) - SUM(t.cost)) / NULLIF(SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc), 0), 1), 'FM990.0') || ' %' AS "هامش"
        FROM all_lines t
        LEFT JOIN CUSTOMER c ON TO_CHAR(c.C_CODE) = TO_CHAR(t.c_code)
        GROUP BY t.c_code
        ORDER BY SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc) - SUM(t.cost) DESC
      ) """

def get_prof_rep_sql():
    return """
      WITH dtl_disc_sum AS (
          SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS_BILL_DTL GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
      ),
      rt_dtl_disc_sum AS (
          SELECT RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS_RT_BILL_DTL GROUP BY RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER
      ),
      sales_lines AS (
          SELECT TO_CHAR(m.REP_CODE) as rep_code,
                 (NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) as gross_rev,
                 NVL(d.DIS_AMT,0) as line_disc,
                 CASE WHEN NVL(m.BILL_AMT,0) > 0 THEN
                     ((NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) / m.BILL_AMT) * GREATEST(0, NVL(m.DISC_AMT,0) - NVL(dds.tot_dtl_disc,0))
                 ELSE 0 END as extra_header_disc,
                 0 as ext_disc,
                 (NVL(d.I_QTY,0) * NVL(d.STK_COST,0)) as cost
          FROM IAS_BILL_DTL d
          JOIN IAS_BILL_MST m ON m.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND m.BILL_NO=d.BILL_NO AND m.BILL_SER=d.BILL_SER
          LEFT JOIN dtl_disc_sum dds ON dds.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND dds.BILL_NO=d.BILL_NO AND dds.BILL_SER=d.BILL_SER
          LEFT JOIN SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(m.REP_CODE)
          WHERE m.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND m.BILL_DOC_TYPE IN (1,4,8)
            AND (:rep_code IS NULL OR TO_CHAR(m.REP_CODE) = :rep_code OR sm.REPRS_A_NAME LIKE '%' || :rep_code || '%')
      ),
      return_lines AS (
          SELECT TO_CHAR(r.REP_CODE) as rep_code,
                 -(NVL(rd.I_QTY,0) * NVL(rd.I_PRICE,0)) as gross_rev,
                 -NVL(rd.DIS_AMT,0) as line_disc,
                 -CASE WHEN NVL(r.BILL_AMT,0) > 0 THEN
                     ((NVL(rd.I_QTY,0) * NVL(rd.I_PRICE,0)) / r.BILL_AMT) * GREATEST(0, NVL(r.DISC_AMT_MST,0) - NVL(rdds.tot_dtl_disc,0))
                 ELSE 0 END as extra_header_disc,
                 0 as ext_disc,
                 -(NVL(rd.I_QTY,0) * NVL(rd.STK_COST,0)) as cost
          FROM IAS_RT_BILL_DTL rd
          JOIN IAS_RT_BILL_MST r ON r.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND r.RT_BILL_NO=rd.RT_BILL_NO AND r.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN rt_dtl_disc_sum rdds ON rdds.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND rdds.RT_BILL_NO=rd.RT_BILL_NO AND rdds.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(r.REP_CODE)
          WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND r.RT_BILL_DOC_TYPE IN (1,4,8)
            AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code OR sm.REPRS_A_NAME LIKE '%' || :rep_code || '%')
      ),
      ext_disc_notes AS (
          SELECT TO_CHAR(p.REP_CODE) as rep_code,
                 0 as gross_rev,
                 0 as line_disc,
                 0 as extra_header_disc,
                 NVL(p.CR_AMT,0) as ext_disc,
                 0 as cost
          FROM IAS_POST_DTL p
          LEFT JOIN SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(p.REP_CODE)
          WHERE p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND p.DOC_TYPE = 15 AND NVL(p.CR_AMT,0) > 0 AND NVL(p.DOC_POST,0) = 1
            AND (:rep_code IS NULL OR TO_CHAR(p.REP_CODE) = :rep_code OR sm.REPRS_A_NAME LIKE '%' || :rep_code || '%')
      ),
      all_lines AS (
          SELECT * FROM sales_lines
          UNION ALL
          SELECT * FROM return_lines
          UNION ALL
          SELECT * FROM ext_disc_notes
      )
      SELECT t.rep_code AS "كود المندوب",
             MAX(sm.REPRS_A_NAME) AS "اسم المندوب",
             TO_CHAR(SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc),'FM999,999,999,990.00') AS "المبيعات",
             TO_CHAR(SUM(t.cost),'FM999,999,999,990.00') AS "التكلفة",
             TO_CHAR(SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc) - SUM(t.cost),'FM999,999,999,990.00') AS "الربح",
             TO_CHAR(ROUND(100 * (SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc) - SUM(t.cost)) / NULLIF(SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc), 0), 1), 'FM990.0') || ' %' AS "هامش"
      FROM all_lines t
      LEFT JOIN SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(t.rep_code)
      WHERE t.rep_code IS NOT NULL
      GROUP BY t.rep_code ORDER BY SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc) - SUM(t.cost) DESC"""

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
            AND NVL(DOC_POST,0)=1
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

