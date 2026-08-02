import codecs
import re

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", 'r', 'utf-8') as f:
    content = f.read()

target_sql = """      inv_cogs_ret AS (
        SELECT 
            '31103' as acc_code,
            0 as op_dr,
            SUM(CASE WHEN r.RT_BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(im.I_QTY,0) * NVL(im.STK_COST,0) ELSE 0 END) as op_cr,
            0 as mv_dr,
            SUM(CASE WHEN r.RT_BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(im.I_QTY,0) * NVL(im.STK_COST,0) ELSE 0 END) as mv_cr
        FROM IAS20261.ITEM_MOVEMENT im
        JOIN IAS20261.IAS_RT_BILL_MST r
          ON r.RT_BILL_DOC_TYPE = im.BILL_DOC_TYPE 
         AND r.RT_BILL_NO = im.DOC_NO 
         AND r.RT_BILL_SER = im.DOC_SER
        WHERE (:rep_code IS NULL OR r.REP_CODE = :rep_code)
          AND im.DOC_TYPE = 2
          AND NVL(im.I_QTY,0) > 0
      ),
      all_data AS (
        SELECT * FROM gl_base
        UNION ALL
        SELECT * FROM inv_cogs
        UNION ALL
        SELECT * FROM inv_cogs_ret
      )"""

replacement_sql = """      inv_cogs_ret AS (
        SELECT 
            '31103' as acc_code,
            0 as op_dr,
            SUM(CASE WHEN r.RT_BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(im.I_QTY,0) * NVL(im.STK_COST,0) ELSE 0 END) as op_cr,
            0 as mv_dr,
            SUM(CASE WHEN r.RT_BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(im.I_QTY,0) * NVL(im.STK_COST,0) ELSE 0 END) as mv_cr
        FROM IAS20261.ITEM_MOVEMENT im
        JOIN IAS20261.IAS_RT_BILL_MST r
          ON r.RT_BILL_DOC_TYPE = im.BILL_DOC_TYPE 
         AND r.RT_BILL_NO = im.DOC_NO 
         AND r.RT_BILL_SER = im.DOC_SER
        WHERE (:rep_code IS NULL OR r.REP_CODE = :rep_code)
          AND im.DOC_TYPE = 3
          AND r.PREV_YEAR IS NULL
          AND NVL(im.I_QTY,0) > 0
      ),
      inv_cogs_ret_prev AS (
        SELECT 
            '31106' as acc_code,
            0 as op_dr,
            SUM(CASE WHEN r.RT_BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(im.I_QTY,0) * NVL(im.STK_COST,0) ELSE 0 END) as op_cr,
            0 as mv_dr,
            SUM(CASE WHEN r.RT_BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(im.I_QTY,0) * NVL(im.STK_COST,0) ELSE 0 END) as mv_cr
        FROM IAS20261.ITEM_MOVEMENT im
        JOIN IAS20261.IAS_RT_BILL_MST r
          ON r.RT_BILL_DOC_TYPE = im.BILL_DOC_TYPE 
         AND r.RT_BILL_NO = im.DOC_NO 
         AND r.RT_BILL_SER = im.DOC_SER
        WHERE (:rep_code IS NULL OR r.REP_CODE = :rep_code)
          AND im.DOC_TYPE = 3
          AND r.PREV_YEAR IS NOT NULL
          AND NVL(im.I_QTY,0) > 0
      ),
      all_data AS (
        SELECT * FROM gl_base
        UNION ALL
        SELECT * FROM inv_cogs
        UNION ALL
        SELECT * FROM inv_cogs_ret
        UNION ALL
        SELECT * FROM inv_cogs_ret_prev
      )"""

if target_sql in content:
    content = content.replace(target_sql, replacement_sql)
    with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", 'w', 'utf-8') as f:
        f.write(content)
    print("Updated successfully.")
else:
    print("Target SQL not found!")
