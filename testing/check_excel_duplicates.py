import openpyxl
from collections import Counter

def safe_str(val):
    if val is None:
        return ""
    return str(val).strip()

try:
    file_path = r"C:\Users\amarn\Downloads\الثلاجات_تصنيف_اونكس_برو.xlsx"
    wb = openpyxl.load_workbook(file_path, data_only=True)
    ws = wb.active
    
    i_codes = []
    
    for row_idx, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
        i_code = safe_str(row[5])
        if i_code:
            i_codes.append(i_code)
            
    # Count occurrences
    counts = Counter(i_codes)
    duplicates = {k: v for k, v in counts.items() if v > 1}
    
    print(f"Total rows with item codes: {len(i_codes)}")
    print(f"Unique item codes: {len(counts)}")
    print(f"Number of items that are duplicated: {len(duplicates)}")
    
    if duplicates:
        print("\nHere are some of the duplicated items and their counts:")
        for item, count in list(duplicates.items())[:10]:
            print(f"  - Item: {item} (Appears {count} times)")
            
except Exception as e:
    print(f"Error: {e}")
