import re

file_path = 'privet/onyx_reports/reports_config.py'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_report = '''
    {"id":"detailed_stock_pivot","title":"تقرير المخزون التفصيلي والمجموعات (مجمع 7 مخازن)","params":[DFROM,DTO],"sql":"""
        WITH item_groups AS (
            SELECT 
                m.I_CODE,
                MAX(m.I_NAME) AS I_NAME,
                MAX(gd.G_A_NAME) AS main_grp,
                MAX(mg.MNG_A_NAME) AS sub_main_grp,
                MAX(sg.SUBG_A_NAME) AS sub_grp,
                MAX(dg.DETAIL_A_NAME) AS dtl_grp
            FROM IAS20261.IAS_ITM_MST m
            LEFT JOIN IAS20261.GROUP_DETAILS gd ON gd.G_CODE = m.G_CODE
            LEFT JOIN IAS20261.IAS_MAINSUB_GRP_DTL mg ON mg.MNG_CODE = m.MNG_CODE AND mg.G_CODE = m.G_CODE
            LEFT JOIN IAS20261.IAS_SUB_GRP_DTL sg ON sg.SUBG_CODE = m.SUBG_CODE AND sg.MNG_CODE = m.MNG_CODE AND sg.G_CODE = m.G_CODE
            LEFT JOIN IAS20261.IAS_DETAIL_GROUP dg ON dg.DET_I_CODE = m.DETAIL_NO AND dg.SUBG_CODE = m.SUBG_CODE AND dg.MNG_CODE = m.MNG_CODE AND dg.G_CODE = m.G_CODE
            GROUP BY m.I_CODE
        ),
        inventory_mov AS (
            SELECT 
                I_CODE,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 105 THEN NVL(I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_105,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 103 THEN NVL(I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_103,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 121 THEN NVL(I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_121,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 122 THEN NVL(I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_122,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 118 THEN NVL(I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_118,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 108 THEN NVL(I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_108,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 119 THEN NVL(I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_119,
                
                SUM(CASE WHEN I_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND IN_OUT = -1 THEN NVL(I_QTY,0) ELSE 0 END) as sales_qty,
                SUM(CASE WHEN I_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND IN_OUT = 1 THEN NVL(I_QTY,0) ELSE 0 END) as pur_qty,
                
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 105 THEN NVL(I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_105,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 103 THEN NVL(I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_103,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 121 THEN NVL(I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_121,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 122 THEN NVL(I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_122,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 118 THEN NVL(I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_118,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 108 THEN NVL(I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_108,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 119 THEN NVL(I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_119
            FROM IAS20261.ITEM_MOVEMENT
            WHERE W_CODE IN (105, 103, 121, 122, 118, 108, 119)
            GROUP BY I_CODE
        )
        SELECT 
            ig.main_grp AS "المجموعة الرئيسية",
            ig.sub_main_grp AS "الفرعية",
            ig.sub_grp AS "تحت الفرعية",
            ig.dtl_grp AS "التفصيلية",
            ig.I_CODE AS "رقم الصنف",
            ig.I_NAME AS "اسم الصنف",
            
            TO_CHAR(NVL(im.op_bal_105, 0), 'FM999,999,990.00') AS "افتتاحي 105",
            TO_CHAR(NVL(im.op_bal_103, 0), 'FM999,999,990.00') AS "افتتاحي 103",
            TO_CHAR(NVL(im.op_bal_121, 0), 'FM999,999,990.00') AS "افتتاحي 121",
            TO_CHAR(NVL(im.op_bal_122, 0), 'FM999,999,990.00') AS "افتتاحي 122",
            TO_CHAR(NVL(im.op_bal_118, 0), 'FM999,999,990.00') AS "افتتاحي 118",
            TO_CHAR(NVL(im.op_bal_108, 0), 'FM999,999,990.00') AS "افتتاحي 108",
            TO_CHAR(NVL(im.op_bal_119, 0), 'FM999,999,990.00') AS "افتتاحي 119",
            
            TO_CHAR(NVL(im.sales_qty, 0), 'FM999,999,990.00') AS "صادر (مبيعات/تحويل)",
            TO_CHAR(NVL(im.pur_qty, 0), 'FM999,999,990.00') AS "وارد (مشتريات/استرجاع)",
            
            TO_CHAR(NVL(im.end_bal_105, 0), 'FM999,999,990.00') AS "نهائي 105",
            TO_CHAR(NVL(im.end_bal_103, 0), 'FM999,999,990.00') AS "نهائي 103",
            TO_CHAR(NVL(im.end_bal_121, 0), 'FM999,999,990.00') AS "نهائي 121",
            TO_CHAR(NVL(im.end_bal_122, 0), 'FM999,999,990.00') AS "نهائي 122",
            TO_CHAR(NVL(im.end_bal_118, 0), 'FM999,999,990.00') AS "نهائي 118",
            TO_CHAR(NVL(im.end_bal_108, 0), 'FM999,999,990.00') AS "نهائي 108",
            TO_CHAR(NVL(im.end_bal_119, 0), 'FM999,999,990.00') AS "نهائي 119"
            
        FROM item_groups ig
        JOIN inventory_mov im ON ig.I_CODE = im.I_CODE
        WHERE NVL(im.op_bal_105,0) <> 0 OR NVL(im.op_bal_103,0) <> 0 OR NVL(im.op_bal_121,0) <> 0 OR NVL(im.op_bal_122,0) <> 0 OR NVL(im.op_bal_118,0) <> 0 OR NVL(im.op_bal_108,0) <> 0 OR NVL(im.op_bal_119,0) <> 0
           OR NVL(im.sales_qty,0) <> 0 OR NVL(im.pur_qty,0) <> 0
           OR NVL(im.end_bal_105,0) <> 0 OR NVL(im.end_bal_103,0) <> 0 OR NVL(im.end_bal_121,0) <> 0 OR NVL(im.end_bal_122,0) <> 0 OR NVL(im.end_bal_118,0) <> 0 OR NVL(im.end_bal_108,0) <> 0 OR NVL(im.end_bal_119,0) <> 0
        ORDER BY ig.main_grp, ig.I_CODE
    """},
'''

pattern = r'(\{"id"\s*:\s*"stock"[^\[]*"reports"\s*:\s*\[)'

if re.search(pattern, content):
    content = re.sub(pattern, r'\1' + new_report, content)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Report patched successfully.")
else:
    print("Could not find the stock tab.")
