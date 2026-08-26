import openpyxl

def safe_str(val):
    if val is None:
        return ""
    return str(val).strip()

try:
    file_path = r"C:\Users\amarn\Downloads\الثلاجات_تصنيف_اونكس_برو.xlsx"
    wb = openpyxl.load_workbook(file_path, data_only=True)
    ws = wb.active
    
    mng_codes_with_items = set()
    all_mng_codes_in_file = set()
    
    empty_rows = []
    
    for row_idx, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
        mng_code = safe_str(row[2])
        if mng_code: mng_code = mng_code.zfill(3)
        
        i_code = safe_str(row[5])
        
        if mng_code:
            all_mng_codes_in_file.add(mng_code)
            if i_code:
                mng_codes_with_items.add(mng_code)
            else:
                empty_rows.append((row_idx, mng_code, safe_str(row[3])))
                
    missing = all_mng_codes_in_file - mng_codes_with_items
    
    print(f"Total unique sub groups mentioned in Excel: {len(all_mng_codes_in_file)}")
    print(f"Sub groups with items: {len(mng_codes_with_items)}")
    
    if missing:
        print("Sub groups mentioned but have NO items linked in the file:")
        for m in sorted(list(missing)):
            print(f"  - {m}")
            
    print("\nRows in Excel with Sub Group but NO Item Code:")
    for r in empty_rows[:10]:
        print(f"  Row {r[0]}: MNG_CODE={r[1]}")
        
    # Let's print all 27 found sub groups to help the user identify
    print("\nThe 27 Sub Groups that have items:")
    for m in sorted(list(mng_codes_with_items)):
        print(f"  - {m}")
        
except Exception as e:
    print(f"Error: {e}")
