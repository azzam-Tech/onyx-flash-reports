import pandas as pd
from database import get_conn
import os

item_code = 'FREAR-80LWG'
rep_code = '144'
date_from = '2026-06-01'
date_to = '2026-06-30'

sql = """
SELECT 
    im.DOC_TYPE as "نوع الحركة",
    im.DOC_NO as "رقم المستند",
    NVL(m.BILL_DATE, r.RT_BILL_DATE) as "تاريخ المستند",
    im.I_QTY as "الكمية",
    NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) as "سعر التكلفة (تسعيرة 1)",
    im.I_COST as "متوسط التكلفة (الفعلي)",
    
    -- حساباتنا (تسعيرة 1)
    CASE WHEN im.DOC_TYPE = 1 THEN im.I_QTY ELSE -im.I_QTY END * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) as "إجمالي التكلفة (عندنا)",
    
    -- حسابات الصديق (فعلي)
    CASE WHEN im.DOC_TYPE = 1 THEN im.I_QTY ELSE -im.I_QTY END * im.I_COST as "إجمالي التكلفة (عند الصديق)",
    
    -- الفارق
    (CASE WHEN im.DOC_TYPE = 1 THEN im.I_QTY ELSE -im.I_QTY END * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0))) - 
    (CASE WHEN im.DOC_TYPE = 1 THEN im.I_QTY ELSE -im.I_QTY END * im.I_COST) as "الفارق"
FROM IAS20261.ITEM_MOVEMENT im
JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
LEFT JOIN IAS20261.IAS_BILL_MST m 
  ON m.BILL_DOC_TYPE = im.BILL_DOC_TYPE 
 AND m.BILL_NO = im.DOC_NO 
 AND m.BILL_SER = im.DOC_SER
 AND im.DOC_TYPE = 1
LEFT JOIN IAS20261.IAS_RT_BILL_MST r
  ON r.RT_BILL_DOC_TYPE = im.BILL_DOC_TYPE 
 AND r.RT_BILL_NO = im.DOC_NO 
 AND r.RT_BILL_SER = im.DOC_SER
 AND im.DOC_TYPE = 3
WHERE im.I_CODE = :item_code
  AND (m.REP_CODE = :rep_code OR r.REP_CODE = :rep_code)
  AND (
       (m.BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND m.BILL_DATE <= TO_DATE(:date_to, 'YYYY-MM-DD'))
       OR 
       (r.RT_BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND r.RT_BILL_DATE <= TO_DATE(:date_to, 'YYYY-MM-DD'))
  )
  AND im.DOC_TYPE IN (1, 3)
ORDER BY NVL(m.BILL_DATE, r.RT_BILL_DATE)
"""

with get_conn() as con:
    df = pd.read_sql(sql, con, params={"item_code": item_code, "rep_code": rep_code, "date_from": date_from, "date_to": date_to})

df['نوع الحركة'] = df['نوع الحركة'].map({1: 'مبيعات', 3: 'مردودات'})

totals = pd.DataFrame({
    'نوع الحركة': ['الإجمالي'],
    'رقم المستند': [''],
    'تاريخ المستند': [''],
    'الكمية': [""],
    'سعر التكلفة (تسعيرة 1)': [''],
    'متوسط التكلفة (الفعلي)': [''],
    'إجمالي التكلفة (عندنا)': [df['إجمالي التكلفة (عندنا)'].sum()],
    'إجمالي التكلفة (عند الصديق)': [df['إجمالي التكلفة (عند الصديق)'].sum()],
    'الفارق': [df['الفارق'].sum()]
})
df_final = pd.concat([df, totals], ignore_index=True)

excel_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'مقارنة_التكلفة_FREAR-80LWG.xlsx'))
df_final.to_excel(excel_path, index=False)
print(f"Excel generated at: {excel_path}")
