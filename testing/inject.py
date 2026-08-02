import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", 'r', 'utf-8') as f:
    content = f.read()

report_code = """
    {"id":"true_income_statement","title":"قائمة الدخل الحقيقي (تكلفة المخزون)","params":[DFROM,DTO,REP],"sql":\"\"\"
      WITH gl_base AS (
        SELECT 
            SUBSTR(AC_CODE_DTL, 1, 5) as acc_code,
            SUM(CASE WHEN DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(DR_AMT,0) ELSE 0 END) as op_dr,
            SUM(CASE WHEN DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(CR_AMT,0) ELSE 0 END) as op_cr,
            SUM(CASE WHEN DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(DR_AMT,0) ELSE 0 END) as mv_dr,
            SUM(CASE WHEN DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(CR_AMT,0) ELSE 0 END) as mv_cr
        FROM IAS20261.IAS_POST_DTL
        WHERE (:rep_code IS NULL OR REP_CODE = :rep_code)
          AND NVL(DOC_POST,0)=1
          AND SUBSTR(AC_CODE_DTL, 1, 5) IN (
              '31102','31104','31105','31109','31110',
              '32101','32201','32401','32801',
              '41101','41202'
          )
        GROUP BY SUBSTR(AC_CODE_DTL, 1, 5)
      ),
      acc_names AS (
        SELECT '31101' as acc_code, 'تكلفة البضاعة المباعة' as acc_name FROM DUAL UNION ALL
        SELECT '31102', 'مردود المبيعات' FROM DUAL UNION ALL
        SELECT '31103', 'تكلفة مردود المبيعات' FROM DUAL UNION ALL
        SELECT '31104', 'الخصم المسموح به' FROM DUAL UNION ALL
        SELECT '31105', 'مردود مبيعات سنوات سابقة' FROM DUAL UNION ALL
        SELECT '31106', 'تكلفة مردود مبيعات سنوات سابقة' FROM DUAL UNION ALL
        SELECT '31109', 'تسوية المخزون' FROM DUAL UNION ALL
        SELECT '31110', 'فوارق التكلفة والكسور' FROM DUAL UNION ALL
        SELECT '32101', 'المرتبات والاجور وما في حكمها' FROM DUAL UNION ALL
        SELECT '32201', 'مصاريف عمولات المناديب' FROM DUAL UNION ALL
        SELECT '32401', 'مصاريف الإدارية' FROM DUAL UNION ALL
        SELECT '32801', 'مصاريف تشغيلية' FROM DUAL UNION ALL
        SELECT '41101', 'ايراد مبيعات' FROM DUAL UNION ALL
        SELECT '41202', 'ايرادات الخصم المكتسب' FROM DUAL
      ),
      inv_cogs AS (
        SELECT 
            '31101' as acc_code,
            SUM(CASE WHEN m.BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(im.I_QTY,0) * NVL(im.STK_COST,0) ELSE 0 END) as op_dr,
            0 as op_cr,
            SUM(CASE WHEN m.BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(im.I_QTY,0) * NVL(im.STK_COST,0) ELSE 0 END) as mv_dr,
            0 as mv_cr
        FROM IAS20261.ITEM_MOVEMENT im
        JOIN IAS20261.IAS_BILL_MST m 
          ON m.BILL_DOC_TYPE = im.BILL_DOC_TYPE 
         AND m.BILL_NO = im.DOC_NO 
         AND m.BILL_SER = im.DOC_SER
        WHERE (:rep_code IS NULL OR m.REP_CODE = :rep_code)
          AND im.DOC_TYPE = 1 
          AND NVL(im.I_QTY,0) > 0
      ),
      inv_cogs_ret AS (
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
      )
      SELECT 
          d.acc_code AS "الرقم", 
          MAX(n.acc_name) AS "الاسم",
          TO_CHAR(SUM(d.op_dr),'FM999,999,990.00') AS "مدين الافتتاحي",
          TO_CHAR(SUM(d.op_cr),'FM999,999,990.00') AS "دائن الافتتاحي",
          TO_CHAR(SUM(d.mv_dr),'FM999,999,990.00') AS "مدين الحركة",
          TO_CHAR(SUM(d.mv_cr),'FM999,999,990.00') AS "دائن الحركة",
          TO_CHAR(SUM(d.op_dr + d.mv_dr),'FM999,999,990.00') AS "مدين الأرصدة",
          TO_CHAR(SUM(d.op_cr + d.mv_cr),'FM999,999,990.00') AS "دائن الأرصدة",
          TO_CHAR(SUM(d.op_cr + d.mv_cr) - SUM(d.op_dr + d.mv_dr), 'FM999,999,990.00') AS "صافي"
      FROM all_data d
      JOIN acc_names n ON n.acc_code = d.acc_code
      GROUP BY d.acc_code
      ORDER BY d.acc_code
    \"\"\"},
"""

target = '     ) WHERE ROWNUM <= 300"""},'

if target in content and "true_income_statement" not in content:
    content = content.replace(target, target + "\n" + report_code, 1)
    with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", 'w', 'utf-8') as f:
        f.write(content)
    print("Report injected successfully.")
else:
    print("Target not found or report already injected.")

