import re

file_path = 'privet/onyx_reports/reports_config.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_block = """        inventory_mov AS (
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
        )"""

new_block = """        inventory_mov AS (
            SELECT 
                dt.I_CODE,
                SUM(CASE WHEN dt.I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND dt.W_CODE = 105 THEN NVL(dt.I_QTY,0) * NVL(dt.IN_OUT,1) ELSE 0 END) as op_bal_105,
                SUM(CASE WHEN dt.I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND dt.W_CODE = 103 THEN NVL(dt.I_QTY,0) * NVL(dt.IN_OUT,1) ELSE 0 END) as op_bal_103,
                SUM(CASE WHEN dt.I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND dt.W_CODE = 121 THEN NVL(dt.I_QTY,0) * NVL(dt.IN_OUT,1) ELSE 0 END) as op_bal_121,
                SUM(CASE WHEN dt.I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND dt.W_CODE = 122 THEN NVL(dt.I_QTY,0) * NVL(dt.IN_OUT,1) ELSE 0 END) as op_bal_122,
                SUM(CASE WHEN dt.I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND dt.W_CODE = 118 THEN NVL(dt.I_QTY,0) * NVL(dt.IN_OUT,1) ELSE 0 END) as op_bal_118,
                SUM(CASE WHEN dt.I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND dt.W_CODE = 108 THEN NVL(dt.I_QTY,0) * NVL(dt.IN_OUT,1) ELSE 0 END) as op_bal_108,
                SUM(CASE WHEN dt.I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND dt.W_CODE = 119 THEN NVL(dt.I_QTY,0) * NVL(dt.IN_OUT,1) ELSE 0 END) as op_bal_119,
                
                SUM(CASE WHEN dt.I_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND dt.I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND dt.IN_OUT = -1 
                  AND NOT EXISTS (
                    SELECT 1 FROM IAS20261.ITEM_MOVEMENT t2 
                    WHERE t2.DOC_NO = dt.DOC_NO AND t2.DOC_SER = dt.DOC_SER AND t2.I_CODE = dt.I_CODE AND t2.IN_OUT = 1 
                    AND t2.W_CODE IN (105, 103, 121, 122, 118, 108, 119)
                  ) THEN NVL(dt.I_QTY,0) ELSE 0 END) as sales_qty,
                  
                SUM(CASE WHEN dt.I_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND dt.I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND dt.IN_OUT = 1 
                  AND NOT EXISTS (
                    SELECT 1 FROM IAS20261.ITEM_MOVEMENT t2 
                    WHERE t2.DOC_NO = dt.DOC_NO AND t2.DOC_SER = dt.DOC_SER AND t2.I_CODE = dt.I_CODE AND t2.IN_OUT = -1 
                    AND t2.W_CODE IN (105, 103, 121, 122, 118, 108, 119)
                  ) THEN NVL(dt.I_QTY,0) ELSE 0 END) as pur_qty,
                
                SUM(CASE WHEN dt.I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND dt.W_CODE = 105 THEN NVL(dt.I_QTY,0) * NVL(dt.IN_OUT,1) ELSE 0 END) as end_bal_105,
                SUM(CASE WHEN dt.I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND dt.W_CODE = 103 THEN NVL(dt.I_QTY,0) * NVL(dt.IN_OUT,1) ELSE 0 END) as end_bal_103,
                SUM(CASE WHEN dt.I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND dt.W_CODE = 121 THEN NVL(dt.I_QTY,0) * NVL(dt.IN_OUT,1) ELSE 0 END) as end_bal_121,
                SUM(CASE WHEN dt.I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND dt.W_CODE = 122 THEN NVL(dt.I_QTY,0) * NVL(dt.IN_OUT,1) ELSE 0 END) as end_bal_122,
                SUM(CASE WHEN dt.I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND dt.W_CODE = 118 THEN NVL(dt.I_QTY,0) * NVL(dt.IN_OUT,1) ELSE 0 END) as end_bal_118,
                SUM(CASE WHEN dt.I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND dt.W_CODE = 108 THEN NVL(dt.I_QTY,0) * NVL(dt.IN_OUT,1) ELSE 0 END) as end_bal_108,
                SUM(CASE WHEN dt.I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND dt.W_CODE = 119 THEN NVL(dt.I_QTY,0) * NVL(dt.IN_OUT,1) ELSE 0 END) as end_bal_119
            FROM IAS20261.ITEM_MOVEMENT dt
            WHERE dt.W_CODE IN (105, 103, 121, 122, 118, 108, 119)
            GROUP BY dt.I_CODE
        )"""

content = content.replace(old_block, new_block)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("reports_config.py patched successfully.")
