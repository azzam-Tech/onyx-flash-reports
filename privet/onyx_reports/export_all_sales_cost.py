import os
import sys
import pandas as pd
from datetime import datetime
from database import get_conn

def export_sales_cost():
    rep_code = '144'
    date_from = '2026-06-01'
    date_to = '2026-06-30'
    
    sql = """
    SELECT 
        m.BILL_DATE as "تاريخ الفاتورة",
        m.BILL_DOC_TYPE as "نوع الفاتورة",
        m.BILL_NO as "رقم الفاتورة",
        im.I_CODE as "رقم الصنف",
        it.I_NAME as "اسم الصنف",
        im.I_QTY as "الكمية",
        NVL(ip1.I_PRICE, NVL(it.PRIMARY_COST,0)) as "سعر تسعيرة 1 (تكلفة تقريرنا)",
        (NVL(im.I_QTY,0) * NVL(ip1.I_PRICE, NVL(it.PRIMARY_COST,0))) as "إجمالي تكلفة تسعيرة 1",
        NVL(ip2.I_PRICE, 0) as "سعر تسعيرة 2",
        (NVL(im.I_QTY,0) * NVL(ip2.I_PRICE, 0)) as "إجمالي تكلفة تسعيرة 2",
        NVL(ip3.I_PRICE, 0) as "سعر تسعيرة 3",
        (NVL(im.I_QTY,0) * NVL(ip3.I_PRICE, 0)) as "إجمالي تكلفة تسعيرة 3",
        NVL(it.PRIMARY_COST, 0) as "التكلفة الأولية",
        (NVL(im.I_QTY,0) * NVL(it.PRIMARY_COST, 0)) as "إجمالي التكلفة الأولية",
        NVL(im.I_COST, 0) as "متوسط التكلفة الفعلي",
        (NVL(im.I_QTY,0) * NVL(im.I_COST, 0)) as "إجمالي تكلفة المتوسط الفعلي"
    FROM IAS20261.ITEM_MOVEMENT im
    JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
    LEFT JOIN IAS20261.IAS_ITEM_PRICE ip1 ON ip1.I_CODE = im.I_CODE AND ip1.LEV_NO = 1
    LEFT JOIN IAS20261.IAS_ITEM_PRICE ip2 ON ip2.I_CODE = im.I_CODE AND ip2.LEV_NO = 2
    LEFT JOIN IAS20261.IAS_ITEM_PRICE ip3 ON ip3.I_CODE = im.I_CODE AND ip3.LEV_NO = 3
    JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE = im.BILL_DOC_TYPE AND m.BILL_NO = im.DOC_NO AND m.BILL_SER = im.DOC_SER
    WHERE m.REP_CODE = :rep_code AND im.DOC_TYPE = 1 
      AND m.BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND m.BILL_DATE <= TO_DATE(:date_to, 'YYYY-MM-DD')
    ORDER BY m.BILL_DATE, m.BILL_NO, im.I_CODE
    """
    
    with get_conn() as con:
        df = pd.read_sql(sql, con, params={"rep_code": rep_code, "date_from": date_from, "date_to": date_to})
    
    # Add Total row
    totals = df.select_dtypes(include=['number']).sum()
    df.loc['المجموع'] = totals
    df.at['المجموع', 'رقم الصنف'] = 'الإجمالي العام'
    df.at['المجموع', 'اسم الصنف'] = '---'
    
    desktop_path = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity"
    excel_file = os.path.join(desktop_path, f"مقارنة_تكلفة_مبيعات_المندوب_{rep_code}.xlsx")
    
    df.to_excel(excel_file, index=False)
    print(f"Excel generated at: {excel_file}")

if __name__ == "__main__":
    export_sales_cost()
