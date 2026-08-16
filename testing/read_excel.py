import sys
try:
    import openpyxl
except ImportError:
    print("Installing openpyxl...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])
    import openpyxl

file_path = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\pricing\تحديث الاسعار.xlsx"
try:
    wb = openpyxl.load_workbook(file_path, data_only=True)
    sheet = wb.active
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)
    
    print("Total rows:", len(data))
    print("First 10 rows:")
    for row in data[1:10]:
        print(repr(row[0]), row[2])
except Exception as e:
    print(f"Error reading excel: {e}")
