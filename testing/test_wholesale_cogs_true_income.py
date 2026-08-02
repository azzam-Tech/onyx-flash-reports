import sys
sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn

# 1. COGS with PRIMARY_COST / STK_COST (Standard Warehouse Cost)
sql_standard = """
SELECT 
    '311010001' as acc_code,
    SUM(CASE WHEN m.BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(im.I_QTY,0) * NVL(it.PRIMARY_COST,0) ELSE 0 END) as cogs_sales
FROM IAS20261.ITEM_MOVEMENT im
JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
JOIN IAS20261.IAS_BILL_MST m 
  ON m.BILL_DOC_TYPE = im.BILL_DOC_TYPE 
 AND m.BILL_NO = im.DOC_NO 
 AND m.BILL_SER = im.DOC_SER
WHERE im.DOC_TYPE = 1 
  AND NVL(im.I_QTY,0) > 0
"""

# 2. COGS with WHOLESALE PRICE (LEV_NO = 1 in IAS_ITEM_PRICE)
sql_wholesale = """
SELECT 
    '311010001' as acc_code,
    SUM(CASE WHEN m.BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 
             THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) 
             ELSE 0 END) as cogs_sales
FROM IAS20261.ITEM_MOVEMENT im
JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
JOIN IAS20261.IAS_BILL_MST m 
  ON m.BILL_DOC_TYPE = im.BILL_DOC_TYPE 
 AND m.BILL_NO = im.DOC_NO 
 AND m.BILL_SER = im.DOC_SER
WHERE im.DOC_TYPE = 1 
  AND NVL(im.I_QTY,0) > 0
"""

binds = {"date_from": "2026-01-01", "date_to": "2026-12-31"}

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute(sql_standard, binds)
        std_val = cur.fetchone()[1]
        
        cur.execute(sql_wholesale, binds)
        ws_val = cur.fetchone()[1]

print(f"Standard Warehouse Cost COGS (311010001): {std_val:,.2f} SAR")
print(f"Wholesale Price List COGS (311010001):    {ws_val:,.2f} SAR")
print(f"Difference (Wholesale - Standard):         {ws_val - std_val:,.2f} SAR")
