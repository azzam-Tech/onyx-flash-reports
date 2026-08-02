# -*- coding: utf-8 -*-
import re

with open('app.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update BTYPE
old_btype = r'BTYPE = \{"name":"bill_type","label":"نوع البيع","type":"select","default":"",\s+"options":\[\["","الكل"\],\["1","نقدي"\],\["4","آجل"\]\]\}'
new_btype = '''BTYPE = {"name":"bill_type","label":"نوع المستند","type":"select","default":"",
         "options":[["","الكل"],["1","مبيعات نقدية"],["4","مبيعات آجلة"],["2","مرتجع نقدي"],["5","مرتجع آجل"]]}'''
text = re.sub(old_btype, new_btype, text)

# 2. Update bills report
old_bills_regex = r'\{\"id\"\:\"bills\".*?FETCH FIRST 300 ROWS ONLY\"\"\"\}'
new_bills = '''{"id":"bills","title":"فواتير المبيعات","params":[DFROM,DTO,BTYPE,REP,CST],"sql":"""
     SELECT CASE b.BILL_DOC_TYPE WHEN 1 THEN 'مبيعات نقدية' WHEN 4 THEN 'مبيعات آجلة' 
                 WHEN 2 THEN 'مرتجع نقدي' WHEN 5 THEN 'مرتجع آجل' ELSE 'أخرى' END AS "نوع المستند",
            b.BILL_NO AS "رقم الفاتورة", TO_CHAR(b.BILL_DATE,'YYYY-MM-DD') AS "التاريخ",
            b.C_CODE AS "كود العميل", MAX(c.C_A_NAME) AS "اسم العميل", b.REP_CODE AS "المندوب",
            TO_CHAR(NVL(b.BILL_AMT,0),'FM999,999,990.00') AS "المبلغ",
            TO_CHAR(NVL(b.DISC_AMT,0),'FM999,999,990.00') AS "الخصم",
            TO_CHAR(NVL(b.VAT_AMT,0),'FM999,999,990.00') AS "الضريبة",
            TO_CHAR((NVL(b.BILL_AMT,0)-NVL(b.DISC_AMT,0)+NVL(b.VAT_AMT,0)+NVL(b.OTHR_AMT,0)) * CASE WHEN b.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 1 END,'FM999,999,990.00') AS "الصافي",
            CASE NVL(b.BILL_POST,0) WHEN 1 THEN 'مرحّلة' ELSE 'غير مرحّلة' END AS "الحالة"
     FROM IAS20261.IAS_BILL_MST b
     LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = b.C_CODE
     WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       AND b.BILL_DOC_TYPE IN (1,4,2,5)
       AND (:bill_type IS NULL OR b.BILL_DOC_TYPE = :bill_type)
       AND (:rep_code IS NULL OR b.REP_CODE = :rep_code)
       AND (:c_code IS NULL OR b.C_CODE = :c_code)
     GROUP BY b.BILL_DOC_TYPE, b.BILL_NO, b.BILL_DATE, b.C_CODE, b.REP_CODE, b.BILL_AMT, b.DISC_AMT, b.VAT_AMT, b.OTHR_AMT, b.BILL_POST
     ORDER BY b.BILL_DATE DESC, b.BILL_NO DESC FETCH FIRST 300 ROWS ONLY"""}'''
text = re.sub(old_bills_regex, new_bills, text, flags=re.DOTALL)

# 3. Update by_customer report
old_cust_regex = r'\{\"id\"\:\"by_customer\".*?FETCH FIRST 300 ROWS ONLY\"\"\"\}'
new_cust = '''{"id":"by_customer","title":"حسب العميل","params":[DFROM,DTO],"sql":"""
     WITH s AS (
       SELECT C_CODE, REP_CODE,
              CASE WHEN BILL_DOC_TYPE IN (1,4) THEN 1 ELSE 0 END as is_sale,
              CASE WHEN BILL_DOC_TYPE IN (2,5) THEN 1 ELSE 0 END as is_ret,
              CASE WHEN BILL_DOC_TYPE IN (1,4) THEN 1 WHEN BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              NVL(BILL_AMT,0) amt, NVL(DISC_AMT,0) disc, NVL(VAT_AMT,0) vat, NVL(OTHR_AMT,0) othr
       FROM IAS20261.IAS_BILL_MST
       WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND BILL_DOC_TYPE IN (1,4,2,5)
     )
     SELECT s.C_CODE AS "كود العميل", MAX(c.C_A_NAME) AS "اسم العميل", MAX(s.REP_CODE) AS "المندوب",
            SUM(s.is_sale) AS "فواتير مبيعات",
            SUM(s.is_ret) AS "فواتير مرتجعات",
            TO_CHAR(SUM(s.amt * s.is_sale),'FM999,999,999,990.00') AS "المبيعات",
            TO_CHAR(SUM(s.amt * s.is_ret),'FM999,999,999,990.00') AS "المردودات (-)",
            TO_CHAR(SUM(s.disc * s.sign),'FM999,999,999,990.00') AS "الخصم (-)",
            TO_CHAR(SUM((s.amt - s.disc) * s.sign),'FM999,999,999,990.00') AS "الصافي قبل الضريبة",
            TO_CHAR(SUM((s.amt - s.disc + s.vat + s.othr) * s.sign),'FM999,999,999,990.00') AS "الإجمالي بالضريبة"
     FROM s LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE=s.C_CODE
     WHERE s.C_CODE IS NOT NULL
     GROUP BY s.C_CODE 
     ORDER BY SUM((s.amt - s.disc) * s.sign) DESC 
     FETCH FIRST 300 ROWS ONLY"""}'''
text = re.sub(old_cust_regex, new_cust, text, flags=re.DOTALL)

# 4. Update by_salesman report
old_rep_regex = r'\{\"id\"\:\"by_salesman\".*?FETCH FIRST 300 ROWS ONLY\"\"\"\}'
new_rep = '''{"id":"by_salesman","title":"حسب المندوب","params":[DFROM,DTO],"sql":"""
     WITH s AS (
       SELECT REP_CODE, C_CODE,
              CASE WHEN BILL_DOC_TYPE IN (1,4) THEN 1 ELSE 0 END as is_sale,
              CASE WHEN BILL_DOC_TYPE IN (2,5) THEN 1 ELSE 0 END as is_ret,
              CASE WHEN BILL_DOC_TYPE IN (1,4) THEN 1 WHEN BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              NVL(BILL_AMT,0) amt, NVL(DISC_AMT,0) disc, NVL(VAT_AMT,0) vat, NVL(OTHR_AMT,0) othr
       FROM IAS20261.IAS_BILL_MST
       WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND BILL_DOC_TYPE IN (1,4,2,5)
     )
     SELECT s.REP_CODE AS "كود المندوب", MAX(sm.REPRS_A_NAME) AS "اسم المندوب",
            COUNT(DISTINCT s.C_CODE) AS "عدد العملاء",
            SUM(s.is_sale) AS "فواتير مبيعات",
            SUM(s.is_ret) AS "فواتير مرتجعات",
            TO_CHAR(SUM(s.amt * s.is_sale),'FM999,999,999,990.00') AS "المبيعات",
            TO_CHAR(SUM(s.amt * s.is_ret),'FM999,999,999,990.00') AS "المردودات (-)",
            TO_CHAR(SUM(s.disc * s.sign),'FM999,999,999,990.00') AS "الخصم (-)",
            TO_CHAR(SUM((s.amt - s.disc) * s.sign),'FM999,999,999,990.00') AS "الصافي قبل الضريبة",
            TO_CHAR(SUM((s.amt - s.disc + s.vat + s.othr) * s.sign),'FM999,999,999,990.00') AS "الإجمالي بالضريبة"
     FROM s LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=s.REP_CODE
     WHERE s.REP_CODE IS NOT NULL
     GROUP BY s.REP_CODE 
     ORDER BY SUM((s.amt - s.disc) * s.sign) DESC 
     FETCH FIRST 300 ROWS ONLY"""}'''
text = re.sub(old_rep_regex, new_rep, text, flags=re.DOTALL)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Sales reports patched successfully!")
