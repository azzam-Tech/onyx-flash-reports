# -*- coding: utf-8 -*-
import re

with open('app.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. prof_summary
old_prof_summary = '''{"id":"prof_summary","title":"ملخّص مجمل الربح للفترة","params":[DFROM,DTO,REP],"sql":"""
     SELECT
       TO_CHAR(SUM(rev),'FM999,999,999,990.00') AS "المبيعات (بلا ضريبة)",
       TO_CHAR(SUM(cst),'FM999,999,999,990.00') AS "تكلفة المبيعات",
       TO_CHAR(SUM(rev)-SUM(cst),'FM999,999,999,990.00') AS "مجمل الربح",
       TO_CHAR(ROUND(100*(SUM(rev)-SUM(cst))/NULLIF(SUM(rev),0),1),'FM990.0')||' %' AS "الهامش"
     FROM (SELECT NVL(d.I_QTY,0)*(NVL(d.I_PRICE,0)-NVL(d.DIS_AMT,0)+NVL(d.OTHR_AMT,0)) rev,
                  NVL(d.I_QTY,0)*NVL(d.STK_COST,0) cst
           FROM IAS20261.IAS_BILL_DTL d JOIN IAS20261.IAS_BILL_MST m ON m.BILL_SER=d.BILL_SER
           WHERE m.BILL_DOC_TYPE IN (1,4)
             AND m.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
             AND (:rep_code IS NULL OR m.REP_CODE = :rep_code))"""}'''

new_prof_summary = '''{"id":"prof_summary","title":"ملخّص مجمل الربح للفترة","params":[DFROM,DTO,REP],"sql":"""
     WITH s AS (
       SELECT CASE WHEN m.BILL_DOC_TYPE IN (1,4) THEN 1 WHEN m.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              NVL(d.I_QTY,0) as qty, NVL(d.I_PRICE,0) as price, NVL(d.DIS_AMT,0) as line_disc,
              CASE WHEN NVL(m.BILL_AMT,0)=0 THEN 0 ELSE ((NVL(d.I_QTY,0)*NVL(d.I_PRICE,0))/m.BILL_AMT)*NVL(m.DISC_AMT,0) END as hdr_disc,
              NVL(d.OTHR_AMT,0) as othr, NVL(d.STK_COST,0) as unit_cost
       FROM IAS20261.IAS_BILL_DTL d JOIN IAS20261.IAS_BILL_MST m ON m.BILL_SER=d.BILL_SER
       WHERE m.BILL_DOC_TYPE IN (1,4,2,5)
         AND m.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND (:rep_code IS NULL OR m.REP_CODE = :rep_code)
     ),
     ext AS (
       SELECT NVL(CR_AMT,0) as ext_disc
       FROM IAS20261.IAS_POST_DTL
       WHERE DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
         AND (:rep_code IS NULL OR REP_CODE = :rep_code)
     )
     SELECT
       TO_CHAR(SUM(rev),'FM999,999,999,990.00') AS "المبيعات (بلا ضريبة)",
       TO_CHAR(SUM(cst),'FM999,999,999,990.00') AS "تكلفة المبيعات",
       TO_CHAR(SUM(rev)-SUM(cst),'FM999,999,999,990.00') AS "مجمل الربح",
       TO_CHAR(ROUND(100*(SUM(rev)-SUM(cst))/NULLIF(SUM(rev),0),1),'FM990.0')||' %' AS "الهامش"
     FROM (
       SELECT SUM(((qty*price) - line_disc - hdr_disc + othr) * sign) - (SELECT NVL(SUM(ext_disc),0) FROM ext) as rev,
              SUM(qty * unit_cost * sign) as cst
       FROM s
     )"""}'''

# 2. prof_item
old_prof_item = '''{"id":"prof_item","title":"ربحية الصنف","params":[DFROM,DTO,REP],"sql":"""
     SELECT * FROM (
       SELECT d.I_CODE AS "كود الصنف", MAX(i.I_NAME) AS "اسم الصنف",
              TO_CHAR(SUM(NVL(d.I_QTY,0)),'FM999,999,990.00') AS "الكمية",
              TO_CHAR(SUM(NVL(d.I_QTY,0)*(NVL(d.I_PRICE,0)-NVL(d.DIS_AMT,0)+NVL(d.OTHR_AMT,0))),'FM999,999,999,990.00') AS "المبيعات",
              TO_CHAR(SUM(NVL(d.I_QTY,0)*NVL(d.STK_COST,0)),'FM999,999,999,990.00') AS "التكلفة",
              TO_CHAR(SUM(NVL(d.I_QTY,0)*(NVL(d.I_PRICE,0)-NVL(d.DIS_AMT,0)+NVL(d.OTHR_AMT,0)))-SUM(NVL(d.I_QTY,0)*NVL(d.STK_COST,0)),'FM999,999,999,990.00') AS "الربح",
              TO_CHAR(ROUND(100*(SUM(NVL(d.I_QTY,0)*(NVL(d.I_PRICE,0)-NVL(d.DIS_AMT,0)+NVL(d.OTHR_AMT,0)))-SUM(NVL(d.I_QTY,0)*NVL(d.STK_COST,0)))/NULLIF(SUM(NVL(d.I_QTY,0)*(NVL(d.I_PRICE,0)-NVL(d.DIS_AMT,0)+NVL(d.OTHR_AMT,0))),0),1),'FM990.0')||' %' AS "هامش"
       FROM IAS20261.IAS_BILL_DTL d
       JOIN IAS20261.IAS_BILL_MST m ON m.BILL_SER=d.BILL_SER
       LEFT JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE=d.I_CODE
       WHERE m.BILL_DOC_TYPE IN (1,4)
         AND m.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND (:rep_code IS NULL OR m.REP_CODE = :rep_code)
       GROUP BY d.I_CODE ORDER BY SUM(NVL(d.I_QTY,0)*(NVL(d.I_PRICE,0)-NVL(d.DIS_AMT,0)+NVL(d.OTHR_AMT,0)))-SUM(NVL(d.I_QTY,0)*NVL(d.STK_COST,0)) DESC
     ) WHERE ROWNUM<=300"""}'''

new_prof_item = '''{"id":"prof_item","title":"ربحية الصنف","params":[DFROM,DTO,REP],"sql":"""
     WITH s AS (
       SELECT d.I_CODE,
              CASE WHEN m.BILL_DOC_TYPE IN (1,4) THEN 1 WHEN m.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              NVL(d.I_QTY,0) as qty, NVL(d.I_PRICE,0) as price, NVL(d.DIS_AMT,0) as line_disc,
              CASE WHEN NVL(m.BILL_AMT,0)=0 THEN 0 ELSE ((NVL(d.I_QTY,0)*NVL(d.I_PRICE,0))/m.BILL_AMT)*NVL(m.DISC_AMT,0) END as hdr_disc,
              NVL(d.OTHR_AMT,0) as othr, NVL(d.STK_COST,0) as unit_cost
       FROM IAS20261.IAS_BILL_DTL d JOIN IAS20261.IAS_BILL_MST m ON m.BILL_SER=d.BILL_SER
       WHERE m.BILL_DOC_TYPE IN (1,4,2,5)
         AND m.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND (:rep_code IS NULL OR m.REP_CODE = :rep_code)
     )
     SELECT * FROM (
       SELECT s.I_CODE AS "كود الصنف", MAX(i.I_NAME) AS "اسم الصنف",
              TO_CHAR(SUM(qty * sign),'FM999,999,990.00') AS "الكمية المباعة",
              TO_CHAR(SUM(((qty*price) - line_disc - hdr_disc + othr) * sign),'FM999,999,999,990.00') AS "المبيعات",
              TO_CHAR(SUM(qty * unit_cost * sign),'FM999,999,999,990.00') AS "التكلفة",
              TO_CHAR(SUM(((qty*price) - line_disc - hdr_disc + othr) * sign) - SUM(qty * unit_cost * sign),'FM999,999,999,990.00') AS "الربح",
              TO_CHAR(ROUND(100*(SUM(((qty*price) - line_disc - hdr_disc + othr) * sign) - SUM(qty * unit_cost * sign))/NULLIF(SUM(((qty*price) - line_disc - hdr_disc + othr) * sign),0),1),'FM990.0')||' %' AS "هامش"
       FROM s LEFT JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE=s.I_CODE
       GROUP BY s.I_CODE ORDER BY SUM(((qty*price) - line_disc - hdr_disc + othr) * sign) - SUM(qty * unit_cost * sign) DESC
     ) WHERE ROWNUM<=300"""}'''

# 3. prof_cust
old_prof_cust = '''{"id":"prof_cust","title":"ربحية العميل","params":[DFROM,DTO,REP],"sql":"""
     SELECT * FROM (
       SELECT m.C_CODE AS "كود العميل", MAX(c.C_A_NAME) AS "اسم العميل",
              TO_CHAR(SUM(NVL(d.I_QTY,0)*(NVL(d.I_PRICE,0)-NVL(d.DIS_AMT,0)+NVL(d.OTHR_AMT,0))),'FM999,999,999,990.00') AS "المبيعات",
              TO_CHAR(SUM(NVL(d.I_QTY,0)*NVL(d.STK_COST,0)),'FM999,999,999,990.00') AS "التكلفة",
              TO_CHAR(SUM(NVL(d.I_QTY,0)*(NVL(d.I_PRICE,0)-NVL(d.DIS_AMT,0)+NVL(d.OTHR_AMT,0)))-SUM(NVL(d.I_QTY,0)*NVL(d.STK_COST,0)),'FM999,999,999,990.00') AS "الربح",
              TO_CHAR(ROUND(100*(SUM(NVL(d.I_QTY,0)*(NVL(d.I_PRICE,0)-NVL(d.DIS_AMT,0)+NVL(d.OTHR_AMT,0)))-SUM(NVL(d.I_QTY,0)*NVL(d.STK_COST,0)))/NULLIF(SUM(NVL(d.I_QTY,0)*(NVL(d.I_PRICE,0)-NVL(d.DIS_AMT,0)+NVL(d.OTHR_AMT,0))),0),1),'FM990.0')||' %' AS "هامش"
       FROM IAS20261.IAS_BILL_DTL d
       JOIN IAS20261.IAS_BILL_MST m ON m.BILL_SER=d.BILL_SER
       LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE=m.C_CODE
       WHERE m.BILL_DOC_TYPE IN (1,4)
         AND m.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND (:rep_code IS NULL OR m.REP_CODE = :rep_code)
       GROUP BY m.C_CODE ORDER BY SUM(NVL(d.I_QTY,0)*(NVL(d.I_PRICE,0)-NVL(d.DIS_AMT,0)+NVL(d.OTHR_AMT,0)))-SUM(NVL(d.I_QTY,0)*NVL(d.STK_COST,0)) DESC
     ) WHERE ROWNUM<=300"""}'''

new_prof_cust = '''{"id":"prof_cust","title":"ربحية العميل","params":[DFROM,DTO,REP],"sql":"""
     WITH s AS (
       SELECT m.C_CODE,
              CASE WHEN m.BILL_DOC_TYPE IN (1,4) THEN 1 WHEN m.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              ((NVL(d.I_QTY,0)*NVL(d.I_PRICE,0)) - NVL(d.DIS_AMT,0) - (CASE WHEN NVL(m.BILL_AMT,0)=0 THEN 0 ELSE ((NVL(d.I_QTY,0)*NVL(d.I_PRICE,0))/m.BILL_AMT)*NVL(m.DISC_AMT,0) END) + NVL(d.OTHR_AMT,0)) as rev,
              (NVL(d.I_QTY,0)*NVL(d.STK_COST,0)) as cst,
              0 as ext_disc
       FROM IAS20261.IAS_BILL_DTL d JOIN IAS20261.IAS_BILL_MST m ON m.BILL_SER=d.BILL_SER
       WHERE m.BILL_DOC_TYPE IN (1,4,2,5)
         AND m.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND (:rep_code IS NULL OR m.REP_CODE = :rep_code)
       UNION ALL
       SELECT C_CODE, 1 as sign, 0 as rev, 0 as cst, NVL(CR_AMT,0) as ext_disc
       FROM IAS20261.IAS_POST_DTL
       WHERE DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
         AND (:rep_code IS NULL OR REP_CODE = :rep_code)
     )
     SELECT * FROM (
       SELECT s.C_CODE AS "كود العميل", MAX(c.C_A_NAME) AS "اسم العميل",
              TO_CHAR(SUM(rev * sign) - SUM(ext_disc),'FM999,999,999,990.00') AS "المبيعات",
              TO_CHAR(SUM(cst * sign),'FM999,999,999,990.00') AS "التكلفة",
              TO_CHAR((SUM(rev * sign) - SUM(ext_disc)) - SUM(cst * sign),'FM999,999,999,990.00') AS "الربح",
              TO_CHAR(ROUND(100*((SUM(rev * sign) - SUM(ext_disc)) - SUM(cst * sign))/NULLIF(SUM(rev * sign) - SUM(ext_disc),0),1),'FM990.0')||' %' AS "هامش"
       FROM s LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE=s.C_CODE
       WHERE s.C_CODE IS NOT NULL
       GROUP BY s.C_CODE ORDER BY (SUM(rev * sign) - SUM(ext_disc)) - SUM(cst * sign) DESC
     ) WHERE ROWNUM<=300"""}'''

# 4. prof_rep
old_prof_rep = '''{"id":"prof_rep","title":"ربحية المندوب","params":[DFROM,DTO],"sql":"""
     SELECT m.REP_CODE AS "كود المندوب", MAX(sm.REPRS_A_NAME) AS "اسم المندوب",
            TO_CHAR(SUM(NVL(d.I_QTY,0)*(NVL(d.I_PRICE,0)-NVL(d.DIS_AMT,0)+NVL(d.OTHR_AMT,0))),'FM999,999,999,990.00') AS "المبيعات",
              TO_CHAR(SUM(NVL(d.I_QTY,0)*NVL(d.STK_COST,0)),'FM999,999,999,990.00') AS "التكلفة",
              TO_CHAR(SUM(NVL(d.I_QTY,0)*(NVL(d.I_PRICE,0)-NVL(d.DIS_AMT,0)+NVL(d.OTHR_AMT,0)))-SUM(NVL(d.I_QTY,0)*NVL(d.STK_COST,0)),'FM999,999,999,990.00') AS "الربح",
              TO_CHAR(ROUND(100*(SUM(NVL(d.I_QTY,0)*(NVL(d.I_PRICE,0)-NVL(d.DIS_AMT,0)+NVL(d.OTHR_AMT,0)))-SUM(NVL(d.I_QTY,0)*NVL(d.STK_COST,0)))/NULLIF(SUM(NVL(d.I_QTY,0)*(NVL(d.I_PRICE,0)-NVL(d.DIS_AMT,0)+NVL(d.OTHR_AMT,0))),0),1),'FM990.0')||' %' AS "هامش"
     FROM IAS20261.IAS_BILL_DTL d
       JOIN IAS20261.IAS_BILL_MST m ON m.BILL_SER=d.BILL_SER
     LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=m.REP_CODE
     WHERE m.BILL_DOC_TYPE IN (1,4)
       AND m.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
     GROUP BY m.REP_CODE ORDER BY SUM(NVL(d.I_QTY,0)*(NVL(d.I_PRICE,0)-NVL(d.DIS_AMT,0)+NVL(d.OTHR_AMT,0)))-SUM(NVL(d.I_QTY,0)*NVL(d.STK_COST,0)) DESC"""}'''

new_prof_rep = '''{"id":"prof_rep","title":"ربحية المندوب","params":[DFROM,DTO],"sql":"""
     WITH s AS (
       SELECT m.REP_CODE,
              CASE WHEN m.BILL_DOC_TYPE IN (1,4) THEN 1 WHEN m.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              ((NVL(d.I_QTY,0)*NVL(d.I_PRICE,0)) - NVL(d.DIS_AMT,0) - (CASE WHEN NVL(m.BILL_AMT,0)=0 THEN 0 ELSE ((NVL(d.I_QTY,0)*NVL(d.I_PRICE,0))/m.BILL_AMT)*NVL(m.DISC_AMT,0) END) + NVL(d.OTHR_AMT,0)) as rev,
              (NVL(d.I_QTY,0)*NVL(d.STK_COST,0)) as cst,
              0 as ext_disc
       FROM IAS20261.IAS_BILL_DTL d JOIN IAS20261.IAS_BILL_MST m ON m.BILL_SER=d.BILL_SER
       WHERE m.BILL_DOC_TYPE IN (1,4,2,5)
         AND m.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       UNION ALL
       SELECT REP_CODE, 1 as sign, 0 as rev, 0 as cst, NVL(CR_AMT,0) as ext_disc
       FROM IAS20261.IAS_POST_DTL
       WHERE DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
     )
     SELECT s.REP_CODE AS "كود المندوب", MAX(sm.REPRS_A_NAME) AS "اسم المندوب",
            TO_CHAR(SUM(rev * sign) - SUM(ext_disc),'FM999,999,999,990.00') AS "المبيعات",
            TO_CHAR(SUM(cst * sign),'FM999,999,999,990.00') AS "التكلفة",
            TO_CHAR((SUM(rev * sign) - SUM(ext_disc)) - SUM(cst * sign),'FM999,999,999,990.00') AS "الربح",
            TO_CHAR(ROUND(100*((SUM(rev * sign) - SUM(ext_disc)) - SUM(cst * sign))/NULLIF(SUM(rev * sign) - SUM(ext_disc),0),1),'FM990.0')||' %' AS "هامش"
     FROM s LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=s.REP_CODE
     WHERE s.REP_CODE IS NOT NULL
     GROUP BY s.REP_CODE ORDER BY (SUM(rev * sign) - SUM(ext_disc)) - SUM(cst * sign) DESC"""}'''

# Replace all
if old_prof_summary in text: text = text.replace(old_prof_summary, new_prof_summary)
if old_prof_item in text: text = text.replace(old_prof_item, new_prof_item)
if old_prof_cust in text: text = text.replace(old_prof_cust, new_prof_cust)
if old_prof_rep in text: text = text.replace(old_prof_rep, new_prof_rep)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Profit reports SQL logic patched!")
