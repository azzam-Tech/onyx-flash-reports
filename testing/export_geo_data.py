import sys
import os
import csv

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            # --- STEP 1: Find unused locations ---
            
            # Unused Provinces
            cur.execute("""
                SELECT p.PROV_NO, p.PROV_A_NAME 
                FROM IAS_PROVINCES p
                WHERE NOT EXISTS (SELECT 1 FROM CUSTOMER c WHERE c.PROV_NO = p.PROV_NO)
            """)
            unused_provs = cur.fetchall()
            
            # Unused Cities
            cur.execute("""
                SELECT c.CITY_NO, c.CITY_A_NAME 
                FROM CITIES c
                WHERE NOT EXISTS (SELECT 1 FROM CUSTOMER cust WHERE cust.CITY_NO = c.CITY_NO)
            """)
            unused_cities = cur.fetchall()
            
            # Unused Regions
            cur.execute("""
                SELECT r.R_CODE, r.R_A_NAME 
                FROM REGIONS r
                WHERE NOT EXISTS (SELECT 1 FROM CUSTOMER c WHERE c.R_CODE = r.R_CODE)
            """)
            unused_regions = cur.fetchall()
            
            md = ["# 🗑️ المواقع غير المستخدمة (بدون عملاء)"]
            md.append("هذه القائمة تحتوي على المواقع التي لا يرتبط بها أي عميل حالياً، ويمكنك دراسة إمكانية إيقافها أو حذفها لتنظيف القوائم.\n")
            
            md.append("### 1. المحافظات غير المستخدمة")
            if unused_provs:
                md.append("| رقم المحافظة | اسم المحافظة |")
                md.append("|---|---|")
                for r in unused_provs:
                    md.append(f"| {r[0]} | {r[1]} |")
            else:
                md.append("*لا يوجد، كل المحافظات قيد الاستخدام.*")
            
            md.append("\n### 2. المدن غير المستخدمة")
            if unused_cities:
                md.append("| رقم المدينة | اسم المدينة |")
                md.append("|---|---|")
                for r in unused_cities:
                    md.append(f"| {r[0]} | {r[1]} |")
            else:
                md.append("*لا يوجد، كل المدن قيد الاستخدام.*")
                
            md.append("\n### 3. المناطق البيعية غير المستخدمة")
            if unused_regions:
                md.append("| رمز المنطقة | اسم المنطقة |")
                md.append("|---|---|")
                for r in unused_regions:
                    md.append(f"| {r[0]} | {r[1]} |")
            else:
                md.append("*لا يوجد، كل المناطق قيد الاستخدام.*")
                
            with open('testing/unused_locations.md', 'w', encoding='utf-8') as f:
                f.write("\n".join(md))
                
            # --- STEP 3: Export tree for Excel ---
            
            # 1. Full Administrative Tree (Country -> Province -> City)
            cur.execute("""
                SELECT 
                    cntry.CNTRY_NO, cntry.CNTRY_A_NAME,
                    prov.PROV_NO, prov.PROV_A_NAME,
                    city.CITY_NO, city.CITY_A_NAME
                FROM CNTRY cntry
                LEFT JOIN IAS_PROVINCES prov ON prov.CNTRY_NO = cntry.CNTRY_NO
                LEFT JOIN CITIES city ON city.PROV_NO = prov.PROV_NO AND city.CNTRY_NO = cntry.CNTRY_NO
                ORDER BY cntry.CNTRY_NO, prov.PROV_NO, city.CITY_NO
            """)
            full_tree = cur.fetchall()
            
            # Save to CSV with BOM for proper Excel display
            os.makedirs('Results', exist_ok=True)
            with open('Results/administrative_tree.csv', 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow(['رقم الدولة', 'اسم الدولة', 'رقم المحافظة', 'اسم المحافظة', 'رقم المدينة', 'اسم المدينة'])
                writer.writerows(full_tree)
                
            # 2. Sales Regions 
            cur.execute("SELECT R_CODE, R_A_NAME FROM REGIONS ORDER BY R_CODE")
            regions = cur.fetchall()
            
            with open('Results/sales_regions.csv', 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow(['رمز المنطقة', 'اسم المنطقة البيعية'])
                writer.writerows(regions)
                
            print("Successfully generated unused_locations.md and CSV files in Results folder.")
            
except Exception as e:
    print(f"Error: {e}")
