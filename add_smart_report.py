import re

file_path = 'privet/onyx_reports/reports_config.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_report = '''{"id":"smart_replenishment","title":"ذكاء المشتريات (تغطية المخزون)","params":[{"name":"as_of","label":"إلى تاريخ","type":"date","default":"2026-07-31"},{"name":"days","label":"فترة سحب المبيعات (أيام)","type":"number","default":"90"}],"sql":"""
        WITH stock AS (
            SELECT mv.I_CODE, 
                   MAX(i.I_NAME) as I_NAME,
                   SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) as current_qty
            FROM IAS20261.ITEM_MOVEMENT mv
            LEFT JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE = mv.I_CODE
            WHERE mv.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1
            GROUP BY mv.I_CODE
            HAVING SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) > 0
        ),
        sales AS (
            SELECT I_CODE, 
                   SUM(CASE WHEN IN_OUT = -1 AND DOC_TYPE IN (1, 7) THEN NVL(I_QTY,0) 
                            WHEN IN_OUT = 1 AND DOC_TYPE = 3 THEN -NVL(I_QTY,0) 
                            ELSE 0 END) as sold_qty
            FROM IAS20261.ITEM_MOVEMENT
            WHERE I_DATE >= TO_DATE(:as_of,'YYYY-MM-DD') - :days 
              AND I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1
            GROUP BY I_CODE
        )
        SELECT s.I_CODE AS "رمز الصنف", 
               s.I_NAME AS "اسم الصنف",
               TO_CHAR(s.current_qty, 'FM999,999,990.00') AS "الرصيد الحالي",
               TO_CHAR(NVL(sa.sold_qty, 0), 'FM999,999,990.00') AS "إجمالي السحب",
               TO_CHAR(NVL(sa.sold_qty, 0) / :days, 'FM999,999,990.00') AS "متوسط السحب اليومي",
               CASE WHEN NVL(sa.sold_qty, 0) > 0 THEN
                  TO_CHAR(s.current_qty / (sa.sold_qty / :days), 'FM999,999,990')
               ELSE 'ركود تام' END AS "أيام التغطية المتبقية",
               CASE 
                  WHEN NVL(sa.sold_qty, 0) <= 0 THEN 'مكدس (لا يوجد سحب)'
                  WHEN (s.current_qty / (sa.sold_qty / :days)) < 15 THEN 'حرج (شراء فوري)'
                  WHEN (s.current_qty / (sa.sold_qty / :days)) <= 60 THEN 'مستقر'
                  ELSE 'مكدس (فائض)'
               END AS "حالة الصنف"
        FROM stock s
        LEFT JOIN sales sa ON sa.I_CODE = s.I_CODE
        ORDER BY 
            CASE 
               WHEN NVL(sa.sold_qty, 0) <= 0 THEN 999999
               ELSE s.current_qty / (sa.sold_qty / :days) 
            END ASC
        """},
      '''

# Find the stock tab and its reports array
pattern = r'(\{"id":"stock","title":"[^"]+","icon":"[^"]+","reports":\[)'

def replacer(match):
    return match.group(1) + "\n      " + new_report

content = re.sub(pattern, replacer, content, count=1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Smart Replenishment report added to reports_config.py!")
