import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

def format_md_table(headers, rows):
    if not rows:
        return "*لا توجد بيانات*"
    res = []
    res.append("| " + " | ".join(headers) + " |")
    res.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        res.append("| " + " | ".join(str(x) if x is not None else "" for x in row) + " |")
    return "\n".join(res)

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            # Fetch Countries
            cur.execute("SELECT CNTRY_NO, CNTRY_A_NAME FROM CNTRY")
            cntry_rows = cur.fetchall()
            
            # Fetch Provinces
            cur.execute("SELECT PROV_NO, PROV_A_NAME, CNTRY_NO FROM IAS_PROVINCES")
            prov_rows = cur.fetchall()
            
            # Fetch Cities
            cur.execute("SELECT CITY_NO, CITY_A_NAME, PROV_NO, CNTRY_NO FROM CITIES")
            city_rows = cur.fetchall()
            
            # Fetch Zones
            cur.execute("SELECT ZONE_NO, ZONE_L_NM FROM S_ZONE")
            zone_rows = cur.fetchall()
            
            # Fetch Sales Regions
            cur.execute("SELECT R_CODE, R_A_NAME FROM REGIONS")
            region_rows = cur.fetchall()
            
            report = []
            report.append("# 📍 تقرير مراجعة البيانات الجغرافية (Geographical Data Audit)\n")
            
            report.append("## 1. الدول المعرفة (Countries)")
            report.append(format_md_table(["رقم الدولة (CNTRY_NO)", "اسم الدولة"], cntry_rows))
            report.append("\n")
            
            report.append("## 2. المحافظات المعرفة (Governorates)")
            report.append(format_md_table(["رقم المحافظة", "اسم المحافظة", "رقم الدولة المرتبطة"], prov_rows))
            report.append("\n")
            
            report.append("## 3. المناطق الإدارية (Zones - S_ZONE)")
            report.append(format_md_table(["رقم المنطقة", "اسم المنطقة"], zone_rows))
            report.append("\n")
            
            report.append("## 4. المناطق البيعية (Sales Regions - REGIONS)")
            report.append(format_md_table(["رمز المنطقة", "اسم المنطقة البيعية"], region_rows))
            report.append("\n")
            
            report.append("## 5. المدن المعرفة (Cities)")
            report.append(format_md_table(["رقم المدينة", "اسم المدينة", "رقم المحافظة", "رقم الدولة"], city_rows))
            report.append("\n")
            
            with open('testing/geo_audit.md', 'w', encoding='utf-8') as f:
                f.write("\n".join(report))
                
            print("Audit report generated at testing/geo_audit.md")
except Exception as e:
    print(f"Error: {e}")
