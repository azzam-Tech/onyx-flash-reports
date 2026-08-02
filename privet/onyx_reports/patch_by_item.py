# -*- coding: utf-8 -*-
import re

with open('app.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_item_regex = r'\{\"id\"\:\"by_item\".*?FETCH FIRST 300 ROWS ONLY\"\"\"\}'
new_item = '''{"id":"by_item","title":"حسب الصنف","params":[DFROM,DTO],"sql":"""
     WITH dt AS (
       SELECT dt.I_CODE,
              CASE WHEN b.BILL_DOC_TYPE IN (1,4) THEN 1 WHEN b.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
              NVL(dt.I_QTY,0) as qty,
              (NVL(dt.I_QTY,0) * NVL(dt.I_PRICE,0) - NVL(dt.DIS_AMT,0)) as item_net,
              CASE WHEN NVL(b.BILL_AMT,0) = 0 THEN 0 ELSE 
                ((NVL(dt.I_QTY,0) * NVL(dt.I_PRICE,0) - NVL(dt.DIS_AMT,0)) / b.BILL_AMT) * NVL(b.DISC_AMT,0) 
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
     FETCH FIRST 300 ROWS ONLY"""}'''

text = re.sub(old_item_regex, new_item, text, flags=re.DOTALL)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("by_item report patched successfully!")
