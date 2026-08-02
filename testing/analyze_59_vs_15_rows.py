import sys
sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn

sql_detailed = """
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
      SUM(CASE WHEN m.BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(im.I_QTY,0) * NVL(it.PRIMARY_COST,0) ELSE 0 END) as op_dr,
      0 as op_cr,
      SUM(CASE WHEN m.BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(im.I_QTY,0) * NVL(it.PRIMARY_COST,0) ELSE 0 END) as mv_dr,
      0 as mv_cr
  FROM IAS20261.ITEM_MOVEMENT im
  JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
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
      SUM(CASE WHEN r.RT_BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(im.I_QTY,0) * NVL(it.PRIMARY_COST,0) ELSE 0 END) as op_cr,
      0 as mv_dr,
      SUM(CASE WHEN r.RT_BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(im.I_QTY,0) * NVL(it.PRIMARY_COST,0) ELSE 0 END) as mv_cr
  FROM IAS20261.ITEM_MOVEMENT im
  JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
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
      SUM(CASE WHEN r.RT_BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(im.I_QTY,0) * NVL(it.PRIMARY_COST,0) ELSE 0 END) as op_cr,
      0 as mv_dr,
      SUM(CASE WHEN r.RT_BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(im.I_QTY,0) * NVL(it.PRIMARY_COST,0) ELSE 0 END) as mv_cr
  FROM IAS20261.ITEM_MOVEMENT im
  JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
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
    d.acc_code AS code, 
    MAX(a.A_NAME) AS name,
    NVL(SUM(d.op_dr),0) as op_dr,
    NVL(SUM(d.op_cr),0) as op_cr,
    NVL(SUM(d.mv_dr),0) as mv_dr,
    NVL(SUM(d.mv_cr),0) as mv_cr
FROM all_data d
LEFT JOIN IAS20261.ACCOUNT a ON a.A_CODE = d.acc_code
GROUP BY d.acc_code
ORDER BY d.acc_code
"""

binds = {"date_from": "2026-01-01", "date_to": "2026-12-31", "rep_code": ""}

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute(sql_detailed, binds)
        rows = cur.fetchall()

print(f"Total detailed accounts fetched: {len(rows)}")

groups = {}
for r in rows:
    code, name, op_dr, op_cr, mv_dr, mv_cr = r
    parent_prefix = code[:5]
    if parent_prefix not in groups:
        groups[parent_prefix] = []
    groups[parent_prefix].append((code, name, mv_dr, mv_cr))

print(f"Total parent groups: {len(groups)}")
for p, items in groups.items():
    print(f"\n--- PARENT GROUP: {p} ({len(items)} sub-accounts) ---")
    for code, name, dr, cr in items:
        print(f"  {code} | {name} | DR: {dr:,.2f} | CR: {cr:,.2f}")
