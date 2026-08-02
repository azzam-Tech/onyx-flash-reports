# -*- coding: utf-8 -*-
with open('app.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add GRP to parameters
if 'GRP   = {"name":"grp_by"' not in text:
    param_target = 'CST   = {"name":"c_code","label":"العميل (اختياري)","type":"text","default":""}'
    param_replace = '''GRP   = {"name":"grp_by","label":"تجميع حسب","type":"select","default":"rep","options":[["rep","المندوب"],["cc","مركز التكلفة"],["cst","العميل"]]}
CST   = {"name":"c_code","label":"العميل (اختياري)","type":"text","default":""}'''
    text = text.replace(param_target, param_replace)

# 2. Update collection_adopted report
old_query = '''    {"id":"collection_adopted","title":"تحصيل المناديب المعتمد","params":[DFROM,DTO,REP,INCR,INCN,INCC,INCRT,INCEX],"sql":"""
      WITH rc AS (
        SELECT REP_CODE, SUM(NVL(CR_AMT,0)) rcpt
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND C_CODE IS NOT NULL AND REP_CODE IS NOT NULL AND NVL(CR_AMT,0)>0
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY REP_CODE),
      nj AS (
        SELECT REP_CODE, SUM(NVL(CR_AMT,0)) net_jrn
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND REP_CODE IS NOT NULL AND NVL(CR_AMT,0)>0
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY REP_CODE),
      cs AS (
        SELECT REP_CODE, 
               SUM(NVL(BILL_AMT,0)-NVL(DISC_AMT,0)+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) cash_sales,
               SUM(NVL(DISC_AMT,0)) inv_disc
        FROM IAS20261.IAS_BILL_MST
        WHERE BILL_DOC_TYPE=1 AND REP_CODE IS NOT NULL
          AND BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY REP_CODE),
      cr AS (
        SELECT REP_CODE, SUM(NVL(CR_AMT,0)) cash_ret
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND REP_CODE IS NOT NULL AND NVL(CR_AMT,0)>0
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY REP_CODE),
      en AS (
        SELECT REP_CODE, SUM(NVL(CR_AMT,0)) ext_notice
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=15 AND REP_CODE IS NOT NULL AND NVL(CR_AMT,0)>0
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY REP_CODE),
      base AS (
        SELECT sm.REPRS_CODE rep_code, sm.REPRS_A_NAME rep_name,
               NVL(rc.rcpt,0) rcpt, NVL(nj.net_jrn,0) net_jrn, NVL(cs.cash_sales,0) cash_sales, NVL(cr.cash_ret,0) cash_ret,
               NVL(cs.inv_disc,0) inv_disc, NVL(en.ext_notice,0) ext_notice,
               (CASE WHEN :inc_rcpt='1' THEN NVL(rc.rcpt,0)    ELSE 0 END
              + CASE WHEN :inc_net='1'  THEN NVL(nj.net_jrn,0) ELSE 0 END
              + CASE WHEN :inc_cash='1' THEN NVL(cs.cash_sales,0) ELSE 0 END
              - CASE WHEN :inc_ret='1'  THEN NVL(cr.cash_ret,0) ELSE 0 END
              - CASE WHEN :inc_ext='1'  THEN NVL(en.ext_notice,0) ELSE 0 END) total_inc
        FROM IAS20261.SALES_MAN sm
        LEFT JOIN rc ON rc.REP_CODE = sm.REPRS_CODE
        LEFT JOIN nj ON nj.REP_CODE = sm.REPRS_CODE
        LEFT JOIN cs ON cs.REP_CODE = sm.REPRS_CODE
        LEFT JOIN cr ON cr.REP_CODE = sm.REPRS_CODE
        LEFT JOIN en ON en.REP_CODE = sm.REPRS_CODE
        WHERE (:rep_code IS NULL OR sm.REPRS_CODE = :rep_code))
      SELECT * FROM (
        SELECT rep_code AS "كود المندوب", rep_name AS "اسم المندوب",
               TO_CHAR(rcpt,'FM999,999,990.00')      AS "سندات القبض",
               TO_CHAR(net_jrn,'FM999,999,990.00')   AS "قيود الشبكة المنفصلة",
               TO_CHAR(cash_sales,'FM999,999,990.00') AS "المبيعات النقدية",
               TO_CHAR(inv_disc,'FM999,999,990.00')   AS "الخصم في الفاتورة",
               TO_CHAR(ext_notice,'FM999,999,990.00') AS "إشعار خصم مستقل (-)",
               TO_CHAR(cash_ret,'FM999,999,990.00')   AS "المرتجع النقدي (-)",
               TO_CHAR(total_inc,'FM999,999,990.00') AS "إجمالي التحصيل"
        FROM base
        WHERE (rcpt > 0 OR net_jrn > 0 OR cash_sales > 0 OR cash_ret > 0 OR inv_disc > 0 OR ext_notice > 0)
        ORDER BY total_inc DESC
      ) WHERE ROWNUM <= 300"""}'''

import re
old_query_regex = r'\{\"id\"\:\"collection_adopted\"\,.*?\n\s+\)\sWHERE\sROWNUM\s<=\s300\"\"\"\}'

new_query = '''    {"id":"collection_adopted","title":"التحصيل المعتمد (ديناميكي)","params":[DFROM,DTO,GRP,REP,INCR,INCN,INCC,INCRT,INCEX],"sql":"""
     WITH 
     grp AS (
       SELECT 'rep' as typ, TO_CHAR(REPRS_CODE) as cd, MAX(REPRS_A_NAME) as nm FROM IAS20261.SALES_MAN GROUP BY TO_CHAR(REPRS_CODE)
       UNION ALL 
       SELECT 'cc' as typ, TO_CHAR(CC_CODE) as cd, MAX(CC_A_NAME) as nm FROM IAS20261.COST_CENTERS GROUP BY TO_CHAR(CC_CODE)
       UNION ALL
       SELECT 'cst' as typ, TO_CHAR(C_CODE) as cd, MAX(C_A_NAME) as nm FROM IAS20261.CUSTOMER GROUP BY TO_CHAR(C_CODE)
       UNION ALL
       SELECT 'cst' as typ, 'UNKNOWN' as cd, 'عميل نقدي عام' as nm FROM DUAL
     ),
     all_trans AS (
       SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END as grp_code,
              CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as inv_disc, 0 as cash_ret, 0 as ext_notice
       FROM IAS20261.IAS_POST_DTL
       WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0
         AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       UNION ALL
       SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
              0, CR_AMT, 0, 0, 0, 0
       FROM IAS20261.IAS_POST_DTL
       WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0
         AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       UNION ALL
       SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
              0, 0, NVL(BILL_AMT,0)-NVL(DISC_AMT,0)+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0), NVL(DISC_AMT,0), 0, 0
       FROM IAS20261.IAS_BILL_MST
       WHERE BILL_DOC_TYPE=1
         AND BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       UNION ALL
       SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
              0, 0, 0, 0, CR_AMT, 0
       FROM IAS20261.IAS_POST_DTL
       WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0
         AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       UNION ALL
       SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
              0, 0, 0, 0, 0, CR_AMT
       FROM IAS20261.IAS_POST_DTL
       WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=15 AND NVL(CR_AMT,0)>0
         AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
     ),
     base AS (
       SELECT grp_code,
              SUM(rcpt) rcpt, SUM(net_jrn) net_jrn, SUM(cash_sales) cash_sales, SUM(inv_disc) inv_disc, SUM(cash_ret) cash_ret, SUM(ext_notice) ext_notice,
              (CASE WHEN :inc_rcpt='1' THEN SUM(rcpt) ELSE 0 END
             + CASE WHEN :inc_net='1'  THEN SUM(net_jrn) ELSE 0 END
             + CASE WHEN :inc_cash='1' THEN SUM(cash_sales) ELSE 0 END
             - CASE WHEN :inc_ret='1'  THEN SUM(cash_ret) ELSE 0 END
             - CASE WHEN :inc_ext='1'  THEN SUM(ext_notice) ELSE 0 END) total_inc
       FROM all_trans
       WHERE grp_code IS NOT NULL
         AND (:rep_code IS NULL OR (:grp_by = 'rep' AND grp_code = :rep_code))
       GROUP BY grp_code
     )
     SELECT * FROM (
       SELECT b.grp_code AS "الكود", NVL(MAX(g.nm), b.grp_code) AS "الجهة / الاسم",
              TO_CHAR(MAX(b.rcpt),'FM999,999,990.00')      AS "سندات القبض",
              TO_CHAR(MAX(b.net_jrn),'FM999,999,990.00')   AS "قيود الشبكة المنفصلة",
              TO_CHAR(MAX(b.cash_sales),'FM999,999,990.00') AS "المبيعات النقدية",
              TO_CHAR(MAX(b.inv_disc),'FM999,999,990.00')   AS "الخصم في الفاتورة",
              TO_CHAR(MAX(b.ext_notice),'FM999,999,990.00') AS "إشعار خصم مستقل (-)",
              TO_CHAR(MAX(b.cash_ret),'FM999,999,990.00')   AS "المرتجع النقدي (-)",
              TO_CHAR(MAX(b.total_inc),'FM999,999,990.00') AS "إجمالي التحصيل"
       FROM base b
       LEFT JOIN grp g ON g.cd = b.grp_code AND g.typ = :grp_by
       WHERE (b.rcpt > 0 OR b.net_jrn > 0 OR b.cash_sales > 0 OR b.cash_ret > 0 OR b.inv_disc > 0 OR b.ext_notice > 0)
       GROUP BY b.grp_code
       ORDER BY MAX(b.total_inc) DESC
     ) WHERE ROWNUM <= 300"""}'''

if old_query in text:
    text = text.replace(old_query, new_query)
else:
    text = re.sub(old_query_regex, new_query, text, flags=re.DOTALL)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated successfully!")
