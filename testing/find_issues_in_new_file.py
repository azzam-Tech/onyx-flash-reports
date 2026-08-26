import openpyxl
from collections import Counter

def safe_str(val):
    if val is None:
        return ""
    if isinstance(val, float) and val.is_integer():
        return str(int(val)).strip()
    return str(val).strip()

try:
    file_path = r"C:\Users\amarn\Downloads\الثلاجات_تصنيف_اونكس_برو_مرتب (1).xlsx"
    wb = openpyxl.load_workbook(file_path, data_only=True)
    ws = wb.active
    
    i_codes = []
    items_with_001 = []
    
    for row_idx, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
        if len(row) > 8 and safe_str(row[8]):
            i_code = safe_str(row[8])
            mng_code = safe_str(row[2])
            
            i_codes.append((row_idx, i_code))
            if mng_code == '001' or mng_code == '1':
                items_with_001.append((row_idx, i_code))
                
    counts = Counter(code for r, code in i_codes)
    duplicates = {k: v for k, v in counts.items() if v > 1}
    
    print("--- 3 Duplicated Items ---")
    for dup in duplicates:
        rows = [r for r, code in i_codes if code == dup]
        print(f"Item {dup} is duplicated on rows: {rows}")
        
    print("\n--- Items with MNG_CODE = 001 ---")
    for r, code in items_with_001:
        print(f"Row {r}: {code}")
        
except Exception as e:
    print(f"Error: {e}")
