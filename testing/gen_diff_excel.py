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
                # 1. SREEN Net Sales & Additional Discounts Ignored by Onyx
                sql_sreen = f'''
                    SELECT 
                        SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT,0)) as sreen_sales,
                        SUM(NVL(ADD_DISC_AMT_MST,0)) as ignored_add_disc
                    FROM IAS20261.IAS_BILL_MST
                    WHERE CC_CODE = {cc}
                      AND BILL_DATE >= TO_DATE('2026-06-01', 'YYYY-MM-DD')
                      AND BILL_DATE <= TO_DATE('2026-06-30', 'YYYY-MM-DD')
                      AND BILL_DOC_TYPE IN (1,4)
                '''
                cur.execute(sql_sreen)
                res = cur.fetchone()
                sreen_sales = res[0] or 0
                ignored_add_disc = res[1] or 0
                
                # 2. Doc Type 8 Sales (Supply Order) Included by Onyx but Ignored by SREEN
                sql_doc8 = f'''
                    SELECT 
                        SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT,0)) as doc8_sales
                    FROM IAS20261.IAS_BILL_MST
                    WHERE CC_CODE = {cc}
                      AND BILL_DATE >= TO_DATE('2026-06-01', 'YYYY-MM-DD')
                      AND BILL_DATE <= TO_DATE('2026-06-30', 'YYYY-MM-DD')
                      AND BILL_DOC_TYPE = 8
                '''
                cur.execute(sql_doc8)
                res_8 = cur.fetchone()
                doc8_sales = res_8[0] or 0
                
                onyx_sales = sreen_sales + ignored_add_disc + doc8_sales
                diff = onyx_sales - sreen_sales
                
                data.append({
                    'رقم المركز': cc,
                    'اسم مركز التكلفة': name,
                    'مبيعات SREEN (الصافية)': sreen_sales,
                    'الخصم الإضافي (لم يخصمه أونكس)': ignored_add_disc,
                    'أوامر التوريد (حسبها أونكس كمبيعات)': doc8_sales,
                    'مبيعات أونكس (النهائية)': onyx_sales,
                    'قيمة الاختلاف': diff
                })
            except Exception as e:
                print(f"Error processing CC {cc}: {e}")

df = pd.DataFrame(data)
df.to_excel('testing/Sales_Differences_Report.xlsx', index=False)
print("Excel file generated successfully!")
