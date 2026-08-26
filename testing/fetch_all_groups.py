import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            # 1. Fetch Sub Groups (MNG_CODE) for G_CODE = '003'
            cur.execute("""
                SELECT MNG_CODE, MNG_A_NAME 
                FROM IAS20261.IAS_MAINSUB_GRP_DTL 
                WHERE G_CODE IN ('003', '03')
                ORDER BY MNG_CODE
            """)
            sub_groups = cur.fetchall()
            
            # 2. Fetch ALL Sub-Sub Groups (SUBG_CODE) because they don't have G_CODE populated!
            cur.execute("""
                SELECT SUBG_CODE, SUBG_A_NAME 
                FROM IAS20261.IAS_SUB_GRP_DTL 
                ORDER BY SUBG_CODE
            """)
            sub_sub_groups = cur.fetchall()
            
            # Write to artifact
            out_path = 'C:/Users/amarn/.gemini/antigravity-ide/brain/8b15bbf6-a63f-4c47-a5af-c7f3231364f8/refrigerator_groups.md'
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write("# المجموعات الخاصة بالثلاجات (المجموعة الرئيسية: 003)\n\n")
                
                f.write("## المجموعات الفرعية (الأحجام/الأنواع)\n")
                f.write("| رقم المجموعة الفرعية | اسم المجموعة الفرعية |\n")
                f.write("| :--- | :--- |\n")
                for r in sub_groups:
                    f.write(f"| `{r[0]}` | {r[1]} |\n")
                    
                f.write("\n## المجموعات تحت الفرعية (الألوان/التفاصيل)\n")
                f.write("> [!NOTE]\n> المجموعات تحت الفرعية غير مرتبطة بشكل مباشر بأب في قاعدة البيانات (Floating Groups)، بل يمكن استخدام أي منها تحت أي مجموعة فرعية.\n\n")
                
                f.write("| رقم المجموعة تحت الفرعية | اسم المجموعة تحت الفرعية |\n")
                f.write("| :--- | :--- |\n")
                for r in sub_sub_groups:
                    f.write(f"| `{r[0]}` | {r[1]} |\n")
                    
            print("Successfully extracted groups to artifact.")
            
except Exception as e:
    print(f"Error: {e}")
