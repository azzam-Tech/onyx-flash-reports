import re

app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    content = f.read()

prof_tab_code = '''  {"id":"prof","title":"الربحية","icon":"M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z","reports":[
    {"id":"prof_summary","title":"ملخّص مجمل الربح للفترة","params":[DFROM,DTO,REP],"sql":"""
      WITH dtl_disc_sum AS (
          SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS20261.IAS_BILL_DTL GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
      ),
      rt_dtl_disc_sum AS (
          SELECT RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS20261.IAS_RT_BILL_DTL GROUP BY RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER
      ),
      sales_lines AS (
          SELECT NVL(d.I_QTY,0) as qty,
                 (NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) as gross_rev,
                 NVL(d.DIS_AMT,0) as line_disc,
                 CASE WHEN NVL(m.BILL_AMT,0) > 0 THEN
                     ((NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) / m.BILL_AMT) * GREATEST(0, NVL(m.DISC_AMT,0) - NVL(dds.tot_dtl_disc,0))
                 ELSE 0 END as extra_header_disc,
                 (NVL(d.I_QTY,0) * NVL(d.STK_COST,0)) as cost
          FROM IAS20261.IAS_BILL_DTL d
          JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND m.BILL_NO=d.BILL_NO AND m.BILL_SER=d.BILL_SER
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
          FROM IAS20261.IAS_RT_BILL_DTL rd
          JOIN IAS20261.IAS_RT_BILL_MST r ON r.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND r.RT_BILL_NO=rd.RT_BILL_NO AND r.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN rt_dtl_disc_sum rdds ON rdds.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND rdds.RT_BILL_NO=rd.RT_BILL_NO AND rdds.RT_BILL_SER=rd.RT_BILL_SER
          WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND r.RT_BILL_DOC_TYPE IN (1,4,8)
            AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code)
      ),
      ext_disc_notes AS (
          SELECT SUM(NVL(CR_AMT,0)) as ext_disc
          FROM IAS20261.IAS_POST_DTL
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
      CROSS JOIN ext_disc_notes e"""},
    {"id":"net_profit","title":"صافي الربح للفترة (بعد كل المصاريف)","params":[DFROM,DTO],"sql":"""
      SELECT
        TO_CHAR(SUM(CASE WHEN nt>0 THEN nt ELSE 0 END),'FM999,999,999,990.00') AS "الإيرادات",
        TO_CHAR(SUM(CASE WHEN nt<0 THEN -nt ELSE 0 END),'FM999,999,999,990.00') AS "المصاريف",
        TO_CHAR(SUM(nt),'FM999,999,999,990.00') AS "صافي الربح"
      FROM (SELECT p.A_CODE, SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)) nt
            FROM IAS20261.IAS_POST_DTL p JOIN IAS20261.ACCOUNT a ON a.A_CODE=p.A_CODE
            WHERE NVL(p.DOC_POST,0)=1 AND a.A_REPORT=2
              AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            GROUP BY p.A_CODE)"""},
    {"id":"prof_item","title":"ربحية الصنف","params":[DFROM,DTO,ITM,REP],"sql":"""
      WITH dtl_disc_sum AS (
          SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS20261.IAS_BILL_DTL GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
      ),
      rt_dtl_disc_sum AS (
          SELECT RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS20261.IAS_RT_BILL_DTL GROUP BY RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER
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
          FROM IAS20261.IAS_BILL_DTL d
          JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND m.BILL_NO=d.BILL_NO AND m.BILL_SER=d.BILL_SER
          LEFT JOIN dtl_disc_sum dds ON dds.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND dds.BILL_NO=d.BILL_NO AND dds.BILL_SER=d.BILL_SER
          LEFT JOIN IAS20261.IAS_ITM_MST im ON TO_CHAR(im.I_CODE) = TO_CHAR(d.I_CODE)
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
          FROM IAS20261.IAS_RT_BILL_DTL rd
          JOIN IAS20261.IAS_RT_BILL_MST r ON r.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND r.RT_BILL_NO=rd.RT_BILL_NO AND r.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN rt_dtl_disc_sum rdds ON rdds.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND rdds.RT_BILL_NO=rd.RT_BILL_NO AND rdds.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN IAS20261.IAS_ITM_MST im ON TO_CHAR(im.I_CODE) = TO_CHAR(rd.I_CODE)
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
        LEFT JOIN IAS20261.IAS_ITM_MST im ON TO_CHAR(im.I_CODE) = TO_CHAR(t.item_code)
        GROUP BY t.item_code
        ORDER BY SUM(t.gross_rev - t.line_disc - t.extra_header_disc) - SUM(t.cost) DESC
      ) WHERE ROWNUM<=300"""},
    {"id":"prof_cust","title":"ربحية العميل","params":[DFROM,DTO,CST,REP],"sql":"""
      WITH dtl_disc_sum AS (
          SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS20261.IAS_BILL_DTL GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
      ),
      rt_dtl_disc_sum AS (
          SELECT RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS20261.IAS_RT_BILL_DTL GROUP BY RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER
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
          FROM IAS20261.IAS_BILL_DTL d
          JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND m.BILL_NO=d.BILL_NO AND m.BILL_SER=d.BILL_SER
          LEFT JOIN dtl_disc_sum dds ON dds.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND dds.BILL_NO=d.BILL_NO AND dds.BILL_SER=d.BILL_SER
          LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = TO_CHAR(m.C_CODE)
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
          FROM IAS20261.IAS_RT_BILL_DTL rd
          JOIN IAS20261.IAS_RT_BILL_MST r ON r.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND r.RT_BILL_NO=rd.RT_BILL_NO AND r.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN rt_dtl_disc_sum rdds ON rdds.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND rdds.RT_BILL_NO=rd.RT_BILL_NO AND rdds.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = TO_CHAR(r.C_CODE)
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
          FROM IAS20261.IAS_POST_DTL p
          LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = TO_CHAR(p.C_CODE)
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
        LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = TO_CHAR(t.c_code)
        GROUP BY t.c_code
        ORDER BY SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc) - SUM(t.cost) DESC
      ) WHERE ROWNUM<=300"""},
    {"id":"prof_rep","title":"ربحية المندوب","params":[DFROM,DTO,REP],"sql":"""
      WITH dtl_disc_sum AS (
          SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS20261.IAS_BILL_DTL GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
      ),
      rt_dtl_disc_sum AS (
          SELECT RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS20261.IAS_RT_BILL_DTL GROUP BY RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER
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
          FROM IAS20261.IAS_BILL_DTL d
          JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND m.BILL_NO=d.BILL_NO AND m.BILL_SER=d.BILL_SER
          LEFT JOIN dtl_disc_sum dds ON dds.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND dds.BILL_NO=d.BILL_NO AND dds.BILL_SER=d.BILL_SER
          LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(m.REP_CODE)
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
          FROM IAS20261.IAS_RT_BILL_DTL rd
          JOIN IAS20261.IAS_RT_BILL_MST r ON r.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND r.RT_BILL_NO=rd.RT_BILL_NO AND r.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN rt_dtl_disc_sum rdds ON rdds.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND rdds.RT_BILL_NO=rd.RT_BILL_NO AND rdds.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(r.REP_CODE)
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
          FROM IAS20261.IAS_POST_DTL p
          LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(p.REP_CODE)
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
      LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(t.rep_code)
      WHERE t.rep_code IS NOT NULL
      GROUP BY t.rep_code ORDER BY SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc) - SUM(t.cost) DESC"""},
    {"id":"true_income_statement","title":"قائمة الدخل الحقيقية (تكاليف ومصاريف أونكس الحقيقية)","fn":"run_true_income_statement","params":[DFROM,DTO],"sql":""},
  ]}'''

# Find the start of prof tab and replace till stock tab
pattern = r'\{\s*"id"\s*:\s*"prof".*?\n\s*\}\s*,\s*\n\s*\{\s*"id"\s*:\s*"stock"'
match = re.search(pattern, content, re.DOTALL)
if match:
    new_content = content[:match.start()] + prof_tab_code + ',\n  {"id":"stock"' + content[match.end():]
    with open(app_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("SUCCESSFULLY REPLACED PROF TAB IN APP.PY!")
else:
    print("MATCH NOT FOUND!")
