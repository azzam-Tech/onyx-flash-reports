import re

file_path = 'privet/onyx_reports/reports_config.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_report = '''{"id":"warehouse_rebalancing","title":"إعادة التوازن (نقل المخزون لتفادي الشراء)","params":[{"name":"as_of","label":"إلى تاريخ","type":"date","default":"2026-07-31"},{"name":"i_code","label":"رقم الصنف (اختياري)","type":"text","default":""}],"sql":"""
        WITH wh_stock AS (
            SELECT mv.I_CODE, mv.W_CODE,
                   SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) as qty
            FROM IAS20261.ITEM_MOVEMENT mv
            WHERE mv.W_CODE IN ('105', '103', '121', '122', '118', '108', '119')
              AND mv.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1
            GROUP BY mv.I_CODE, mv.W_CODE
        ),
        item_matrix AS (
            SELECT I_CODE,
                   SUM(CASE WHEN W_CODE = '105' THEN qty ELSE 0 END) as w_105,
                   SUM(CASE WHEN W_CODE = '103' THEN qty ELSE 0 END) as w_103,
                   SUM(CASE WHEN W_CODE = '121' THEN qty ELSE 0 END) as w_121,
                   SUM(CASE WHEN W_CODE = '122' THEN qty ELSE 0 END) as w_122,
                   SUM(CASE WHEN W_CODE = '118' THEN qty ELSE 0 END) as w_118,
                   SUM(CASE WHEN W_CODE = '108' THEN qty ELSE 0 END) as w_108,
                   SUM(CASE WHEN W_CODE = '119' THEN qty ELSE 0 END) as w_119,
                   MAX(qty) as max_qty,
                   MIN(qty) as min_qty,
                   SUM(qty) as tot_qty
            FROM wh_stock
            GROUP BY I_CODE
            HAVING SUM(qty) > 0
        )
        SELECT m.I_CODE AS "رمز الصنف",
               i.I_NAME AS "اسم الصنف",
               TO_CHAR(m.tot_qty, 'FM999,999,990') AS "إجمالي الأرصدة (كل الفروع)",
               TO_CHAR(m.w_103, 'FM999,999,990') AS "الرياض (103)",
               TO_CHAR(m.w_121, 'FM999,999,990') AS "جدة (121)",
               TO_CHAR(m.w_122, 'FM999,999,990') AS "الدمام (122)",
               TO_CHAR(m.w_105, 'FM999,999,990') AS "خميس مشيط (105)",
               TO_CHAR(m.w_118, 'FM999,999,990') AS "بريدة (118)",
               TO_CHAR(m.w_119, 'FM999,999,990') AS "تبوك (119)",
               TO_CHAR(m.w_108, 'FM999,999,990') AS "مستودع المرتجعات (108)"
        FROM item_matrix m
        JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE = m.I_CODE
        WHERE m.min_qty = 0 AND m.max_qty > 0
          AND (:i_code IS NULL OR m.I_CODE = :i_code)
        ORDER BY m.tot_qty DESC
      """},
      '''

# Find the stock tab and its reports array
pattern = r'(\{"id":"stock","title":"[^"]+","icon":"[^"]+","reports":\[)'

def replacer(match):
    return match.group(1) + "\n      " + new_report

content = re.sub(pattern, replacer, content, count=1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Warehouse Rebalancing report added to reports_config.py!")
