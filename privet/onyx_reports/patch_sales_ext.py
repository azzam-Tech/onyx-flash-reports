# -*- coding: utf-8 -*-
import re

with open('app.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Update by_customer report
old_cust_regex = r'\{\"id\"\:\"by_customer\".*?FETCH FIRST 300 ROWS ONLY\"\"\"\}'
new_cust = '''{"id":"by_customer","title":"حسب العميل","params":[DFROM,DTO],"sql":"""
     WITH s AS (
       SELECT C_CODE, REP_CODE,
              CASE WHEN BILL_DOC_TYPE IN (1,4) THEN 1 ELSE 0 END as is_sale,
              CASE WHEN BILL_DOC_TYPE IN (2,5) THEN 1 ELSE 0 END as is_ret,
              CASE WHEN BILL_DOC_TYPE IN (1,4) THEN 1 WHEN BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              NVL(BILL_AMT,0) amt, NVL(DISC_AMT,0) disc, 0 as ext_disc, NVL(VAT_AMT,0) vat, NVL(OTHR_AMT,0) othr
       FROM IAS20261.IAS_BILL_MST
       WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND BILL_DOC_TYPE IN (1,4,2,5)
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
            TO_CHAR(SUM(s.disc * s.sign),'FM999,999,999,990.00') AS "خصم الفواتير (-)",
            TO_CHAR(SUM(s.ext_disc),'FM999,999,999,990.00') AS "إشعار خصم مستقل (-)",
            TO_CHAR(SUM((s.amt - s.disc) * s.sign) - SUM(s.ext_disc),'FM999,999,999,990.00') AS "الصافي قبل الضريبة",
            TO_CHAR(SUM((s.amt - s.disc + s.vat + s.othr) * s.sign) - SUM(s.ext_disc),'FM999,999,999,990.00') AS "الإجمالي بالضريبة"
     FROM s LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE=s.C_CODE
     WHERE s.C_CODE IS NOT NULL
     GROUP BY s.C_CODE 
     ORDER BY SUM((s.amt - s.disc) * s.sign) - SUM(s.ext_disc) DESC 
     FETCH FIRST 300 ROWS ONLY"""}'''
text = re.sub(old_cust_regex, new_cust, text, flags=re.DOTALL)

# Update by_salesman report
old_rep_regex = r'\{\"id\"\:\"by_salesman\".*?FETCH FIRST 300 ROWS ONLY\"\"\"\}'
new_rep = '''{"id":"by_salesman","title":"حسب المندوب","params":[DFROM,DTO],"sql":"""
     WITH s AS (
       SELECT REP_CODE, C_CODE,
              CASE WHEN BILL_DOC_TYPE IN (1,4) THEN 1 ELSE 0 END as is_sale,
              CASE WHEN BILL_DOC_TYPE IN (2,5) THEN 1 ELSE 0 END as is_ret,
              CASE WHEN BILL_DOC_TYPE IN (1,4) THEN 1 WHEN BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              NVL(BILL_AMT,0) amt, NVL(DISC_AMT,0) disc, 0 as ext_disc, NVL(VAT_AMT,0) vat, NVL(OTHR_AMT,0) othr
       FROM IAS20261.IAS_BILL_MST
       WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND BILL_DOC_TYPE IN (1,4,2,5)
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
            TO_CHAR(SUM(s.disc * s.sign),'FM999,999,999,990.00') AS "خصم الفواتير (-)",
            TO_CHAR(SUM(s.ext_disc),'FM999,999,999,990.00') AS "إشعار خصم مستقل (-)",
            TO_CHAR(SUM((s.amt - s.disc) * s.sign) - SUM(s.ext_disc),'FM999,999,999,990.00') AS "الصافي قبل الضريبة",
            TO_CHAR(SUM((s.amt - s.disc + s.vat + s.othr) * s.sign) - SUM(s.ext_disc),'FM999,999,999,990.00') AS "الإجمالي بالضريبة"
     FROM s LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=s.REP_CODE
     WHERE s.REP_CODE IS NOT NULL
     GROUP BY s.REP_CODE 
     ORDER BY SUM((s.amt - s.disc) * s.sign) - SUM(s.ext_disc) DESC 
     FETCH FIRST 300 ROWS ONLY"""}'''
text = re.sub(old_rep_regex, new_rep, text, flags=re.DOTALL)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("External notices added to sales reports successfully!")
