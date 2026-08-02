import os
import json
import datetime
import bisect
import collections
from collections import defaultdict
from database import get_conn

SETTINGS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings.json")
PROFIT_TABS = {"prof"}
PROFIT_REPORTS = {"fin/income_statement", "fin/cost_centers"}
DFROM = {"name":"date_from","label":"من تاريخ","type":"date","default":"2026-01-01"}
DTO   = {"name":"date_to","label":"إلى تاريخ","type":"date","default":"2026-07-10"}
REP   = {"name":"rep_code","label":"المندوب (اختياري)","type":"text","default":""}
INCR  = {"name":"inc_rcpt","label":"سندات القبض","type":"select","default":"1","options":[["1","تضمين"],["0","استبعاد"]]}
INCN  = {"name":"inc_net","label":"قيود الشبكة المنفصلة","type":"select","default":"1","options":[["1","تضمين"],["0","استبعاد"]]}
INCC  = {"name":"inc_cash","label":"المبيعات النقدية","type":"select","default":"1","options":[["1","تضمين"],["0","استبعاد"]]}
INCRT = {"name":"inc_ret","label":"المرتجع النقدي (خصم)","type":"select","default":"1","options":[["1","خصم"],["0","تجاهل"]]}
INCEX = {"name":"inc_ext","label":"إشعار خصم مستقل (خصم)","type":"select","default":"0","hidden":True,"options":[["1","خصم"],["0","تجاهل"]]}
GRP   = {"name":"grp_by","label":"تجميع حسب","type":"select","default":"rep","options":[["rep","المندوب"],["cc","مركز التكلفة"],["cst","العميل"]]}
CST   = {"name":"c_code","label":"العميل (اختياري)","type":"text","default":""}
BTYPE = {"name":"bill_type","label":"نوع المستند","type":"select","default":"",
         "options":[["","الكل"],["1","مبيعات نقدية"],["4","مبيعات آجلة"],["2","مرتجع نقدي"],["5","مرتجع آجل"]]}
TABS = [
 {"id":"dash","title":"لوحة القيادة","icon":"M3 13h8V3H3zM13 21h8V3h-8zM3 21h8v-6H3z","dash":True,"reports":[{"id":"overview","title":"نظرة عامة","params":[{"name":"date_from","label":"من تاريخ","type":"date","default":"2026-01-01"},{"name":"date_to","label":"إلى تاريخ","type":"date","default":"2026-12-31"}]}]},
 {"id":"sales","title":"المبيعات","icon":"M4 20V10M10 20V4M16 20v-7M22 20H2","reports":[
   {"id":"bills","title":"فواتير المبيعات","params":[DFROM,DTO,BTYPE,REP,CST],"sql":"""
     SELECT CASE b.BILL_DOC_TYPE WHEN 1 THEN 'مبيعات نقدية' WHEN 4 THEN 'مبيعات آجلة' 
                 WHEN 2 THEN 'مرتجع نقدي' WHEN 5 THEN 'مرتجع آجل' ELSE 'أخرى' END AS "نوع المستند",
            b.BILL_NO AS "رقم الفاتورة", TO_CHAR(b.BILL_DATE,'YYYY-MM-DD') AS "التاريخ",
            b.C_CODE AS "كود العميل", MAX(c.C_A_NAME) AS "اسم العميل", b.REP_CODE AS "المندوب",
            TO_CHAR(NVL(b.BILL_AMT,0),'FM999,999,990.00') AS "المبلغ",
            TO_CHAR(NVL(d.itm_disc,0),'FM999,999,990.00') AS "خصم الأصناف",
            TO_CHAR(NVL(b.DISC_AMT,0),'FM999,999,990.00') AS "الخصم الإجمالي",
            TO_CHAR(NVL(b.VAT_AMT,0),'FM999,999,990.00') AS "الضريبة",
            TO_CHAR((NVL(b.BILL_AMT,0)-NVL(b.DISC_AMT,0)-NVL(d.itm_disc,0)+NVL(b.VAT_AMT,0)+NVL(b.OTHR_AMT,0)) * CASE WHEN b.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 1 END,'FM999,999,990.00') AS "الصافي",
            CASE NVL(b.BILL_POST,0) WHEN 1 THEN 'مرحّلة' ELSE 'غير مرحّلة' END AS "الحالة"
     FROM IAS20261.IAS_BILL_MST b
     LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = b.C_CODE
     LEFT JOIN (
         SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as itm_disc
         FROM IAS20261.IAS_BILL_DTL
         GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
     ) d ON b.BILL_DOC_TYPE = d.BILL_DOC_TYPE AND b.BILL_NO = d.BILL_NO AND b.BILL_SER = d.BILL_SER
     WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       AND b.BILL_DOC_TYPE IN (1,4,2,5)
       AND (:bill_type IS NULL OR b.BILL_DOC_TYPE = :bill_type)
       AND (:rep_code IS NULL OR b.REP_CODE = :rep_code)
       AND (:c_code IS NULL OR b.C_CODE = :c_code)
     GROUP BY b.BILL_DOC_TYPE, b.BILL_NO, b.BILL_DATE, b.C_CODE, b.REP_CODE, b.BILL_AMT, b.DISC_AMT, b.VAT_AMT, b.OTHR_AMT, b.BILL_POST, d.itm_disc
     ORDER BY b.BILL_DATE DESC, b.BILL_NO DESC FETCH FIRST 300 ROWS ONLY"""},
   {"id":"by_item","title":"حسب الصنف","params":[DFROM,DTO],"sql":"""
     WITH dt AS (
       SELECT dt.I_CODE,
              CASE WHEN b.BILL_DOC_TYPE IN (1,4) THEN 1 WHEN b.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              NVL(dt.I_QTY,0) as qty,
              (NVL(dt.I_QTY,0) * NVL(dt.I_PRICE,0) - NVL(dt.DIS_AMT,0)) as item_net,
              CASE WHEN NVL(b.BILL_AMT,0) = 0 THEN 0 ELSE 
                ((NVL(dt.I_QTY,0) * NVL(dt.I_PRICE,0)) / b.BILL_AMT) * NVL(b.DISC_AMT,0) 
              END as prorated_disc
       FROM IAS20261.IAS_BILL_DTL dt
       JOIN IAS20261.IAS_BILL_MST b ON b.BILL_DOC_TYPE=dt.BILL_DOC_TYPE AND b.BILL_NO=dt.BILL_NO AND b.BILL_SER=dt.BILL_SER
       WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND b.BILL_DOC_TYPE IN (1,4,2,5)
     )
     SELECT dt.I_CODE AS "كود الصنف", MAX(m.I_NAME) AS "اسم الصنف",
            ROUND(SUM(CASE WHEN dt.sign=1 THEN dt.qty ELSE 0 END),2) AS "كمية المبيعات",
            ROUND(SUM(CASE WHEN dt.sign=-1 THEN dt.qty ELSE 0 END),2) AS "كمية المردودات (-)",
            TO_CHAR(SUM(dt.item_net * dt.sign),'FM999,999,999,990.00') AS "قيمة المبيعات",
            TO_CHAR(SUM(dt.prorated_disc * dt.sign),'FM999,999,999,990.00') AS "نصيب الصنف من الخصم (-)",
            TO_CHAR(SUM((dt.item_net - dt.prorated_disc) * dt.sign),'FM999,999,999,990.00') AS "الصافي"
     FROM dt
     LEFT JOIN IAS20261.IAS_ITM_MST m ON m.I_CODE=dt.I_CODE
     GROUP BY dt.I_CODE
     ORDER BY SUM((dt.item_net - dt.prorated_disc) * dt.sign) DESC 
     FETCH FIRST 300 ROWS ONLY"""},
   {"id":"by_customer","title":"حسب العميل","params":[DFROM,DTO],"sql":"""
     WITH s AS (
       SELECT b.C_CODE, b.REP_CODE,
              CASE WHEN b.BILL_DOC_TYPE IN (1,4) THEN 1 ELSE 0 END as is_sale,
              CASE WHEN b.BILL_DOC_TYPE IN (2,5) THEN 1 ELSE 0 END as is_ret,
              CASE WHEN b.BILL_DOC_TYPE IN (1,4) THEN 1 WHEN b.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              NVL(b.BILL_AMT,0) amt, NVL(b.DISC_AMT,0) + NVL(d.itm_disc,0) disc, 0 as ext_disc, NVL(b.VAT_AMT,0) vat, NVL(b.OTHR_AMT,0) othr
       FROM IAS20261.IAS_BILL_MST b
       LEFT JOIN (
           SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as itm_disc
           FROM IAS20261.IAS_BILL_DTL
           GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
       ) d ON b.BILL_DOC_TYPE = d.BILL_DOC_TYPE AND b.BILL_NO = d.BILL_NO AND b.BILL_SER = d.BILL_SER
       WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND b.BILL_DOC_TYPE IN (1,4,2,5)
       UNION ALL
       SELECT C_CODE, REP_CODE,
              0 as is_sale, 0 as is_ret, 0 as sign,
              0 as amt, 0 as disc, NVL(CR_AMT,0) as ext_disc, 0 as vat, 0 as othr
       FROM IAS20261.IAS_POST_DTL
       WHERE DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
     )
     SELECT s.C_CODE AS "كود العميل", MAX(c.C_A_NAME) AS "اسم العميل", MAX(s.REP_CODE) AS "المندوب",
            SUM(s.is_sale) AS "فواتير مبيعات",
            SUM(s.is_ret) AS "فواتير مرتجعات",
            TO_CHAR(SUM(s.amt * s.is_sale),'FM999,999,999,990.00') AS "المبيعات",
            TO_CHAR(SUM(s.amt * s.is_ret),'FM999,999,999,990.00') AS "المردودات (-)",
            TO_CHAR(SUM(s.disc * s.sign),'FM999,999,999,990.00') AS "خصم الفواتير والأصناف (-)",
            TO_CHAR(SUM(s.ext_disc),'FM999,999,999,990.00') AS "إشعار خصم مستقل (-)",
            TO_CHAR(SUM((s.amt - s.disc) * s.sign) - SUM(s.ext_disc),'FM999,999,999,990.00') AS "الصافي قبل الضريبة",
            TO_CHAR(SUM((s.amt - s.disc + s.vat + s.othr) * s.sign) - SUM(s.ext_disc),'FM999,999,999,990.00') AS "الإجمالي بالضريبة"
     FROM s LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE=s.C_CODE
     WHERE s.C_CODE IS NOT NULL
     GROUP BY s.C_CODE 
     ORDER BY SUM((s.amt - s.disc) * s.sign) - SUM(s.ext_disc) DESC 
     FETCH FIRST 300 ROWS ONLY"""},
   {"id":"by_salesman","title":"حسب المندوب","params":[DFROM,DTO],"sql":"""
     WITH s AS (
       SELECT b.REP_CODE, b.C_CODE,
              CASE WHEN b.BILL_DOC_TYPE IN (1,4) THEN 1 ELSE 0 END as is_sale,
              CASE WHEN b.BILL_DOC_TYPE IN (2,5) THEN 1 ELSE 0 END as is_ret,
              CASE WHEN b.BILL_DOC_TYPE IN (1,4) THEN 1 WHEN b.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              NVL(b.BILL_AMT,0) amt, NVL(b.DISC_AMT,0) + NVL(d.itm_disc,0) disc, 0 as ext_disc, NVL(b.VAT_AMT,0) vat, NVL(b.OTHR_AMT,0) othr
       FROM IAS20261.IAS_BILL_MST b
       LEFT JOIN (
           SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as itm_disc
           FROM IAS20261.IAS_BILL_DTL
           GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
       ) d ON b.BILL_DOC_TYPE = d.BILL_DOC_TYPE AND b.BILL_NO = d.BILL_NO AND b.BILL_SER = d.BILL_SER
       WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND b.BILL_DOC_TYPE IN (1,4,2,5)
       UNION ALL
       SELECT REP_CODE, C_CODE,
              0 as is_sale, 0 as is_ret, 0 as sign,
              0 as amt, 0 as disc, NVL(CR_AMT,0) as ext_disc, 0 as vat, 0 as othr
       FROM IAS20261.IAS_POST_DTL
       WHERE DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
     )
     SELECT s.REP_CODE AS "كود المندوب", MAX(sm.REPRS_A_NAME) AS "اسم المندوب",
            COUNT(DISTINCT s.C_CODE) AS "عدد العملاء",
            SUM(s.is_sale) AS "فواتير مبيعات",
            SUM(s.is_ret) AS "فواتير مرتجعات",
            TO_CHAR(SUM(s.amt * s.is_sale),'FM999,999,999,990.00') AS "المبيعات",
            TO_CHAR(SUM(s.amt * s.is_ret),'FM999,999,999,990.00') AS "المردودات (-)",
            TO_CHAR(SUM(s.disc * s.sign),'FM999,999,999,990.00') AS "خصم الفواتير والأصناف (-)",
            TO_CHAR(SUM(s.ext_disc),'FM999,999,999,990.00') AS "إشعار خصم مستقل (-)",
            TO_CHAR(SUM((s.amt - s.disc) * s.sign) - SUM(s.ext_disc),'FM999,999,999,990.00') AS "الصافي قبل الضريبة",
            TO_CHAR(SUM((s.amt - s.disc + s.vat + s.othr) * s.sign) - SUM(s.ext_disc),'FM999,999,999,990.00') AS "الإجمالي بالضريبة"
     FROM s LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=s.REP_CODE
     WHERE s.REP_CODE IS NOT NULL
     GROUP BY s.REP_CODE 
     ORDER BY SUM((s.amt - s.disc) * s.sign) - SUM(s.ext_disc) DESC 
     FETCH FIRST 300 ROWS ONLY"""},
 ]},
 {"id":"ar","title":"العملاء والمدينون","icon":"M9 8a3 3 0 100-6 3 3 0 000 6zM3 20c0-3 3-5 6-5s6 2 6 5","reports":[
   {"id":"balances","title":"أرصدة العملاء","params":[DTO],"sql":"""
     SELECT p.C_CODE AS "كود العميل", MAX(c.C_A_NAME) AS "اسم العميل", MAX(c.REP_CODE) AS "المندوب",
            TO_CHAR(SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0)),'FM999,999,999,990.00') AS "الرصيد (مدين)"
     FROM IAS20261.IAS_POST_DTL p LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE=p.C_CODE
     WHERE p.C_CODE IS NOT NULL AND NVL(p.DOC_POST,0)=1
       AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
     GROUP BY p.C_CODE HAVING SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0))<>0
     ORDER BY SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0)) DESC FETCH FIRST 300 ROWS ONLY"""},
   {"id":"statement","title":"كشف حساب عميل","params":[{"name":"c_code","label":"كود العميل","type":"text","default":"1381"},DFROM,DTO],"sql":"""
      WITH open_bal AS (
        SELECT SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0)) as bal
        FROM IAS20261.IAS_POST_DTL
        WHERE C_CODE = :c_code AND NVL(DOC_POST,0)=1
          AND DOC_DATE < TO_DATE(:date_from,'YYYY-MM-DD')
      ),
      trans AS (
        SELECT p.DOC_DATE, d.JV_NAME, p.DOC_NO, p.DOC_DESC, NVL(p.DR_AMT,0) dr, NVL(p.CR_AMT,0) cr, p.DOC_SER
        FROM IAS20261.IAS_POST_DTL p
        LEFT JOIN IAS_SYS.IAS_DOCJV_TYPE_SYSTEMS d ON d.DOC_TYPE=p.DOC_TYPE AND d.JV_TYPE=p.JV_TYPE AND d.LANG_NO=1
        WHERE p.C_CODE = :c_code AND NVL(p.DOC_POST,0)=1
          AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      )
      SELECT "التاريخ","نوع المستند","رقم المستند","البيان","مدين","دائن","الرصيد" FROM (
        SELECT TO_CHAR(TO_DATE(:date_from,'YYYY-MM-DD')-1, 'YYYY-MM-DD') AS "التاريخ", 'رصيد افتتاحي' AS "نوع المستند",
               NULL AS "رقم المستند", 'رصيد ما قبل الفترة' AS "البيان",
               TO_CHAR(CASE WHEN bal>0 THEN bal ELSE 0 END,'FM999,999,990.00') AS "مدين",
               TO_CHAR(CASE WHEN bal<0 THEN -bal ELSE 0 END,'FM999,999,990.00') AS "دائن",
               TO_CHAR(NVL(bal,0),'FM999,999,990.00') AS "الرصيد",
               TO_DATE('1900-01-01','YYYY-MM-DD') s1, 0 s2, 0 s3
        FROM open_bal
        UNION ALL
        SELECT TO_CHAR(t.DOC_DATE,'YYYY-MM-DD'), t.JV_NAME, t.DOC_NO, t.DOC_DESC,
               TO_CHAR(t.dr,'FM999,999,990.00'), TO_CHAR(t.cr,'FM999,999,990.00'),
               TO_CHAR((SELECT NVL(bal,0) FROM open_bal) + SUM(t.dr-t.cr) OVER (ORDER BY t.DOC_DATE, t.DOC_NO, t.DOC_SER), 'FM999,999,990.00'),
               t.DOC_DATE s1, t.DOC_NO s2, t.DOC_SER s3
        FROM trans t
      ) ORDER BY s1, s2, s3 FETCH FIRST 1000 ROWS ONLY"""},
   {"id":"aging","title":"أعمار الديون","params":[
     DTO,
     {"name":"rep_code","label":"المندوب (اختياري)","type":"text","default":""},
     {"name":"c_code","label":"كود العميل (اختياري)","type":"text","default":""}
   ],"sql":"""
     WITH pay AS (SELECT C_CODE, SUM(NVL(CR_AMT,0)) paid FROM IAS20261.IAS_POST_DTL
                  WHERE NVL(DOC_POST,0)=1 AND C_CODE IS NOT NULL
                    AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
                  GROUP BY C_CODE),
     charges AS (SELECT p.C_CODE, p.DOC_DATE, NVL(p.DR_AMT,0) amt,
                   SUM(NVL(p.DR_AMT,0)) OVER (PARTITION BY p.C_CODE ORDER BY p.DOC_DATE,p.DOC_NO,p.DOC_SER
                        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) cum
                 FROM IAS20261.IAS_POST_DTL p
                 WHERE NVL(p.DOC_POST,0)=1 AND p.C_CODE IS NOT NULL AND NVL(p.DR_AMT,0)>0
                   AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1),
     openit AS (SELECT ch.C_CODE, GREATEST(0,LEAST(ch.amt,ch.cum-NVL(pay.paid,0))) unpaid,
                   TRUNC(TO_DATE(:date_to,'YYYY-MM-DD'))-TRUNC(ch.DOC_DATE) age
                FROM charges ch LEFT JOIN pay ON pay.C_CODE=ch.C_CODE)
     SELECT o.C_CODE AS "كود العميل", MAX(c.C_A_NAME) AS "اسم العميل", MAX(c.REP_CODE) AS "المندوب",
            TO_CHAR(SUM(CASE WHEN o.age<=30 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "0-30",
            TO_CHAR(SUM(CASE WHEN o.age BETWEEN 31 AND 60 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "31-60",
            TO_CHAR(SUM(CASE WHEN o.age BETWEEN 61 AND 90 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "61-90",
            TO_CHAR(SUM(CASE WHEN o.age BETWEEN 91 AND 120 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "91-120",
            TO_CHAR(SUM(CASE WHEN o.age>120 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "أكثر من 120",
            TO_CHAR(SUM(o.unpaid),'FM999,999,990.00') AS "الإجمالي"
     FROM openit o LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE=o.C_CODE
     WHERE o.unpaid>0 AND (:rep_code IS NULL OR c.REP_CODE = :rep_code)
       AND (:c_code IS NULL OR o.C_CODE = :c_code)
     GROUP BY o.C_CODE ORDER BY SUM(o.unpaid) DESC FETCH FIRST 300 ROWS ONLY"""},
   {"id":"dormant","title":"العملاء الخاملون","params":[{"name":"as_of","label":"حتى تاريخ","type":"date","default":"2026-07-10"},{"name":"days","label":"أيام الخمول","type":"number","default":"90"}],"sql":"""
     SELECT * FROM (
       SELECT c.C_CODE AS "كود العميل", c.C_A_NAME AS "اسم العميل", c.REP_CODE AS "المندوب",
              TO_CHAR(lb.last_bill,'YYYY-MM-DD') AS "آخر فاتورة",
              (TRUNC(TO_DATE(:as_of,'YYYY-MM-DD'))-TRUNC(lb.last_bill)) AS "أيام منذ آخر تعامل"
       FROM IAS20261.CUSTOMER c
       LEFT JOIN (SELECT C_CODE, MAX(BILL_DATE) last_bill FROM IAS20261.IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,4) GROUP BY C_CODE) lb ON lb.C_CODE=c.C_CODE
       WHERE NVL(c.INACTIVE,0)=0 AND (lb.last_bill IS NULL OR lb.last_bill < TO_DATE(:as_of,'YYYY-MM-DD') - :days)
       ORDER BY lb.last_bill NULLS FIRST
     ) WHERE ROWNUM <= 300"""},
 ]},
 {"id":"dts","title":"التوزيع والمناديب","icon":"M3 13l3-7h7l3 4h4v5M3 13h17M6 18a2 2 0 100-4 2 2 0 000 4zm11 0a2 2 0 100-4 2 2 0 000 4z","reports":[
   {"id":"collections","title":"تحصيل المناديب","params":[DFROM,DTO,REP],"sql":"""
     SELECT p.REP_CODE AS "كود المندوب", MAX(s.REPRS_A_NAME) AS "اسم المندوب",
            COUNT(DISTINCT p.C_CODE) AS "عدد العملاء",
            TO_CHAR(SUM(NVL(p.CR_AMT,0)),'FM999,999,999,990.00') AS "إجمالي التحصيل"
     FROM IAS20261.IAS_POST_DTL p LEFT JOIN IAS20261.SALES_MAN s ON s.REPRS_CODE = p.REP_CODE
     WHERE NVL(p.DOC_POST,0)=1 AND p.C_CODE IS NOT NULL AND NVL(p.CR_AMT,0)>0 AND p.REP_CODE IS NOT NULL AND p.DOC_TYPE = 2
       AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       AND (:rep_code IS NULL OR p.REP_CODE = :rep_code)
     GROUP BY p.REP_CODE ORDER BY SUM(NVL(p.CR_AMT,0)) DESC FETCH FIRST 300 ROWS ONLY"""},
   {"id":"performance","title":"أداء المناديب","params":[DFROM,DTO,REP],"sql":"""
     SELECT * FROM (
       SELECT s.REPRS_CODE AS "كود المندوب", s.REPRS_A_NAME AS "اسم المندوب",
              NVL(sl.inv,0) AS "عدد الفواتير", NVL(sl.custs,0) AS "عدد العملاء",
              TO_CHAR(NVL(sl.sales,0),'FM999,999,999,990.00') AS "المبيعات بالضريبة",
              TO_CHAR(NVL(col.coll,0),'FM999,999,999,990.00') AS "التحصيل",
              TO_CHAR(NVL(sl.sales,0)-NVL(col.coll,0),'FM999,999,999,990.00') AS "صافي (مبيعات - تحصيل)"
       FROM IAS20261.SALES_MAN s
       LEFT JOIN (SELECT REP_CODE, SUM(NVL(BILL_AMT,0)-NVL(DISC_AMT,0)+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) sales, COUNT(*) inv, COUNT(DISTINCT C_CODE) custs
                  FROM IAS20261.IAS_BILL_MST
                  WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1 AND BILL_DOC_TYPE IN (1,4)
                  GROUP BY REP_CODE) sl ON sl.REP_CODE = s.REPRS_CODE
       LEFT JOIN (SELECT REP_CODE, SUM(NVL(CR_AMT,0)) coll
                  FROM IAS20261.IAS_POST_DTL
                  WHERE NVL(DOC_POST,0)=1 AND C_CODE IS NOT NULL AND NVL(CR_AMT,0)>0 AND DOC_TYPE = 2
                    AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
                  GROUP BY REP_CODE) col ON col.REP_CODE = s.REPRS_CODE
       WHERE (sl.sales IS NOT NULL OR col.coll IS NOT NULL) AND (:rep_code IS NULL OR s.REPRS_CODE = :rep_code)
       ORDER BY NVL(sl.sales,0) DESC
     ) WHERE ROWNUM <= 300"""},
        {"id":"perf_aging","title":"أداء المناديب الموسّع (أعمار التحصيل)","params":[DFROM,DTO,REP],"sql":"""
      WITH coll AS (
        SELECT C_CODE, DOC_DATE as c_date, NVL(CR_AMT,0) as amt,
               NVL(DOC_TYPE_REF_DTL, DOC_TYPE_REF) as i_type, 
               NVL(DOC_NO_REF_DTL, DOC_NO_REF) as i_no, 
               NVL(DOC_SER_REF_DTL, DOC_SER_REF) as i_ser
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND NVL(CR_AMT,0) > 0
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      ),
      inv AS (
        SELECT DOC_TYPE, DOC_NO, DOC_SER, MAX(DOC_DATE) as i_date
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND NVL(DR_AMT,0) > 0
          AND C_CODE IN (SELECT DISTINCT C_CODE FROM coll)
        GROUP BY DOC_TYPE, DOC_NO, DOC_SER
      ),
      matched AS (
        SELECT c.C_CODE, c.amt, c.c_date,
               GREATEST(0, TRUNC(c.c_date) - TRUNC(NVL(i.i_date, c.c_date))) as age
        FROM coll c
        LEFT JOIN inv i ON i.DOC_TYPE = c.i_type AND i.DOC_NO = c.i_no AND i.DOC_SER = c.i_ser
      )
      SELECT * FROM (
        SELECT c.REP_CODE AS "كود المندوب", MAX(sm.REPRS_A_NAME) AS "اسم المندوب",
               COUNT(DISTINCT m.C_CODE) AS "عدد العملاء",
               TO_CHAR(SUM(CASE WHEN m.age<=30 THEN m.amt ELSE 0 END),'FM999,999,990.00') AS "0-30",
               TO_CHAR(SUM(CASE WHEN m.age BETWEEN 31 AND 60 THEN m.amt ELSE 0 END),'FM999,999,990.00') AS "31-60",
               TO_CHAR(SUM(CASE WHEN m.age BETWEEN 61 AND 90 THEN m.amt ELSE 0 END),'FM999,999,990.00') AS "61-90",
               TO_CHAR(SUM(CASE WHEN m.age BETWEEN 91 AND 120 THEN m.amt ELSE 0 END),'FM999,999,990.00') AS "91-120",
               TO_CHAR(SUM(CASE WHEN m.age>120 THEN m.amt ELSE 0 END),'FM999,999,990.00') AS "أكثر من 120",
               TO_CHAR(SUM(m.amt),'FM999,999,990.00') AS "المبلغ المحصل"
        FROM matched m JOIN IAS20261.CUSTOMER c ON c.C_CODE=m.C_CODE
        LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=c.REP_CODE
        WHERE (:rep_code IS NULL OR c.REP_CODE = :rep_code)
        GROUP BY c.REP_CODE ORDER BY SUM(m.amt) DESC
      ) WHERE ROWNUM <= 300"""},
        {"id":"perf_aging_dynamic","title":"أعمار التحصيل الصافي (ديناميكي)","params":[DFROM,DTO,REP,INCR,INCN,INCC,INCRT],"sql":"""
       -- This report dynamically processes valid collections via Python FIFO
       SELECT 'Dynamic' as "Placeholder" FROM DUAL
       """},
   {"id":"perf_aging_exact","title":"أعمار التحصيل (مطابق أونكس 100%)","params":[DFROM,DTO,REP],"sql":"""
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
     ) WHERE ROWNUM <= 300"""},
       {"id":"collection_adopted","title":"التحصيل المعتمد (ديناميكي)","params":[DFROM,DTO,GRP,REP,INCR,INCN,INCC,INCRT],"sql":"""
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
              CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as inv_disc, 0 as cash_ret, 0 as ext_notice, 0 as rcpt_unknown
       FROM IAS20261.IAS_POST_DTL
       WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
         AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       UNION ALL
       SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
              0, CR_AMT, 0, 0, 0, 0, 0
       FROM IAS20261.IAS_POST_DTL
       WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
         AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       UNION ALL
       SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
              0, 0, NVL(BILL_AMT,0)-NVL(DISC_AMT,0)+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0), NVL(DISC_AMT,0), 0, 0, 0
       FROM IAS20261.IAS_BILL_MST
       WHERE BILL_DOC_TYPE=1
         AND BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       UNION ALL
       SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
              0, 0, 0, 0, CR_AMT, 0, 0
       FROM IAS20261.IAS_POST_DTL
       WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0
         AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       UNION ALL
       SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
              0, 0, 0, 0, 0, CR_AMT, 0
       FROM IAS20261.IAS_POST_DTL
       WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=15 AND NVL(CR_AMT,0)>0
         AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       UNION ALL
       SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
              0, 0, 0, 0, 0, 0, CR_AMT
       FROM IAS20261.IAS_POST_DTL
       WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NULL
         AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
     ),
     base AS (
       SELECT grp_code,
              SUM(rcpt) rcpt, SUM(net_jrn) net_jrn, SUM(cash_sales) cash_sales, SUM(inv_disc) inv_disc, SUM(cash_ret) cash_ret, SUM(ext_notice) ext_notice, SUM(rcpt_unknown) rcpt_unknown,
              (CASE WHEN :inc_rcpt='1' THEN SUM(rcpt) ELSE 0 END
             + CASE WHEN :inc_net='1'  THEN SUM(net_jrn) ELSE 0 END
             + CASE WHEN :inc_cash='1' THEN SUM(cash_sales) ELSE 0 END
             - CASE WHEN :inc_ret='1'  THEN SUM(cash_ret) ELSE 0 END
             - 0) total_inc
       FROM all_trans
       WHERE grp_code IS NOT NULL
         AND (:rep_code IS NULL OR (:grp_by = 'rep' AND grp_code = :rep_code))
       GROUP BY grp_code
     )
     SELECT * FROM (
       SELECT b.grp_code AS "الكود", NVL(MAX(g.nm), b.grp_code) AS "الجهة / الاسم",
              TO_CHAR(MAX(b.rcpt),'FM999,999,990.00')      AS "سندات القبض",
              TO_CHAR(MAX(b.rcpt_unknown),'FM999,999,990.00') AS "إيداعات وتسويات (بدون عميل)",
              TO_CHAR(MAX(b.net_jrn),'FM999,999,990.00')   AS "قيود الشبكة المنفصلة",
              TO_CHAR(MAX(b.cash_sales),'FM999,999,990.00') AS "المبيعات النقدية",
              TO_CHAR(MAX(b.inv_disc),'FM999,999,990.00')   AS "الخصم في الفاتورة",
              TO_CHAR(MAX(b.ext_notice),'FM999,999,990.00') AS "إشعار خصم مستقل (-)",
              TO_CHAR(MAX(b.cash_ret),'FM999,999,990.00')   AS "المرتجع النقدي (-)",
              TO_CHAR(MAX(b.total_inc),'FM999,999,990.00') AS "إجمالي التحصيل"
       FROM base b
       LEFT JOIN grp g ON g.cd = b.grp_code AND g.typ = :grp_by
       WHERE (b.rcpt > 0 OR b.net_jrn > 0 OR b.cash_sales > 0 OR b.cash_ret > 0 OR b.inv_disc > 0 OR b.ext_notice > 0 OR b.rcpt_unknown > 0)
       GROUP BY b.grp_code
       ORDER BY MAX(b.total_inc) DESC
     ) WHERE ROWNUM <= 300"""},
 ]},
 {"id":"pur","title":"المشتريات والموردون","icon":"M6 6h15l-1.5 9h-12zM6 6L5 3H2M9 20a1 1 0 100-2 1 1 0 000 2zm9 0a1 1 0 100-2 1 1 0 000 2z","reports":[
   {"id":"pi_bills","title":"فواتير المشتريات","params":[DFROM,DTO,{"name":"v_code","label":"المورد (اختياري)","type":"text","default":""}],"sql":"""
     SELECT BILL_NO AS "رقم الفاتورة", TO_CHAR(BILL_DATE,'YYYY-MM-DD') AS "التاريخ",
            V_CODE AS "كود المورد", V_NAME AS "اسم المورد",
            TO_CHAR(NVL(BILL_AMT,0),'FM999,999,990.00') AS "المبلغ",
            TO_CHAR(NVL(DISC_AMT,0),'FM999,999,990.00') AS "الخصم",
            TO_CHAR(NVL(VAT_AMT,0),'FM999,999,990.00') AS "الضريبة",
            TO_CHAR(NVL(BILL_AMT,0)-NVL(DISC_AMT,0)+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0),'FM999,999,990.00') AS "الصافي",
            CASE NVL(BILL_POST,0) WHEN 1 THEN 'مرحّلة' ELSE 'غير مرحّلة' END AS "الحالة"
     FROM IAS20261.IAS_PI_BILL_MST
     WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       AND (:v_code IS NULL OR V_CODE = :v_code)
     ORDER BY BILL_DATE DESC, BILL_NO DESC FETCH FIRST 300 ROWS ONLY"""},
   {"id":"pi_by_vendor","title":"حسب المورد","params":[DFROM,DTO],"sql":"""
     SELECT V_CODE AS "كود المورد", MAX(V_NAME) AS "اسم المورد", COUNT(*) AS "عدد الفواتير",
            TO_CHAR(SUM(NVL(BILL_AMT,0)-NVL(DISC_AMT,0)),'FM999,999,999,990.00') AS "صافي قبل الضريبة",
            TO_CHAR(SUM(NVL(BILL_AMT,0)-NVL(DISC_AMT,0)+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)),'FM999,999,999,990.00') AS "الإجمالي بالضريبة"
     FROM IAS20261.IAS_PI_BILL_MST
     WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
     GROUP BY V_CODE ORDER BY SUM(NVL(BILL_AMT,0)-NVL(DISC_AMT,0)) DESC FETCH FIRST 300 ROWS ONLY"""},
   {"id":"pi_by_item","title":"حسب الصنف","params":[DFROM,DTO,{"name":"i_code","label":"الصنف (اختياري)","type":"text","default":""}],"sql":"""
     SELECT dt.I_CODE AS "كود الصنف", MAX(m.I_NAME) AS "اسم الصنف",
            ROUND(SUM(NVL(dt.I_QTY,0)),2) AS "إجمالي الكمية",
            TO_CHAR(ROUND(SUM(NVL(dt.I_QTY,0)*NVL(dt.I_PRICE,0)),2),'FM999,999,999,990.00') AS "قيمة المشتريات",
            COUNT(DISTINCT b.BILL_NO) AS "عدد الفواتير"
     FROM IAS20261.IAS_PI_BILL_DTL dt
     JOIN IAS20261.IAS_PI_BILL_MST b ON b.BILL_DOC_TYPE=dt.BILL_DOC_TYPE AND b.BILL_NO=dt.BILL_NO AND b.BILL_SER=dt.BILL_SER
     LEFT JOIN IAS20261.IAS_ITM_MST m ON m.I_CODE=dt.I_CODE
     WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       AND (:i_code IS NULL OR dt.I_CODE = :i_code)
     GROUP BY dt.I_CODE ORDER BY SUM(NVL(dt.I_QTY,0)*NVL(dt.I_PRICE,0)) DESC FETCH FIRST 300 ROWS ONLY"""},
   {"id":"vendor_statement","title":"كشف حساب مورد","params":[{"name":"v_code","label":"كود المورد","type":"text","default":"222"},DFROM,DTO],"sql":"""
     SELECT "التاريخ","نوع المستند","رقم المستند","البيان","مدين","دائن","الرصيد" FROM (
       SELECT TO_CHAR(p.DOC_DATE,'YYYY-MM-DD') AS "التاريخ", d.JV_NAME AS "نوع المستند",
              p.DOC_NO AS "رقم المستند", p.DOC_DESC AS "البيان",
              TO_CHAR(NVL(p.DR_AMT,0),'FM999,999,990.00') AS "مدين",
              TO_CHAR(NVL(p.CR_AMT,0),'FM999,999,990.00') AS "دائن",
              TO_CHAR(SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)) OVER (ORDER BY p.DOC_DATE,p.DOC_NO,p.DOC_SER),'FM999,999,990.00') AS "الرصيد",
              p.DOC_DATE s1, p.DOC_NO s2, p.DOC_SER s3
       FROM IAS20261.IAS_POST_DTL p
       LEFT JOIN IAS_SYS.IAS_DOCJV_TYPE_SYSTEMS d ON d.DOC_TYPE=p.DOC_TYPE AND d.JV_TYPE=p.JV_TYPE AND d.LANG_NO=1
       WHERE p.V_CODE = :v_code AND NVL(p.DOC_POST,0)=1
         AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       ORDER BY p.DOC_DATE, p.DOC_NO, p.DOC_SER
     ) FETCH FIRST 1000 ROWS ONLY"""},
   {"id":"vendor_aging","title":"أعمار الدائنين","params":[{"name":"as_of","label":"حتى تاريخ","type":"date","default":"2026-07-10"}],"sql":"""
     WITH pay AS (SELECT V_CODE, SUM(NVL(DR_AMT,0)) paid FROM IAS20261.IAS_POST_DTL
                  WHERE NVL(DOC_POST,0)=1 AND V_CODE IS NOT NULL GROUP BY V_CODE),
     charges AS (SELECT p.V_CODE, p.DOC_DATE, NVL(p.CR_AMT,0) amt,
                   SUM(NVL(p.CR_AMT,0)) OVER (PARTITION BY p.V_CODE ORDER BY p.DOC_DATE,p.DOC_NO,p.DOC_SER
                        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) cum
                 FROM IAS20261.IAS_POST_DTL p WHERE NVL(p.DOC_POST,0)=1 AND p.V_CODE IS NOT NULL AND NVL(p.CR_AMT,0)>0),
     openit AS (SELECT ch.V_CODE, GREATEST(0,LEAST(ch.amt,ch.cum-NVL(pay.paid,0))) unpaid,
                   TRUNC(TO_DATE(:as_of,'YYYY-MM-DD'))-TRUNC(ch.DOC_DATE) age
                FROM charges ch JOIN pay ON pay.V_CODE=ch.V_CODE)
     SELECT o.V_CODE AS "كود المورد", MAX(v.V_NAME) AS "اسم المورد",
            TO_CHAR(SUM(CASE WHEN o.age<=30 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "0-30",
            TO_CHAR(SUM(CASE WHEN o.age BETWEEN 31 AND 60 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "31-60",
            TO_CHAR(SUM(CASE WHEN o.age BETWEEN 61 AND 90 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "61-90",
            TO_CHAR(SUM(CASE WHEN o.age BETWEEN 91 AND 120 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "91-120",
            TO_CHAR(SUM(CASE WHEN o.age>120 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "أكثر من 120",
            TO_CHAR(SUM(o.unpaid),'FM999,999,990.00') AS "الإجمالي"
     FROM openit o LEFT JOIN (SELECT V_CODE, MAX(V_NAME) V_NAME FROM IAS20261.IAS_PI_BILL_MST GROUP BY V_CODE) v ON v.V_CODE=o.V_CODE
     WHERE o.unpaid>0 GROUP BY o.V_CODE ORDER BY SUM(o.unpaid) DESC FETCH FIRST 300 ROWS ONLY"""},
 ]},
 {"id":"fin","title":"المالية والمحاسبة","icon":"M4 20V4h16v16zM8 16v-4M12 16V8M16 16v-6","reports":[
   {"id":"trial_balance","title":"ميزان المراجعة","params":[DFROM,DTO],"sql":"""
     SELECT * FROM (
       SELECT p.A_CODE AS "رقم الحساب", MAX(a.A_NAME) AS "اسم الحساب",
              TO_CHAR(SUM(NVL(p.DR_AMT,0)),'FM999,999,999,990.00') AS "إجمالي مدين",
              TO_CHAR(SUM(NVL(p.CR_AMT,0)),'FM999,999,999,990.00') AS "إجمالي دائن",
              TO_CHAR(SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0)),'FM999,999,999,990.00') AS "الرصيد"
       FROM IAS20261.IAS_POST_DTL p LEFT JOIN IAS20261.ACCOUNT a ON a.A_CODE=p.A_CODE
       WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       GROUP BY p.A_CODE HAVING SUM(NVL(p.DR_AMT,0))<>0 OR SUM(NVL(p.CR_AMT,0))<>0
       ORDER BY p.A_CODE
     ) WHERE ROWNUM <= 500"""},
   {"id":"income_statement","title":"قائمة الدخل","params":[DFROM,DTO],"sql":"""
     SELECT NVL(pa.A_NAME, a.A_PARENT) AS "البند",
            TO_CHAR(SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)),'FM999,999,999,990.00') AS "الصافي"
     FROM IAS20261.IAS_POST_DTL p
     JOIN IAS20261.ACCOUNT a ON a.A_CODE=p.A_CODE
     LEFT JOIN IAS20261.ACCOUNT pa ON pa.A_CODE=a.A_PARENT
     WHERE NVL(p.DOC_POST,0)=1 AND a.A_REPORT=2
       AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
     GROUP BY a.A_PARENT, pa.A_NAME
     ORDER BY SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)) DESC"""},
   {"id":"cost_centers","title":"مراكز التكلفة","params":[DFROM,DTO],"sql":"""
     SELECT * FROM (
       SELECT p.CC_CODE AS "مركز التكلفة", MAX(cc.CC_A_NAME) AS "الاسم",
              TO_CHAR(SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)),'FM999,999,999,990.00') AS "صافي الربح/الخسارة"
       FROM IAS20261.IAS_POST_DTL p JOIN IAS20261.ACCOUNT a ON a.A_CODE=p.A_CODE
       LEFT JOIN IAS20261.COST_CENTERS cc ON cc.CC_CODE=p.CC_CODE
       WHERE NVL(p.DOC_POST,0)=1 AND a.A_REPORT=2
         AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       GROUP BY p.CC_CODE HAVING SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0))<>0
       ORDER BY SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)) DESC
     ) WHERE ROWNUM <= 200"""},
   {"id":"journal","title":"قيود اليومية","params":[{"name":"date_from","label":"من تاريخ","type":"date","default":"2026-07-01"},{"name":"date_to","label":"إلى تاريخ","type":"date","default":"2026-07-10"},{"name":"a_code","label":"الحساب (اختياري)","type":"text","default":""}],"sql":"""
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
     ) WHERE ROWNUM <= 300"""},
 ]},
 {"id":"tax","title":"الضريبة","icon":"M4 4h16v4H4zM6 8v12M18 8v12M4 20h16M9 12h6M9 16h6","reports":[
   {"id":"vat_decl","title":"الإقرار الضريبي (شهري)","params":[],"sql":"""
     SELECT PRD_NM AS "الفترة",
       TO_CHAR(-(SUM(CASE WHEN DOC_TYPE IN (4,5,15) THEN DOC_AMT_VAT ELSE 0 END)),'FM999,999,999,990.00') AS "المبيعات الخاضعة",
       TO_CHAR(-(SUM(CASE WHEN DOC_TYPE IN (4,5,15) THEN VAT_AMT ELSE 0 END)),'FM999,999,999,990.00') AS "ضريبة المخرجات",
       TO_CHAR(SUM(CASE WHEN DOC_TYPE IN (6,7,16) THEN DOC_AMT_VAT ELSE 0 END),'FM999,999,999,990.00') AS "المشتريات الخاضعة",
       TO_CHAR(SUM(CASE WHEN DOC_TYPE IN (6,7,16) THEN VAT_AMT ELSE 0 END),'FM999,999,999,990.00') AS "ضريبة المدخلات",
       TO_CHAR(SUM(CASE WHEN DOC_TYPE IN (1,3) THEN VAT_AMT ELSE 0 END),'FM999,999,999,990.00') AS "تعديلات",
       TO_CHAR(-(SUM(VAT_AMT)),'FM999,999,999,990.00') AS "صافي الضريبة المستحقة"
     FROM IAS20261.GNR_TAX_SUM_VW
     GROUP BY PRD_NO, PRD_NM ORDER BY PRD_NO"""},
   {"id":"vat_out","title":"تفصيل ضريبة المخرجات","params":[],"sql":"""
     SELECT PRD_NM AS "الفترة", DOC_TYP_NAME AS "نوع المستند",
       TO_CHAR(-(SUM(DOC_AMT_VAT)),'FM999,999,999,990.00') AS "الوعاء الخاضع",
       TO_CHAR(-(SUM(VAT_AMT)),'FM999,999,999,990.00') AS "الضريبة"
     FROM IAS20261.GNR_TAX_SUM_VW WHERE DOC_TYPE IN (4,5,15)
     GROUP BY PRD_NO, PRD_NM, DOC_TYPE, DOC_TYP_NAME ORDER BY PRD_NO, DOC_TYPE"""},
   {"id":"vat_in","title":"تفصيل ضريبة المدخلات","params":[],"sql":"""
     SELECT PRD_NM AS "الفترة", DOC_TYP_NAME AS "نوع المستند",
       TO_CHAR(SUM(DOC_AMT_VAT),'FM999,999,999,990.00') AS "الوعاء الخاضع",
       TO_CHAR(SUM(VAT_AMT),'FM999,999,999,990.00') AS "الضريبة"
     FROM IAS20261.GNR_TAX_SUM_VW WHERE DOC_TYPE IN (6,7,16,1,3)
     GROUP BY PRD_NO, PRD_NM, DOC_TYPE, DOC_TYP_NAME ORDER BY PRD_NO, DOC_TYPE"""},
 ]},
 {"id":"prof","title":"الربحية","icon":"M3 3v18h18M7 14l3-4 3 3 5-6","reports":[
   {"id":"prof_summary","title":"ملخّص مجمل الربح للفترة","params":[DFROM,DTO,REP],"sql":"""
     WITH s AS (
       SELECT CASE WHEN m.BILL_DOC_TYPE IN (1,4) THEN 1 WHEN m.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              NVL(d.I_QTY,0) as qty, NVL(d.I_PRICE,0) as price, NVL(d.DIS_AMT,0) as line_disc,
              CASE WHEN NVL(m.BILL_AMT,0)=0 THEN 0 ELSE ((NVL(d.I_QTY,0)*NVL(d.I_PRICE,0))/m.BILL_AMT)*NVL(m.DISC_AMT,0) END as hdr_disc,
              NVL(d.OTHR_AMT,0) as othr, NVL(d.STK_COST,0) as unit_cost
       FROM IAS20261.IAS_BILL_DTL d JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND m.BILL_NO=d.BILL_NO AND m.BILL_SER=d.BILL_SER
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
       SELECT (SELECT SUM(((qty*price) - line_disc - hdr_disc + othr) * sign) FROM s) - (SELECT NVL(SUM(ext_disc),0) FROM ext) as rev,
              (SELECT SUM(qty * unit_cost * sign) FROM s) as cst
       FROM DUAL
     )"""},
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
   {"id":"prof_item","title":"ربحية الصنف","params":[DFROM,DTO,REP],"sql":"""
     WITH s AS (
       SELECT d.I_CODE,
              CASE WHEN m.BILL_DOC_TYPE IN (1,4) THEN 1 WHEN m.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              NVL(d.I_QTY,0) as qty, NVL(d.I_PRICE,0) as price, NVL(d.DIS_AMT,0) as line_disc,
              CASE WHEN NVL(m.BILL_AMT,0)=0 THEN 0 ELSE ((NVL(d.I_QTY,0)*NVL(d.I_PRICE,0))/m.BILL_AMT)*NVL(m.DISC_AMT,0) END as hdr_disc,
              NVL(d.OTHR_AMT,0) as othr, NVL(d.STK_COST,0) as unit_cost
       FROM IAS20261.IAS_BILL_DTL d JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND m.BILL_NO=d.BILL_NO AND m.BILL_SER=d.BILL_SER
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
     ) WHERE ROWNUM<=300"""},
   {"id":"prof_cust","title":"ربحية العميل","params":[DFROM,DTO,REP],"sql":"""
     WITH s AS (
       SELECT m.C_CODE,
              CASE WHEN m.BILL_DOC_TYPE IN (1,4) THEN 1 WHEN m.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              ((NVL(d.I_QTY,0)*NVL(d.I_PRICE,0)) - NVL(d.DIS_AMT,0) - (CASE WHEN NVL(m.BILL_AMT,0)=0 THEN 0 ELSE ((NVL(d.I_QTY,0)*NVL(d.I_PRICE,0))/m.BILL_AMT)*NVL(m.DISC_AMT,0) END) + NVL(d.OTHR_AMT,0)) as rev,
              (NVL(d.I_QTY,0)*NVL(d.STK_COST,0)) as cst,
              0 as ext_disc
       FROM IAS20261.IAS_BILL_DTL d JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND m.BILL_NO=d.BILL_NO AND m.BILL_SER=d.BILL_SER
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
     ) WHERE ROWNUM<=300"""},
   {"id":"prof_rep","title":"ربحية المندوب","params":[DFROM,DTO],"sql":"""
     WITH s AS (
       SELECT m.REP_CODE,
              CASE WHEN m.BILL_DOC_TYPE IN (1,4) THEN 1 WHEN m.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              ((NVL(d.I_QTY,0)*NVL(d.I_PRICE,0)) - NVL(d.DIS_AMT,0) - (CASE WHEN NVL(m.BILL_AMT,0)=0 THEN 0 ELSE ((NVL(d.I_QTY,0)*NVL(d.I_PRICE,0))/m.BILL_AMT)*NVL(m.DISC_AMT,0) END) + NVL(d.OTHR_AMT,0)) as rev,
              (NVL(d.I_QTY,0)*NVL(d.STK_COST,0)) as cst,
              0 as ext_disc
       FROM IAS20261.IAS_BILL_DTL d JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND m.BILL_NO=d.BILL_NO AND m.BILL_SER=d.BILL_SER
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
     GROUP BY s.REP_CODE ORDER BY (SUM(rev * sign) - SUM(ext_disc)) - SUM(cst * sign) DESC"""},
 ]},
 {"id":"stock","title":"المخزون","icon":"M3 7l9-4 9 4-9 4zM3 7v10l9 4 9-4V7M12 11v10","reports":[
   {"id":"stock_bal","title":"أرصدة الأصناف","params":[{"name":"as_of","label":"حتى تاريخ","type":"date","default":"2026-07-10"},{"name":"w_code","label":"المستودع (اختياري)","type":"text","default":""}],"sql":"""
     SELECT * FROM (
       SELECT mv.I_CODE AS "كود الصنف", MAX(i.I_NAME) AS "اسم الصنف",
              TO_CHAR(SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))),'FM999,999,990.00') AS "الرصيد",
              TO_CHAR(SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))*NVL(mv.STK_COST,0)),'FM999,999,999,990.00') AS "قيمة الرصيد (تقريبية)"
       FROM IAS20261.ITEM_MOVEMENT mv LEFT JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE=mv.I_CODE
       WHERE mv.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1
         AND (:w_code IS NULL OR mv.W_CODE = :w_code)
       GROUP BY mv.I_CODE HAVING SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))) <> 0
       ORDER BY SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))*NVL(mv.STK_COST,0)) DESC
     ) WHERE ROWNUM<=300"""},
   {"id":"stock_move","title":"حركة صنف","params":[{"name":"i_code","label":"كود الصنف","type":"text","default":""},DFROM,DTO],"sql":"""
     SELECT * FROM (
       SELECT TO_CHAR(mv.I_DATE,'DD/MM/YYYY') AS "التاريخ", mv.DOC_NO AS "المستند",
              CASE NVL(mv.IN_OUT,0) WHEN 1 THEN 'وارد' ELSE 'صادر' END AS "الاتجاه",
              TO_CHAR(NVL(mv.I_QTY,0),'FM999,999,990.00') AS "الكمية",
              TO_CHAR(NVL(mv.STK_COST,0),'FM999,999,990.00') AS "التكلفة",
              mv.W_CODE AS "المستودع"
       FROM IAS20261.ITEM_MOVEMENT mv
       WHERE mv.I_CODE = :i_code
         AND mv.I_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND mv.I_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       ORDER BY mv.I_DATE, mv.DOC_NO
     ) WHERE ROWNUM<=500"""},
   {"id":"stock_dormant","title":"الأصناف الراكدة (لم تُبَع)","params":[{"name":"as_of","label":"حتى تاريخ","type":"date","default":"2026-07-10"},{"name":"days","label":"أيام الركود","type":"number","default":"90"}],"sql":"""
     SELECT * FROM (
       SELECT mv.I_CODE AS "كود الصنف", MAX(i.I_NAME) AS "اسم الصنف",
              TO_CHAR(SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))),'FM999,999,990.00') AS "الرصيد",
              TO_CHAR(MAX(CASE WHEN NVL(mv.IN_OUT,0)<>1 THEN mv.I_DATE END),'DD/MM/YYYY') AS "آخر صرف",
              TRUNC(TO_DATE(:as_of,'YYYY-MM-DD')) - TRUNC(MAX(CASE WHEN NVL(mv.IN_OUT,0)<>1 THEN mv.I_DATE END)) AS "أيام منذ آخر صرف"
       FROM IAS20261.ITEM_MOVEMENT mv LEFT JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE=mv.I_CODE
       WHERE mv.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1
       GROUP BY mv.I_CODE
       HAVING SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))) > 0
          AND ( MAX(CASE WHEN NVL(mv.IN_OUT,0)<>1 THEN mv.I_DATE END) IS NULL
                OR TRUNC(TO_DATE(:as_of,'YYYY-MM-DD')) - TRUNC(MAX(CASE WHEN NVL(mv.IN_OUT,0)<>1 THEN mv.I_DATE END)) >= :days )
       ORDER BY SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))) DESC
     ) WHERE ROWNUM<=300"""},
   {"id":"main_wh_movement","title":"حركة الأصناف (7 مستودعات)","params":[{"name":"i_code","label":"كود الصنف (اختياري)","type":"text","default":""},DFROM,DTO],"sql":""},
 ]},
 {"id":"general","title":"تقارير عامة","icon":"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z","reports":[
   {"id":"detailed_net_jrn","title":"قيود الشبكة التفصيلي","params":[DFROM,DTO,REP,CST],"sql":"""
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
   """}
 ]},
]
TABMAP = {t["id"]: t for t in TABS}

def _load_raw():
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def load_hidden_raw():
    d = _load_raw()
    return set(d.get("tabs", [])), set(d.get("reports", []))

def load_hide_profit():
    return bool(_load_raw().get("hide_profit"))

def load_hidden():
    """المجموعات الفعّالة المطبَّقة على الواجهة (تشمل إخفاء الربح إن كان مفعّلاً)."""
    tabs, reps = load_hidden_raw()
    if load_hide_profit():
        tabs = tabs | PROFIT_TABS
        reps = reps | PROFIT_REPORTS
    return tabs, reps

def save_hidden(tabs, reports, hide_profit=False):
    try:
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump({"tabs": list(tabs), "reports": list(reports),
                       "hide_profit": bool(hide_profit)}, f, ensure_ascii=False)
    except Exception as e:
        print("settings save error:", e)

def find_report(tab, rid):
    t = TABMAP.get(tab) or TABS[0]
    for r in t["reports"]:
        if r["id"] == rid:
            return t, r
    return t, t["reports"][0]

def run_report(rpt, args):
    if rpt["id"] in ["perf_aging", "perf_aging_dynamic"]:
        cols, rows = run_perf_aging_fifo(rpt, args)
    elif rpt["id"] == "main_wh_movement":
        cols, rows = run_main_wh_movement(rpt, args)
    else:
        binds = {}
        for p in rpt["params"]:
            v = args.get(p["name"], p.get("default",""))
            if p["type"] == "number":
                try: v = int(v)
                except: v = 0
                binds[p["name"]] = v
            else:
                if p["name"] in ("rep_code","c_code","v_code","i_code","a_code","w_code") and v:
                    v = v.split(" - ")[0].strip()
                binds[p["name"]] = v if v != "" else None
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute(rpt["sql"], binds)
                cols = [d[0] for d in cur.description]
                rows = cur.fetchall()
                
    return add_total_row(cols, rows)

def add_total_row(cols, rows):
    if not rows:
        return cols, rows
        
    totals = [0.0] * len(cols)
    is_numeric = [False] * len(cols)
    
    for col_idx in range(len(cols)):
        col_name = str(cols[col_idx]).lower()
        if any(x in col_name for x in ['كود', 'رقم', 'تاريخ', 'هاتف', 'code', 'no', 'date', 'phone', 'اسم', 'حساب']):
            continue
            
        for row in rows[:10]:
            val = row[col_idx]
            if val is None or val == "": 
                continue
            if isinstance(val, (int, float)):
                is_numeric[col_idx] = True
                break
            if isinstance(val, str):
                try:
                    float(val.replace(',', ''))
                    is_numeric[col_idx] = True
                    break
                except ValueError:
                    pass
                    
    for row in rows:
        for col_idx in range(len(cols)):
            if is_numeric[col_idx]:
                val = row[col_idx]
                if val is not None and val != "":
                    if isinstance(val, str):
                        try:
                            totals[col_idx] += float(val.replace(',', ''))
                        except ValueError:
                            pass
                    else:
                        totals[col_idx] += float(val)
                        
    total_row = []
    has_total_label = False
    
    for col_idx in range(len(cols)):
        if is_numeric[col_idx]:
            total_row.append(f"{totals[col_idx]:,.2f}")
        else:
            if not has_total_label and not any(x in str(cols[col_idx]).lower() for x in ['كود', 'رقم', 'code', 'no']):
                total_row.append("الإجمالي")
                has_total_label = True
            elif not has_total_label and col_idx == 0:
                total_row.append("الإجمالي")
                has_total_label = True
            else:
                total_row.append("")
                
    if not has_total_label:
        total_row[0] = "الإجمالي"
        
    return cols, [tuple(total_row)] + list(rows)

def lookups(name):
    if name in _LK_CACHE:
        return _LK_CACHE[name]
    q = {
      "rep_code": "SELECT REPRS_CODE, REPRS_A_NAME FROM IAS20261.SALES_MAN WHERE REPRS_CODE IS NOT NULL ORDER BY REPRS_A_NAME",
      "c_code":   "SELECT C_CODE, C_A_NAME FROM IAS20261.CUSTOMER WHERE NVL(INACTIVE,0)=0 AND C_CODE IS NOT NULL ORDER BY C_A_NAME",
      "v_code":   "SELECT V_CODE, MAX(V_NAME) FROM IAS20261.IAS_PI_BILL_MST WHERE V_CODE IS NOT NULL GROUP BY V_CODE ORDER BY MAX(V_NAME)",
      "i_code":   "SELECT I_CODE, I_NAME FROM IAS20261.IAS_ITM_MST WHERE I_CODE IS NOT NULL ORDER BY I_NAME",
      "a_code":   "SELECT A_CODE, A_NAME FROM IAS20261.ACCOUNT WHERE A_CODE IS NOT NULL ORDER BY A_CODE",
    }.get(name)
    if not q:
        return []
    out = []
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute(q)
                for code, nm in cur.fetchall():
                    if code is None:
                        continue
                    out.append(("%s - %s" % (str(code).strip(), (nm or "").strip())).strip(" -"))
        _LK_CACHE[name] = out
        return out
    except Exception:
        return []

def jv_options():
    global _JV_CACHE
    if _JV_CACHE is not None:
        return _JV_CACHE
    opts = [["","الكل"]]
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute("""SELECT p.JV_TYPE, MAX(j.JV_NAME) nm
                    FROM IAS20261.IAS_POST_DTL p
                    LEFT JOIN IAS20261.JV_TYPES j ON j.JV_TYPE=p.JV_TYPE
                    WHERE p.C_CODE IS NOT NULL AND NVL(p.DOC_POST,0)=1
                    GROUP BY p.JV_TYPE ORDER BY COUNT(*) DESC""")
                for t, nm in cur.fetchall():
                    if t is None: continue
                    code = str(int(t))
                    label = nm or ("بدون نوع" if int(t)==0 else "نوع "+code)
                    opts.append([code, label])
        _JV_CACHE = opts
        return _JV_CACHE
    except Exception:
        return [["","الكل"],["1","قيد يومية"],["2","قيود الشبكة"],["4","قيود دائنون"],["9","قيد ضريبي"],["11","رصيد افتتاحي للعملاء"],["0","بدون نوع"]]

def compute_dash(f, t):
    b = {"f": f, "t": t}
    P="TO_DATE(:f,\'YYYY-MM-DD\')"; Q="TO_DATE(:t,\'YYYY-MM-DD\')+1"
    d = {"sales":0,"collect":0,"purch":0,"gross":0,"netprofit":0,"recv":0,"invval":0,"vat":0,
         "months":[],"msales":[],"mcollect":[],"mpurch":[],"rep_labels":[],"rep_vals":[],"itm_labels":[],"itm_vals":[]}
    try:
        with get_conn() as con:
            cur = con.cursor()
            def sc(sql):
                try:
                    cur.execute(sql,{k:v for k,v in b.items() if (":"+k) in sql}); r=cur.fetchone()
                    return round(float(r[0]),2) if r and r[0] is not None else 0.0
                except Exception: return 0.0
            def rw(sql):
                try:
                    cur.execute(sql,{k:v for k,v in b.items() if (":"+k) in sql}); return cur.fetchall()
                except Exception: return []
            d["sales"]=sc("SELECT NVL(SUM(NVL(BILL_AMT,0)-NVL(DISC_AMT,0)+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)),0) FROM IAS20261.IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,4) AND BILL_DATE>="+P+" AND BILL_DATE<"+Q)
            d["collect"]=sc("SELECT NVL(SUM(NVL(CR_AMT,0)),0) FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND C_CODE IS NOT NULL AND DOC_DATE>="+P+" AND DOC_DATE<"+Q)
            d["purch"]=sc("SELECT NVL(SUM(NVL(BILL_AMT,0)-NVL(DISC_AMT,0)+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)),0) FROM IAS20261.IAS_PI_BILL_MST WHERE BILL_DATE>="+P+" AND BILL_DATE<"+Q)
            d["gross"]=sc("SELECT NVL(SUM(NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))-NVL(x.I_QTY,0)*NVL(x.STK_COST,0)),0) FROM IAS20261.IAS_BILL_DTL x JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=x.BILL_DOC_TYPE AND m.BILL_NO=x.BILL_NO AND m.BILL_SER=x.BILL_SER WHERE m.BILL_DOC_TYPE IN (1,4) AND m.BILL_DATE>="+P+" AND m.BILL_DATE<"+Q)
            d["netprofit"]=sc("SELECT NVL(SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)),0) FROM IAS20261.IAS_POST_DTL p JOIN IAS20261.ACCOUNT a ON a.A_CODE=p.A_CODE WHERE NVL(p.DOC_POST,0)=1 AND a.A_REPORT=2 AND p.DOC_DATE>="+P+" AND p.DOC_DATE<"+Q)
            d["recv"]=sc("SELECT NVL(SUM(bal),0) FROM (SELECT SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0)) bal FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND C_CODE IS NOT NULL AND DOC_DATE<"+Q+" GROUP BY C_CODE HAVING SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0))>0)")
            d["invval"]=sc("SELECT NVL(SUM(NVL(I_QTY,0)*NVL(IN_OUT,0)*NVL(STK_COST,0)),0) FROM IAS20261.ITEM_MOVEMENT WHERE I_DATE<"+Q)
            ov=sc("SELECT NVL(SUM(NVL(VAT_AMT,0)),0) FROM IAS20261.IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,4) AND BILL_DATE>="+P+" AND BILL_DATE<"+Q)
            iv=sc("SELECT NVL(SUM(NVL(VAT_AMT,0)),0) FROM IAS20261.IAS_PI_BILL_MST WHERE BILL_DATE>="+P+" AND BILL_DATE<"+Q)
            d["vat"]=round(ov-iv,2)
            def mm(sql):
                m={}
                for r in rw(sql):
                    m[str(r[0])]=round(float(r[1] or 0),2)
                return m
            ms=mm("SELECT TO_CHAR(BILL_DATE,\'YYYY-MM\'), SUM(NVL(BILL_AMT,0)-NVL(DISC_AMT,0)+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) FROM IAS20261.IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,4) AND BILL_DATE>="+P+" AND BILL_DATE<"+Q+" GROUP BY TO_CHAR(BILL_DATE,\'YYYY-MM\')")
            mc=mm("SELECT TO_CHAR(DOC_DATE,\'YYYY-MM\'), SUM(NVL(CR_AMT,0)) FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND C_CODE IS NOT NULL AND DOC_DATE>="+P+" AND DOC_DATE<"+Q+" GROUP BY TO_CHAR(DOC_DATE,\'YYYY-MM\')")
            mp=mm("SELECT TO_CHAR(BILL_DATE,\'YYYY-MM\'), SUM(NVL(BILL_AMT,0)-NVL(DISC_AMT,0)+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) FROM IAS20261.IAS_PI_BILL_MST WHERE BILL_DATE>="+P+" AND BILL_DATE<"+Q+" GROUP BY TO_CHAR(BILL_DATE,\'YYYY-MM\')")
            months=sorted(set(list(ms)+list(mc)+list(mp)))
            d["months"]=months
            d["msales"]=[ms.get(x,0) for x in months]
            d["mcollect"]=[mc.get(x,0) for x in months]
            d["mpurch"]=[mp.get(x,0) for x in months]
            for r in rw("SELECT NVL(sm.REPRS_A_NAME, m.REP_CODE) nm, SUM(NVL(m.BILL_AMT,0)-NVL(m.DISC_AMT,0)+NVL(m.VAT_AMT,0)+NVL(m.OTHR_AMT,0)) v FROM IAS20261.IAS_BILL_MST m LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=m.REP_CODE WHERE m.BILL_DOC_TYPE IN (1,4) AND m.BILL_DATE>="+P+" AND m.BILL_DATE<"+Q+" GROUP BY NVL(sm.REPRS_A_NAME,m.REP_CODE) ORDER BY v DESC FETCH FIRST 7 ROWS ONLY"):
                d["rep_labels"].append(str(r[0])); d["rep_vals"].append(round(float(r[1] or 0),2))
            for r in rw("SELECT NVL(i.I_NAME, x.I_CODE) nm, SUM(NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))) v FROM IAS20261.IAS_BILL_DTL x JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=x.BILL_DOC_TYPE AND m.BILL_NO=x.BILL_NO AND m.BILL_SER=x.BILL_SER LEFT JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE=x.I_CODE WHERE m.BILL_DOC_TYPE IN (1,4) AND m.BILL_DATE>="+P+" AND m.BILL_DATE<"+Q+" GROUP BY NVL(i.I_NAME,x.I_CODE) ORDER BY v DESC FETCH FIRST 7 ROWS ONLY"):
                d["itm_labels"].append(str(r[0])[:22]); d["itm_vals"].append(round(float(r[1] or 0),2))
    except Exception as e:
        d["err"]=str(e)
    return d

def run_perf_aging_fifo(rpt, args):
    import bisect
    from collections import defaultdict
    from datetime import datetime
    
    is_dynamic = (rpt.get("id") == "perf_aging_dynamic")
    
    rep_code = args.get("rep_code")
    if is_dynamic:
        inc_rcpt = str(args.get("inc_rcpt", "1")) == "1"
        inc_net  = str(args.get("inc_net", "1")) == "1"
        inc_cash = str(args.get("inc_cash", "1")) == "1"
        inc_ret  = str(args.get("inc_ret", "1")) == "1"
        inc_ext  = False
    else:
        inc_rcpt = True
        inc_net  = False
        inc_cash = False
        inc_ret  = False
        inc_ext  = False
    if rep_code:
        rep_code = rep_code.split(" - ")[0].strip()
    
    date_from_str = args.get("date_from", "")
    date_to_str = args.get("date_to", "")
    if not date_from_str: date_from_str = "2026-06-01"
    if not date_to_str: date_to_str = "2026-06-30"
    
    from_dt = datetime.strptime(date_from_str, '%Y-%m-%d').date()
    to_dt = datetime.strptime(date_to_str, '%Y-%m-%d').date()

    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT C_CODE, REP_CODE FROM IAS20261.CUSTOMER")
            cust_rep = {str(c): str(r) for c, r in cur.fetchall()}
                
            cur.execute("SELECT REPRS_CODE, REPRS_A_NAME FROM IAS20261.SALES_MAN")
            rep_name = {str(c): n for c, n in cur.fetchall()}

            # Get Cash Sales for the period (no C_CODE needed)
            sql_cash = """
                SELECT TO_CHAR(REP_CODE), SUM(NVL(BILL_AMT,0)-NVL(DISC_AMT,0)+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0))
                FROM IAS20261.IAS_BILL_MST
                WHERE BILL_DOC_TYPE=1
                  AND BILL_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND BILL_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
                GROUP BY TO_CHAR(REP_CODE)
            """
            cur.execute(sql_cash, {"df": date_from_str, "dt": date_to_str})
            cash_sales_by_rep = {r: float(amt) for r, amt in cur.fetchall() if r}

            # Fetch relevant debits and credits from IAS_POST_DTL
            sql = """
                SELECT p.C_CODE, p.DOC_DATE, NVL(p.DR_AMT,0), NVL(p.CR_AMT,0), p.DOC_TYPE, p.JV_TYPE, p.A_CODE
                FROM IAS20261.IAS_POST_DTL p
                WHERE NVL(p.DOC_POST,0)=1
                  AND (NVL(p.DR_AMT,0) > 0 OR NVL(p.CR_AMT,0) > 0)
            """
            cur.execute(sql)
            byc = defaultdict(lambda: {"debits": [], "credits": []})
            
            for ccode, ddate, dr, cr, dtype, jvtype, acode in cur.fetchall():
                if ccode is None: continue
                d = ddate.date() if hasattr(ddate, "date") else ddate
                dr = float(dr)
                cr = float(cr)
                
                valid_cr = 0.0
                if cr > 0:
                    if not is_dynamic:
                        valid_cr = cr
                    else:
                        if dtype == 2 and inc_rcpt:  # rcpt
                            valid_cr = cr
                        elif dtype == 1 and jvtype == 2 and inc_net:  # net_jrn
                            valid_cr = cr
                        elif dtype == 5 and acode and str(acode).startswith('111') and inc_ret:  # cash_ret
                            valid_cr = -cr
                        elif dtype == 15 and inc_ext:  # ext_notice
                            valid_cr = -cr
                
                if dr > 0:
                    byc[str(ccode)]["debits"].append((d, dr))
                if valid_cr != 0:
                    byc[str(ccode)]["credits"].append((d, valid_cr))

    def bucket_of(age):
        if age <= 30:  return 0
        if age <= 60:  return 1
        if age <= 90:  return 2
        if age <= 120: return 3
        return 4

    rep_results = defaultdict(lambda: {"cust_count": set(), "b": [0.0]*5, "total": 0.0})

    for ccode, evs in byc.items():
        r_code = cust_rep.get(ccode)
        if not r_code: continue
        if rep_code and r_code != rep_code: continue

        debits  = sorted(evs["debits"], key=lambda x: x[0])
        credits = sorted(evs["credits"], key=lambda x: x[0])
        
        dcum = 0.0; dint = []
        for (d, dr) in debits:
            lo = dcum; dcum += dr; dint.append((lo, dcum, d))
        ddates = [x[0] for x in debits]
        
        ccum = 0.0
        for (d, cr) in credits:
            clo = ccum; ccum += cr; chi = ccum
            if not (from_dt <= d <= to_dt):
                continue
            
            # Handle negative credits (deductions)
            lo_cr, hi_cr = min(clo, chi), max(clo, chi)
            is_negative = (cr < 0)
            
            rep_results[r_code]["cust_count"].add(ccode)
            rep_results[r_code]["total"] += cr
            
            for (lo, hi, idate) in dint:
                if lo < hi_cr and hi > lo_cr:
                    amt = min(hi_cr, hi) - max(lo_cr, lo)
                    if amt <= 0: continue
                    
                    if is_negative: amt = -amt
                    
                    if idate > d:
                        j = bisect.bisect_right(ddates, d) - 1
                        eff = ddates[j] if j >= 0 else d
                        age = (d - eff).days
                    else:
                        age = (d - idate).days
                    
                    rep_results[r_code]["b"][bucket_of(age)] += amt

    # Add cash sales
    if inc_cash:
        for r_code, c_sales in cash_sales_by_rep.items():
            if rep_code and r_code != rep_code: continue
            if c_sales > 0:
                rep_results[r_code]["total"] += c_sales
                rep_results[r_code]["b"][0] += c_sales

    cols = ["كود المندوب", "اسم المندوب", "عدد العملاء", "0-30", "31-60", "61-90", "91-120", "أكثر من 120", "المبلغ المحصل"]
    rows = []
    
    for r_code, data in rep_results.items():
        # Avoid showing empty rows if net collection is 0 and buckets are 0
        if round(data["total"], 2) == 0 and sum(abs(x) for x in data["b"]) < 0.01: continue
        row = (
            r_code,
            rep_name.get(r_code, r_code),
            len(data["cust_count"]),
            f"{data['b'][0]:,.2f}",
            f"{data['b'][1]:,.2f}",
            f"{data['b'][2]:,.2f}",
            f"{data['b'][3]:,.2f}",
            f"{data['b'][4]:,.2f}",
            f"{data['total']:,.2f}"
        )
        rows.append(row)
        
    rows.sort(key=lambda x: float(x[8].replace(',','')), reverse=True)
    return cols, rows

def run_main_wh_movement(rpt, args):
    from collections import defaultdict
    date_from_str = args.get("date_from", "2026-01-01")
    date_to_str = args.get("date_to", "2026-12-31")
    i_code_str = args.get("i_code", "").split(" - ")[0].strip()
    
    print(f"[DEBUG WH] date_from: {date_from_str}, date_to: {date_to_str}, i_code: {i_code_str}")
    
    wh_mapping = {
        "105": "مخزن عيضة",
        "103": "مخزن حسام",
        "121": "مخزن المنصورية",
        "122": "مخزن الدمام",
        "118": "مخزن تبوك",
        "108": "مخزن الجنوب",
        "119": "مخزن جده"
    }
    
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                codes_str = ",".join(MAIN_WAREHOUSES_CODES)
                cur.execute(f"SELECT W_CODE, W_NAME FROM IAS20261.WAREHOUSE_DETAILS WHERE W_CODE IN ({codes_str})")
                for w_code, w_name in cur.fetchall():
                    wh_mapping[str(w_code)] = w_name
    except Exception as e:
        print("Error fetching warehouse names dynamically:", e)

    wh_codes = MAIN_WAREHOUSES_CODES
    
    item_filter = ""
    if i_code_str:
        item_filter = " AND dt.I_CODE = :icode "
    
    sql = f"""
        SELECT
            dt.I_CODE,
            MAX(m.I_NAME),
            dt.W_CODE,
            SUM(NVL(dt.I_QTY, 0)) AS net_qty
        FROM IAS20261.ITEM_MOVEMENT dt
        LEFT JOIN IAS20261.IAS_ITM_MST m ON m.I_CODE = dt.I_CODE
        WHERE dt.I_DATE >= TO_DATE(:df, 'YYYY-MM-DD')
          AND dt.I_DATE < TO_DATE(:dt, 'YYYY-MM-DD') + 1
          AND dt.W_CODE IN (105, 103, 121, 122, 118, 108, 119)
          AND dt.IN_OUT = -1
          {item_filter}
        GROUP BY dt.I_CODE, dt.W_CODE
        HAVING SUM(NVL(dt.I_QTY, 0)) > 0
    """
    
    params = {"df": date_from_str, "dt": date_to_str}
    if i_code_str:
        params["icode"] = i_code_str
    
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute(sql, params)
            results = cur.fetchall()
            print(f"[DEBUG WH] Query returned {len(results)} raw grouped rows.")
            
    items = defaultdict(lambda: {"name": "", "total": 0, "wh": defaultdict(float)})
    for i_code, i_name, w_code, net_qty in results:
        code_str = str(w_code)
        items[str(i_code)]["name"] = str(i_name)
        items[str(i_code)]["total"] += float(net_qty)
        items[str(i_code)]["wh"][code_str] += float(net_qty)
        
    cols = ["كود الصنف", "اسم الصنف", "الإجمالي"] + [wh_mapping[c] for c in wh_codes]
    rows = []
    for code, data in items.items():
        row = [code, data["name"], f"{data['total']:,.2f}"]
        for w_code in wh_codes:
            row.append(f"{data['wh'][w_code]:,.2f}")
        rows.append(tuple(row))
        
    rows.sort(key=lambda x: float(x[2].replace(',', '')), reverse=True)
    return cols, rows[:300]

