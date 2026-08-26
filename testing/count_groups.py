import openpyxl

def safe_str(val):
    if val is None:
        return ""
    return str(val).strip()

try:
    file_path = r"C:\Users\amarn\Downloads\الثلاجات_تصنيف_اونكس_برو.xlsx"
    wb = openpyxl.load_workbook(file_path, data_only=True)
    ws = wb.active
    
    mng_codes = set()
    subg_codes = set()
    
    for row in ws.iter_rows(min_row=2, values_only=True):
        mng_code = safe_str(row[2])
        if mng_code: mng_code = mng_code.zfill(3)
        subg_code = safe_str(row[3])
        if subg_code: subg_code = subg_code.zfill(3)
        
        i_code = safe_str(row[5])
        
        if i_code:
            if mng_code:
                mng_codes.add(mng_code)
            if subg_code:
                subg_codes.add(subg_code) # Count absolute sub-sub groups, not pairs
                
    print(f"Unique Sub Groups (MNG_CODE): {len(mng_codes)}")
    print(f"Unique Sub-Sub Groups (SUBG_CODE): {len(subg_codes)}")
    
except Exception as e:
    print(f"Error: {e}")
