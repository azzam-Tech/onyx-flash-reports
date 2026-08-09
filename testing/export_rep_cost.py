import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn

def export_for_date(conn, rep_code, date):
    query = f"""
    WITH sales AS (
        SELECT 
            m.BILL_NO AS bill_no,
            'مبيعات' AS trans_type,
            im.I_CODE AS item_code,
            it.I_NAME AS item_name,
            NVL(im.I_QTY, 0) AS qty,
            NVL(ip.I_PRICE, NVL(it.PRIMARY_COST, 0)) AS unit_cost,
            (NVL(im.I_QTY, 0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST, 0))) AS total_cost,
            ((NVL(d.I_PRICE, 0) - NVL(d.DIS_AMT, 0)) + (NVL(d.OTHR_AMT, 0) + NVL(d.VAT_AMT, 0))) AS unit_sale,
            (((NVL(d.I_PRICE, 0) - NVL(d.DIS_AMT, 0)) + (NVL(d.OTHR_AMT, 0) + NVL(d.VAT_AMT, 0))) * NVL(im.I_QTY, 0)) AS total_sale
        FROM IAS20261.ITEM_MOVEMENT im
        JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
        LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
        JOIN IAS20261.IAS_BILL_MST m 
          ON m.BILL_DOC_TYPE = im.BILL_DOC_TYPE 
         AND m.BILL_NO = im.DOC_NO 
         AND m.BILL_SER = im.DOC_SER
        LEFT JOIN IAS20261.IAS_BILL_DTL d
          ON d.BILL_DOC_TYPE = im.BILL_DOC_TYPE
         AND d.BILL_NO = im.DOC_NO
         AND d.BILL_SER = im.DOC_SER
         AND d.I_CODE = im.I_CODE
        WHERE m.REP_CODE = {rep_code}
          AND im.DOC_TYPE = 1 
          AND m.BILL_DATE = TO_DATE('{date}', 'YYYY-MM-DD')
          AND NVL(im.I_QTY, 0) > 0
    ),
    returns AS (
        SELECT 
            r.RT_BILL_NO AS bill_no,
            'مردود مبيعات' AS trans_type,
            im.I_CODE AS item_code,
            it.I_NAME AS item_name,
            NVL(im.I_QTY, 0) * -1 AS qty,
            NVL(ip.I_PRICE, NVL(it.PRIMARY_COST, 0)) AS unit_cost,
            (NVL(im.I_QTY, 0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST, 0))) * -1 AS total_cost,
            ((NVL(d.I_PRICE, 0) - NVL(d.DIS_AMT, 0)) + (NVL(d.OTHR_AMT, 0) + NVL(d.VAT_AMT, 0))) AS unit_sale,
            (((NVL(d.I_PRICE, 0) - NVL(d.DIS_AMT, 0)) + (NVL(d.OTHR_AMT, 0) + NVL(d.VAT_AMT, 0))) * NVL(im.I_QTY, 0)) * -1 AS total_sale
        FROM IAS20261.ITEM_MOVEMENT im
        JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
        LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
        JOIN IAS20261.IAS_RT_BILL_MST r
          ON r.RT_BILL_DOC_TYPE = im.BILL_DOC_TYPE 
         AND r.RT_BILL_NO = im.DOC_NO 
         AND r.RT_BILL_SER = im.DOC_SER
        LEFT JOIN IAS20261.IAS_RT_BILL_DTL d
          ON d.RT_BILL_DOC_TYPE = im.BILL_DOC_TYPE
         AND d.RT_BILL_NO = im.DOC_NO
         AND d.RT_BILL_SER = im.DOC_SER
         AND d.I_CODE = im.I_CODE
        WHERE r.REP_CODE = {rep_code}
          AND im.DOC_TYPE = 3
          AND r.RT_BILL_DATE = TO_DATE('{date}', 'YYYY-MM-DD')
          AND r.PREV_YEAR IS NULL
          AND NVL(im.I_QTY, 0) > 0
    )
    SELECT * FROM sales
    UNION ALL
    SELECT * FROM returns
    ORDER BY 2, 1
    """
    
    print(f"Executing query for {date}...")
    df = pd.read_sql(query, conn)
    
    # Rename columns to Arabic
    df.rename(columns={
        'BILL_NO': 'رقم الفاتورة',
        'TRANS_TYPE': 'نوع الحركة',
        'ITEM_CODE': 'رقم الصنف',
        'ITEM_NAME': 'اسم الصنف',
        'QTY': 'الكمية',
        'UNIT_COST': 'تكلفة الوحدة',
        'TOTAL_COST': 'إجمالي التكلفة',
        'UNIT_SALE': 'سعر البيع',
        'TOTAL_SALE': 'إجمالي البيع'
    }, inplace=True)
    
    total_cost = df['إجمالي التكلفة'].sum()
    total_sale = df['إجمالي البيع'].sum()
    profit = total_sale - total_cost
    
    print(f"Results for {date}:")
    print(f"  Total Cost : {total_cost:,.2f}")
    print(f"  Total Sales: {total_sale:,.2f}")
    print(f"  Gross Profit: {profit:,.2f}")
    
    excel_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../Cost_Sales_Details_{rep_code}_{date}.xlsx'))
    df.to_excel(excel_path, index=False)
    print(f"Saved details to {excel_path}\n")

def main():
    conn = get_conn()
    if not conn:
        print("Failed to connect to DB")
        return
        
    rep_code = 144
    export_for_date(conn, rep_code, '2026-06-04')
    export_for_date(conn, rep_code, '2026-06-06')
    
    conn.close()

if __name__ == "__main__":
    main()
