import openpyxl

try:
    wb = openpyxl.load_workbook('Results/City_Merge_Template_Prefilled.xlsx')
    ws = wb['دمج المدن المتكررة']
    
    mappings = []
    # Columns: 
    # 0: prov_no, 1: prov_name, 2: city_no, 3: city_name, 4: merge_target
    for row in ws.iter_rows(min_row=2, values_only=True):
        city_no = row[2]
        city_name = row[3]
        merge_target = row[4]
        
        if merge_target is not None and str(merge_target).strip() != '':
            # Convert to int to be safe
            city_no = int(city_no)
            merge_target = int(merge_target)
            
            # Avoid mapping to itself
            if city_no != merge_target:
                mappings.append((city_no, merge_target, city_name))
                
    sql_lines = [
        "-- سكربت دمج المدن المتكررة (City Migration Script)",
        "-- هذا السكربت يقوم بنقل كل البيانات التابعة للمدينة المكررة (عملاء، مناطق، موردين...) لتصبح تحت المدينة الأساسية.",
        "SET DEFINE OFF;",
        ""
    ]
    
    tables_to_update = [
        'CUSTOMER',
        'SALES_MAN',
        'V_DETAILS',
        'REGIONS',
        'WAREHOUSE_DETAILS',
        'S_BRN',
        'IAS_PROMOTERS',
        'IAS_SMAN_COL_CNDTN_DTL',
        'CUSTOMER_RQ',
        'IAS_ONLINE_CONN_WC_RGN'
    ]
    
    for wrong, correct, name in mappings:
        sql_lines.append(f"-- ==========================================")
        sql_lines.append(f"-- دمج المدينة المكررة ({wrong} - {name}) إلى المدينة الأساسية ({correct})")
        sql_lines.append(f"-- ==========================================")
        for table in tables_to_update:
            sql_lines.append(f"UPDATE IAS20261.{table} SET CITY_NO = {correct} WHERE CITY_NO = {wrong};")
        sql_lines.append("")
        
    sql_lines.append("-- أخيراً، حذف المدن المتكررة بأمان بعد أن تم نقل كل ما فيها")
    sql_lines.append("BEGIN")
    for wrong, _, _ in mappings:
        sql_lines.append(f"  BEGIN DELETE FROM IAS20261.CITIES WHERE CITY_NO = {wrong}; EXCEPTION WHEN OTHERS THEN NULL; END;")
    sql_lines.append("END;")
    sql_lines.append("/")
    sql_lines.append("COMMIT;")
    sql_lines.append("")
    
    output_path = 'testing/migrate_cities.sql'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(sql_lines))
        
    print(f"Generated city migration script with {len(mappings)} city merges.")
    print(f"File saved to {output_path}")
            
except Exception as e:
    print(f"Error: {e}")
