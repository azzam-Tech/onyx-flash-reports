import openpyxl
import json

def read_excel():
    file_path = r"C:\Users\amarn\Downloads\الثلاجات.xlsx"
    try:
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        data = []
        for i, row in enumerate(sheet.iter_rows(values_only=True)):
            data.append(row)
            if i >= 5:
                break
        
        with open("testing/excel_out.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    read_excel()
