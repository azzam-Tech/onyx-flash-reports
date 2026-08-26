import sys
import os
import csv

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            query = """
                SELECT 
                    c.C_CODE, 
                    c.C_A_NAME, 
                    c.PROV_NO, 
                    p.PROV_A_NAME, 
                    c.CITY_NO, 
                    city.CITY_A_NAME, 
                    c.R_CODE, 
                    rgn.R_A_NAME
                FROM CUSTOMER c
                LEFT JOIN IAS_PROVINCES p ON c.PROV_NO = p.PROV_NO
                LEFT JOIN CITIES city ON c.CITY_NO = city.CITY_NO
                LEFT JOIN REGIONS rgn ON c.R_CODE = rgn.R_CODE
                WHERE 
                   (c.PROV_NO IS NOT NULL AND (c.PROV_NO < 101 OR c.PROV_NO > 113))
                   OR (city.PROV_NO IS NOT NULL AND (city.PROV_NO < 101 OR city.PROV_NO > 113))
                   OR (rgn.PROV_NO IS NOT NULL AND (rgn.PROV_NO < 101 OR rgn.PROV_NO > 113))
                ORDER BY c.C_CODE
            """
            cur.execute(query)
            rows = cur.fetchall()
            
            # Save to CSV
            os.makedirs('Results', exist_ok=True)
            csv_path = 'Results/wrong_location_customers.csv'
            with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'رقم العميل', 'اسم العميل', 
                    'رقم المحافظة (في العميل)', 'اسم المحافظة', 
                    'رقم المدينة (في العميل)', 'اسم المدينة', 
                    'رقم المنطقة (في العميل)', 'اسم المنطقة'
                ])
                writer.writerows(rows)
            
            # Save top 100 to Markdown artifact for quick viewing
            md = ["# ⚠️ قائمة العملاء المرتبطين بمواقع خاطئة"]
            md.append("هذه القائمة تعرض العملاء الذين تم ربطهم بمحافظات (أو مدن ومناطق تتبع لمحافظات) تقع خارج النطاق الصحيح المعتمد (101 - 113).")
            md.append(f"\n**إجمالي عدد العملاء المخالفين:** {len(rows)} عميل.\n")
            
            if rows:
                md.append("*(نعرض هنا أول 100 عميل فقط كعينة، القائمة الكاملة متوفرة في ملف CSV في مجلد Results)*\n")
                md.append("| رقم العميل | اسم العميل | رقم المحافظة | اسم المحافظة | رقم المدينة | اسم المدينة | رقم المنطقة | اسم المنطقة |")
                md.append("|---|---|---|---|---|---|---|---|")
                for r in rows[:100]:
                    md.append(f"| {r[0]} | {r[1]} | {r[2] or '-'} | {r[3] or '-'} | {r[4] or '-'} | {r[5] or '-'} | {r[6] or '-'} | {r[7] or '-'} |")
            else:
                md.append("🎉 **رائع! لا يوجد أي عميل مرتبط بمواقع جغرافية خاطئة حالياً.**")
                
            md_path = 'testing/wrong_customers.md'
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write("\n".join(md))
                
            print(f"Found {len(rows)} customers with wrong locations.")
            print(f"CSV saved to {csv_path}")
            print(f"Markdown report saved to {md_path}")
            
except Exception as e:
    print(f"Error: {e}")
