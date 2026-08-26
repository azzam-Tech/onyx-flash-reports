import openpyxl

try:
    file_path = r"C:\Users\amarn\Downloads\الثلاجات_تصنيف_اونكس_برو_محدث3.xlsx"
    wb = openpyxl.load_workbook(file_path, data_only=True)
    ws = wb.active
    
    count_000 = 0
    count_001 = 0
    
    for row_idx, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
        if len(row) > 8 and row[8] is not None:
            mng_code = str(row[2]).strip()
            if mng_code == '000' or mng_code == '0':
                count_000 += 1
                print(f"Row {row_idx}: Item {row[8]} has MNG_CODE = {row[2]}")
            if mng_code == '001' or mng_code == '1':
                count_001 += 1
                print(f"Row {row_idx}: Item {row[8]} has MNG_CODE = {row[2]}")
                
    print(f"\nFound {count_000} occurrences of '000' and {count_001} occurrences of '001'.")
    
except Exception as e:
    print(f"Error: {e}")
