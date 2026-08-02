app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find('"id":"true_income_statement"')
if idx == -1:
    print("ERROR: true_income_statement not found!")
    sys.exit(1)

start_idx = content.rfind('{', 0, idx)
end_idx = content.find('}', idx) + 1

old_block = content[start_idx:end_idx]

new_block = """{"id":"true_income_statement","title":"قائمة الدخل (الحقيقية)","params":[DFROM,DTO,REP],"sql":\"\"\"
        WITH gl_base AS (
          SELECT 
              A_CODE as acc_code,
              SUM(CASE WHEN DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(DR_AMT,0) ELSE 0 END) as op_dr,
              SUM(CASE WHEN DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(CR_AMT,0) ELSE 0 END) as op_cr,
              SUM(CASE WHEN DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(DR_AMT,0) ELSE 0 END) as mv_dr,
              SUM(CASE WHEN DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(CR_AMT,0) ELSE 0 END) as mv_cr
          FROM IAS20261.IAS_POST_DTL
          WHERE (:rep_code IS NULL OR REP_CODE = :rep_code OR CC_CODE = :rep_code)
            AND NVL(DOC_POST,0)=1
            AND (
                A_CODE LIKE '31102%' OR A_CODE LIKE '31104%' OR A_CODE LIKE '31105%' OR A_CODE LIKE '31109%' OR A_CODE LIKE '31110%' OR
                A_CODE LIKE '32101%' OR A_CODE LIKE '32201%' OR A_CODE LIKE '32401%' OR A_CODE LIKE '32801%' OR
                A_CODE LIKE '41101%' OR A_CODE LIKE '41202%'
            )
          GROUP BY A_CODE
        ),
        inv_cogs AS (
          SELECT 
              '311010001' as acc_code,
              SUM(CASE WHEN m.BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) ELSE 0 END) as op_dr,
              0 as op_cr,
              SUM(CASE WHEN m.BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) ELSE 0 END) as mv_dr,
              0 as mv_cr
          FROM IAS20261.ITEM_MOVEMENT im
          JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
          LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
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
              '311030001' as acc_code,
              0 as op_dr,
              SUM(CASE WHEN r.RT_BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) ELSE 0 END) as op_cr,
              0 as mv_dr,
              SUM(CASE WHEN r.RT_BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) ELSE 0 END) as mv_cr
          FROM IAS20261.ITEM_MOVEMENT im
          JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
          LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
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
              '311060001' as acc_code,
              0 as op_dr,
              SUM(CASE WHEN r.RT_BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) ELSE 0 END) as op_cr,
              0 as mv_dr,
              SUM(CASE WHEN r.RT_BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) ELSE 0 END) as mv_cr
          FROM IAS20261.ITEM_MOVEMENT im
          JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
          LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
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
        )
        SELECT 
            d.acc_code AS "الرقم", 
            MAX(a.A_NAME) AS "الاسم",
            TO_CHAR(NULLIF(ROUND(NVL(SUM(d.op_dr),0),2), 0),'FM999,999,990.00') AS "الرصيد الافتتاحي مدين",
            TO_CHAR(NULLIF(ROUND(NVL(SUM(d.op_cr),0),2), 0),'FM999,999,990.00') AS "الرصيد الافتتاحي دائن",
            TO_CHAR(NULLIF(ROUND(NVL(SUM(d.mv_dr),0),2), 0),'FM999,999,990.00') AS "رصيد الحركة مدين",
            TO_CHAR(NULLIF(ROUND(NVL(SUM(d.mv_cr),0),2), 0),'FM999,999,990.00') AS "رصيد الحركة دائن",
            TO_CHAR(NULLIF(ROUND(
              CASE WHEN (NVL(SUM(d.op_dr),0) + NVL(SUM(d.mv_dr),0)) - (NVL(SUM(d.op_cr),0) + NVL(SUM(d.mv_cr),0)) > 0 
                   THEN (NVL(SUM(d.op_dr),0) + NVL(SUM(d.mv_dr),0)) - (NVL(SUM(d.op_cr),0) + NVL(SUM(d.mv_cr),0))
                   ELSE 0 END, 2), 0), 'FM999,999,990.00'
            ) AS "الأرصدة مدين",
            TO_CHAR(NULLIF(ROUND(
              CASE WHEN (NVL(SUM(d.op_cr),0) + NVL(SUM(d.mv_cr),0)) - (NVL(SUM(d.op_dr),0) + NVL(SUM(d.mv_dr),0)) > 0 
                   THEN (NVL(SUM(d.op_cr),0) + NVL(SUM(d.mv_cr),0)) - (NVL(SUM(d.op_dr),0) + NVL(SUM(d.mv_dr),0))
                   ELSE 0 END, 2), 0), 'FM999,999,990.00'
            ) AS "الأرصدة دائن"
        FROM all_data d
        LEFT JOIN IAS20261.ACCOUNT a ON a.A_CODE = d.acc_code
        GROUP BY d.acc_code
        ORDER BY d.acc_code
      \"\"\"}"""

content = content[:start_idx] + new_block + content[end_idx:]

with open(app_path, "w", encoding="utf-8") as f:
    f.write(content)

print("APPLIED WHOLESALE COGS TO APP.PY SUCCESSFULLY!")
