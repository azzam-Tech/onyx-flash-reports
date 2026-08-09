import pandas as pd
from database import get_conn

with get_conn() as con:
    # Query for Sales
    sql_sales = '''
        SELECT 
            m.BILL_NO as "رقم الفاتورة",
            TO_CHAR(m.BILL_DATE, 'YYYY-MM-DD') as "تاريخ الفاتورة",
            im.I_CODE as "رقم الصنف",
            MAX(it.I_NAME) as "اسم الصنف",
            SUM(NVL(im.I_QTY,0)) as "الكمية",
            MAX(NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0))) as "تكلفة الوحدة (تسعيرة 1)",
            SUM(NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0))) as "إجمالي التكلفة"
        FROM IAS20261.ITEM_MOVEMENT im
        JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE = im.BILL_DOC_TYPE AND m.BILL_NO = im.DOC_NO AND m.BILL_SER = im.DOC_SER
        JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
        LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
        WHERE m.REP_CODE = '144'
          AND im.DOC_TYPE = 1 
          AND NVL(im.I_QTY,0) > 0
          AND m.BILL_DATE >= TO_DATE('2026-06-01', 'YYYY-MM-DD') AND m.BILL_DATE <= TO_DATE('2026-06-30', 'YYYY-MM-DD')
        GROUP BY m.BILL_NO, m.BILL_DATE, im.I_CODE
        ORDER BY m.BILL_DATE, m.BILL_NO
    '''
    df_sales = pd.read_sql(sql_sales, con)
    
    # Query for Returns
    sql_returns = '''
        SELECT 
            r.RT_BILL_NO as "رقم مرتجع المبيعات",
            TO_CHAR(r.RT_BILL_DATE, 'YYYY-MM-DD') as "تاريخ المرتجع",
            im.I_CODE as "رقم الصنف",
            MAX(it.I_NAME) as "اسم الصنف",
            SUM(NVL(im.I_QTY,0)) as "الكمية",
            MAX(NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0))) as "تكلفة الوحدة (تسعيرة 1)",
            SUM(NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0))) as "إجمالي التكلفة"
        FROM IAS20261.ITEM_MOVEMENT im
        JOIN IAS20261.IAS_RT_BILL_MST r ON r.RT_BILL_DOC_TYPE = im.BILL_DOC_TYPE AND r.RT_BILL_NO = im.DOC_NO AND r.RT_BILL_SER = im.DOC_SER
        JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
        LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
        WHERE r.REP_CODE = '144'
          AND im.DOC_TYPE = 3
          AND NVL(im.I_QTY,0) > 0
          AND r.RT_BILL_DATE >= TO_DATE('2026-06-01', 'YYYY-MM-DD') AND r.RT_BILL_DATE <= TO_DATE('2026-06-30', 'YYYY-MM-DD')
        GROUP BY r.RT_BILL_NO, r.RT_BILL_DATE, im.I_CODE
        ORDER BY r.RT_BILL_DATE, r.RT_BILL_NO
    '''
    df_returns = pd.read_sql(sql_returns, con)

# Add a totals row to Sales
total_sales = df_sales['إجمالي التكلفة'].sum()
totals_sales_row = pd.DataFrame([{
    'رقم الفاتورة': 'الإجمالي الكلي',
    'تاريخ الفاتورة': '',
    'رقم الصنف': '',
    'اسم الصنف': '',
    'الكمية': None,
    'تكلفة الوحدة (تسعيرة 1)': None,
    'إجمالي التكلفة': total_sales
}])
df_sales = pd.concat([df_sales, totals_sales_row], ignore_index=True)

# Add a totals row to Returns
total_returns = df_returns['إجمالي التكلفة'].sum()
totals_returns_row = pd.DataFrame([{
    'رقم مرتجع المبيعات': 'الإجمالي الكلي',
    'تاريخ المرتجع': '',
    'رقم الصنف': '',
    'اسم الصنف': '',
    'الكمية': None,
    'تكلفة الوحدة (تسعيرة 1)': None,
    'إجمالي التكلفة': total_returns
}])
df_returns = pd.concat([df_returns, totals_returns_row], ignore_index=True)

file_path = '../Delegate_144_Cost_Of_Sales_Month6.xlsx'
with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
    df_sales.to_excel(writer, sheet_name='مبيعات شهر 6', index=False)
    df_returns.to_excel(writer, sheet_name='مرتجعات شهر 6', index=False)

print(f"File exported successfully to {file_path}")
print(f"Total Sales Cost: {total_sales}")
print(f"Total Returns Cost: {total_returns}")
