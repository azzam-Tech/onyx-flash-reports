import openpyxl
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

try:
    wb = openpyxl.load_workbook('Results/Region_Merge_Template_Short.xlsx')
    ws = wb['دمج المناطق الفعالة فقط']
    
    mappings = []
    # Columns: 
    # 0: city_no, 1: city_name, 2: r_code, 3: r_name, 4: merge_target
    for row in ws.iter_rows(min_row=2, values_only=True):
        r_code = row[2]
        r_name = row[3]
        merge_target = row[4]
        
        if merge_target is not None and str(merge_target).strip() != '':
            r_code = int(r_code)
            merge_target = int(merge_target)
            
            if r_code != merge_target:
                mappings.append((r_code, merge_target, r_name))
                
    if not mappings:
        print("No merges found in the template.")
        sys.exit(0)

    # Now get the foreign key details from the database
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            # 1. Get the PK constraint of REGIONS
            cur.execute("""
                SELECT CONSTRAINT_NAME 
                FROM ALL_CONSTRAINTS 
                WHERE TABLE_NAME = 'REGIONS' AND CONSTRAINT_TYPE = 'P' AND OWNER = 'IAS20261'
            """)
            pk_name = cur.fetchone()[0]
            
            # 2. Get all tables and columns that reference this PK
            # A foreign key can have multiple columns (like CITY_NO, R_CODE).
            # We specifically want the column that maps to R_CODE in the parent REGIONS table.
            # Assuming REGIONS PK is (CITY_NO, R_CODE) or just R_CODE.
            # Let's get the position of R_CODE in REGIONS PK
            cur.execute(f"""
                SELECT POSITION FROM ALL_CONS_COLUMNS 
                WHERE CONSTRAINT_NAME = '{pk_name}' AND COLUMN_NAME = 'R_CODE' AND OWNER = 'IAS20261'
            """)
            r_code_pos = cur.fetchone()[0]
            
            # Now find matching columns in child tables
            cur.execute(f"""
                SELECT a.TABLE_NAME, a.COLUMN_NAME
                FROM ALL_CONS_COLUMNS a
                JOIN ALL_CONSTRAINTS c ON a.CONSTRAINT_NAME = c.CONSTRAINT_NAME AND a.OWNER = c.OWNER
                WHERE c.R_CONSTRAINT_NAME = '{pk_name}' 
                  AND c.OWNER = 'IAS20261'
                  AND a.POSITION = {r_code_pos}
            """)
            fk_columns = cur.fetchall()
            
    sql_lines = [
        "-- سكربت دمج المناطق البيعية (Region Migration Script)",
        "-- هذا السكربت الشامل يقوم بنقل البيانات عبر جميع الجداول المرتبطة بالمنطقة.",
        "SET DEFINE OFF;",
        ""
    ]
    
    for wrong, correct, name in mappings:
        sql_lines.append(f"-- ==========================================")
        sql_lines.append(f"-- دمج المنطقة المكررة ({wrong} - {name}) إلى المنطقة الأساسية ({correct})")
        sql_lines.append(f"-- ==========================================")
        
        # We might have multiple FKs on the same table (e.g. CUSTOMER has two FKs to REGIONS).
        # We should generate distinct UPDATE statements per TABLE + COLUMN combination.
        unique_updates = set()
        for table_name, column_name in fk_columns:
            unique_updates.add((table_name, column_name))
            
        for table_name, column_name in unique_updates:
            sql_lines.append(f"UPDATE IAS20261.{table_name} SET {column_name} = {correct} WHERE {column_name} = {wrong};")
            
        sql_lines.append("")
        
    sql_lines.append("-- أخيراً، حذف المناطق المتكررة بأمان")
    sql_lines.append("BEGIN")
    for wrong, _, _ in mappings:
        sql_lines.append(f"  BEGIN DELETE FROM IAS20261.REGIONS WHERE R_CODE = {wrong}; EXCEPTION WHEN OTHERS THEN NULL; END;")
    sql_lines.append("END;")
    sql_lines.append("/")
    sql_lines.append("COMMIT;")
    sql_lines.append("")
    
    output_path = 'testing/migrate_regions.sql'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(sql_lines))
        
    print(f"Generated region migration script with {len(mappings)} region merges.")
    print(f"Updated {len(unique_updates)} foreign key references per merge.")
    print(f"File saved to {output_path}")

except Exception as e:
    print(f"Error: {e}")
