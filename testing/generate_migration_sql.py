import openpyxl

try:
    wb = openpyxl.load_workbook('Results/Province_Mapping_Template.xlsx')
    ws = wb['خريطة دمج المحافظات']
    
    mappings = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        wrong_id, wrong_name, correct_id = row
        if correct_id is not None and str(correct_id).strip() != '':
            mappings.append((wrong_id, correct_id))
            
    sql_lines = [
        "-- سكربت ترحيل البيانات الجغرافية (Migration Script)",
        "-- هذا السكربت يقوم بنقل المدن، المناطق البيعية، والعملاء من الأرقام الخاطئة إلى الأرقام الصحيحة بناءً على الخريطة التي قدمتها.",
        "SET DEFINE OFF;",
        ""
    ]
    
    tables_to_update = [
        'CITIES',
        'REGIONS',
        'CUSTOMER',
        'WAREHOUSE_DETAILS',
        'S_BRN',
        'IAS_SMAN_COL_CNDTN_DTL',
        'IAS_ONLINE_CONN_WC_RGN'
    ]
    
    for wrong, correct in mappings:
        sql_lines.append(f"-- ==========================================")
        sql_lines.append(f"-- دمج المحافظة الخاطئة ({wrong}) إلى المحافظة الصحيحة ({correct})")
        sql_lines.append(f"-- ==========================================")
        for table in tables_to_update:
            sql_lines.append(f"UPDATE IAS20261.{table} SET PROV_NO = {correct} WHERE PROV_NO = {wrong};")
        sql_lines.append("")
        
    sql_lines.append("-- أخيراً، محاولة حذف المحافظات الخاطئة بعد أن تم إفراغها ونقل كل ما فيها")
    sql_lines.append("BEGIN")
    for wrong, _ in mappings:
        sql_lines.append(f"  BEGIN DELETE FROM IAS20261.IAS_PROVINCES WHERE PROV_NO = {wrong}; EXCEPTION WHEN OTHERS THEN NULL; END;")
    sql_lines.append("END;")
    sql_lines.append("/")
    sql_lines.append("COMMIT;")
    sql_lines.append("")
    
    with open('testing/migrate_locations.sql', 'w', encoding='utf-8') as f:
        f.write("\n".join(sql_lines))
        
    print("Migration SQL script generated successfully.")
            
except Exception as e:
    print(f"Error: {e}")
