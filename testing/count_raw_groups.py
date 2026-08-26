import openpyxl

try:
    file_path = r"C:\Users\amarn\Downloads\الثلاجات_تصنيف_اونكس_برو.xlsx"
    wb = openpyxl.load_workbook(file_path, data_only=True)
    ws = wb.active
    
    raw_mng_codes = set()
    raw_mng_names = set()
    
    for row in ws.iter_rows(min_row=2, values_only=True):
        mng_code = row[2]
        # Skip purely empty
        if mng_code is not None and str(mng_code).strip() != '':
            raw_mng_codes.add(str(mng_code).strip())
            
        # Let's also check column 3 (Sub-Sub Group or is it something else?)
        # Wait, the user said column 3 might be names or sizes?
        # Let's check what they actually wrote in the raw column 3 if it was the Sub-Sub code? No, column index 2 is Sub Group Code.
        # But wait, what if they meant unique SIZES (which might be in another column, e.g. column 3)?
    
    print(f"Raw unique MNG_CODEs (Column C): {len(raw_mng_codes)}")
    print("Values:")
    print(sorted(list(raw_mng_codes)))
    
except Exception as e:
    print(f"Error: {e}")
