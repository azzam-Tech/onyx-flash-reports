import pandas as pd
import sys
sys.path.append('privet/onyx_reports')
from app import get_conn
import traceback

ccs = [
    (141, 'عبدالله النهدي'),
    (145, 'اقبال الهندي القصيم'),
    (146, 'ابو صالح الرياض'),
    (149, 'جاسر الهندي الرياض'),
    (151, 'احمد اخو الطيب'),
    (154, 'عبدالسلام الهندي'),
    (168, 'موقع سرين'),
    (169, 'موقع نون'),
    (171, 'مركز رامي شرمان')
]

data = []

with get_conn() as con:
    with con.cursor() as cur:
        for cc, name in ccs:
            try:
                # 1. Invoices with Additional Discounts Ignored by Onyx
                sql_add_disc = f'''
                    SELECT 
                        BILL_NO, 
                        BILL_DATE,
                        BILL_DOC_TYPE,
                        BILL_AMT,
                        ADD_DISC_AMT_MST
                    FROM IAS20261.IAS_BILL_MST
                    WHERE CC_CODE = {cc}
                      AND BILL_DATE >= TO_DATE('2026-06-01', 'YYYY-MM-DD')
                      AND BILL_DATE <= TO_DATE('2026-06-30', 'YYYY-MM-DD')
                      AND BILL_DOC_TYPE IN (1,4)
                      AND ADD_DISC_AMT_MST > 0
                '''
                cur.execute(sql_add_disc)
                for r in cur.fetchall():
                    bill_no = r[0]
                    bill_date = r[1].strftime('%Y-%m-%d') if r[1] else ''
                    doc_type = 'نقدي' if r[2] == 1 else 'آجل'
                    bill_amt = r[3] or 0
                    ignored_disc = r[4] or 0
                    
                    data.append({
                        'رقم المركز': cc,
                        'اسم المركز': name,
                        'رقم الفاتورة': bill_no,
                        'تاريخ الفاتورة': bill_date,
                        'نوع الفاتورة': f'مبيعات {doc_type}',
                        'قيمة الفاتورة': bill_amt,
                        'قيمة الاختلاف': ignored_disc,
                        'سبب الاختلاف': 'خصم إضافي تم إضافته للفاتورة ولكن تجاهله تقرير أونكس (لم يطرحه)'
                    })
                
                # 2. Doc Type 8 Sales (Supply Order) Included by Onyx
                sql_doc8 = f'''
                    SELECT 
                        BILL_NO, 
                        BILL_DATE,
                        BILL_AMT
                    FROM IAS20261.IAS_BILL_MST
                    WHERE CC_CODE = {cc}
                      AND BILL_DATE >= TO_DATE('2026-06-01', 'YYYY-MM-DD')
                      AND BILL_DATE <= TO_DATE('2026-06-30', 'YYYY-MM-DD')
                      AND BILL_DOC_TYPE = 8
                '''
                cur.execute(sql_doc8)
                for r in cur.fetchall():
                    bill_no = r[0]
                    bill_date = r[1].strftime('%Y-%m-%d') if r[1] else ''
                    bill_amt = r[2] or 0
                    
                    data.append({
                        'رقم المركز': cc,
                        'اسم المركز': name,
                        'رقم الفاتورة': bill_no,
                        'تاريخ الفاتورة': bill_date,
                        'نوع الفاتورة': 'أمر توريد مخزني',
                        'قيمة الفاتورة': bill_amt,
                        'قيمة الاختلاف': bill_amt,
                        'سبب الاختلاف': 'فاتورة أمر توريد مخزني قام تقرير أونكس بضمها للمبيعات بينما تم تجاهلها في SREEN'
                    })
                    
            except Exception as e:
                print(f"Error processing CC {cc}: {e}")

df = pd.DataFrame(data)
df.to_excel('testing/Detailed_Sales_Differences_Report.xlsx', index=False)
print("Detailed Excel file generated successfully!")
