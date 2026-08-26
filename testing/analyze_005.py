import os
import sys
import openpyxl

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def analyze_005_excel():
    file_path = r"C:\Users\amarn\Downloads\غسالات_مصنفة_بالاكواد_1.xlsx"
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    try:
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        
        excel_items = []
        for i, row in enumerate(sheet.iter_rows(values_only=True)):
            if i > 0: # skip header
                excel_items.append(row)
                
        print(f"Total rows in Excel (excluding header): {len(excel_items)}")
        
        with get_conn() as con:
            with con.cursor() as cur:
                # Get all I_CODEs for G_CODE = '005'
                cur.execute("SELECT I_CODE FROM IAS_ITM_MST WHERE G_CODE = '005'")
                db_items = {str(r[0]).strip() for r in cur.fetchall()}
                
        print(f"Total items in DB for G_CODE '005': {len(db_items)}")
        
        matched = 0
        not_in_db = []
        
        for row in excel_items:
            # Assuming I_CODE is at index 8 based on previous output
            icode = str(row[8]).strip() if row[8] else None
            if not icode:
                continue
                
            if icode in db_items:
                matched += 1
            else:
                not_in_db.append(icode)
                
        print(f"Matched I_CODEs between Excel and DB: {matched}")
        if not_in_db:
            print(f"Items in Excel but NOT in DB (first 10): {not_in_db[:10]}")
            
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == '__main__':
    analyze_005_excel()
