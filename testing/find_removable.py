import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            # 1. Removable Provinces
            cur.execute("""
                SELECT p.PROV_NO, p.PROV_A_NAME 
                FROM IAS_PROVINCES p
                WHERE (p.PROV_NO < 101 OR p.PROV_NO > 113 OR p.PROV_NO IS NULL)
                  AND NOT EXISTS (SELECT 1 FROM CUSTOMER c WHERE c.PROV_NO = p.PROV_NO)
                ORDER BY p.PROV_NO
            """)
            removable_provs = cur.fetchall()
            
            # 2. Removable Cities
            cur.execute("""
                SELECT c.CITY_NO, c.CITY_A_NAME, c.PROV_NO 
                FROM CITIES c
                WHERE (c.PROV_NO < 101 OR c.PROV_NO > 113 OR c.PROV_NO IS NULL)
                  AND NOT EXISTS (SELECT 1 FROM CUSTOMER cust WHERE cust.CITY_NO = c.CITY_NO)
                ORDER BY c.CITY_NO
            """)
            removable_cities = cur.fetchall()
            
            # 3. Removable Regions
            cur.execute("""
                SELECT r.R_CODE, r.R_A_NAME, r.PROV_NO 
                FROM REGIONS r
                WHERE (r.PROV_NO < 101 OR r.PROV_NO > 113 OR r.PROV_NO IS NULL)
                  AND NOT EXISTS (SELECT 1 FROM CUSTOMER c WHERE c.R_CODE = r.R_CODE)
                ORDER BY r.R_CODE
            """)
            removable_regions = cur.fetchall()
            
            md = ["# 🧹 المواقع المخالفة للترتيب (جاهزة للحذف)"]
            md.append("بناءً على الترتيب المعتمد (المحافظات من 101 إلى 113 حصراً)، هذه هي المواقع التابعة لأرقام محافظات أخرى (أو بدون محافظة) **والتي لا يوجد عملاء مرتبطين بها أبداً**، مما يعني أنك تستطيع التخلص منها مباشرة.\n")
            
            md.append(f"### 1. المحافظات المخالفة وغير المستخدمة (العدد: {len(removable_provs)})")
            if removable_provs:
                md.append("| رقم المحافظة | اسم المحافظة |")
                md.append("|---|---|")
                for r in removable_provs:
                    md.append(f"| {r[0]} | {r[1]} |")
            
            md.append(f"\n### 2. المدن التابعة لها وغير المستخدمة (العدد: {len(removable_cities)})")
            if removable_cities:
                md.append("| رقم المدينة | اسم المدينة | تابعة للمحافظة رقم |")
                md.append("|---|---|---|")
                for r in removable_cities:
                    md.append(f"| {r[0]} | {r[1]} | {r[2] if r[2] else 'بدون'} |")
                    
            md.append(f"\n### 3. المناطق البيعية التابعة لها وغير المستخدمة (العدد: {len(removable_regions)})")
            if removable_regions:
                md.append("| رمز المنطقة | اسم المنطقة | تابعة للمحافظة رقم |")
                md.append("|---|---|---|")
                for r in removable_regions:
                    md.append(f"| {r[0]} | {r[1]} | {r[2] if r[2] else 'بدون'} |")
            
            with open('testing/removable_mess.md', 'w', encoding='utf-8') as f:
                f.write("\n".join(md))
                
            print(f"Found {len(removable_provs)} provinces, {len(removable_cities)} cities, {len(removable_regions)} regions.")
            print("Results saved to testing/removable_mess.md")

except Exception as e:
    print(f"Error: {e}")
