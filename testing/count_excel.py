import openpyxl
import json

def count_excel():
    file_path = r"C:\Users\amarn\Downloads\الثلاجات.xlsx"
    try:
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        
        # Skip header row
        rows = list(sheet.iter_rows(values_only=True))
        data_rows = [r for r in rows[1:] if r[4]] # where item_code is not null
        
        print(f"Total data rows in Excel: {len(data_rows)}")
        
        # Save a sample to json for viewing
        sample = data_rows[:3]
        with open("testing/excel_sample.json", "w", encoding="utf-8") as f:
            json.dump(sample, f, ensure_ascii=False, indent=2)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    count_excel()
