import sys
import os
import openpyxl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_excel_items():
    file_path = r"C:\Users\amarn\Downloads\الثلاجات_تصنيف_اونكس_برو_مرتب.xlsx"
    try:
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        
        # Read Excel, assume first row is header
        excel_items = []
        for i, row in enumerate(sheet.iter_rows(values_only=True)):
            if i == 0: continue # Skip header
            
            # The user says "اسم الصنف رقم الصنف". Let's try to find the code.
            # We don't know exact column indices, so we'll collect all cell values
            # and guess the I_CODE. Usually it's numeric/string.
            excel_items.append(row)
            
        # Try to guess which column is I_CODE by querying the DB
        # Usually it's the 4th, 5th, or 1st column. Let's just collect all non-null values.
        
        with get_conn() as con:
            with con.cursor() as cur:
                # Get all I_CODEs from DB
                cur.execute("SELECT I_CODE, G_CODE FROM IAS_ITM_MST")
                db_items = {r[0]: r[1] for r in cur.fetchall()}
                
                matched = 0
                not_found = []
                wrong_group = []
                
                # Let's find the I_CODE column in the first row
                icode_idx = -1
                for idx, val in enumerate(excel_items[0]):
                    if val and str(val).strip() in db_items:
                        icode_idx = idx
                        break
                        
                if icode_idx == -1:
                    print("Could not detect I_CODE column in Excel file!")
                    print("First row values:", excel_items[0])
                    return
                
                print(f"Detected I_CODE at column index {icode_idx}")
                
                for row in excel_items:
                    icode = str(row[icode_idx]).strip() if row[icode_idx] else None
                    if not icode:
                        continue
                        
                    if icode not in db_items:
                        not_found.append(row)
                    elif db_items[icode] != '003':
                        wrong_group.append((icode, db_items[icode]))
                    else:
                        matched += 1
                        
                print(f"Total rows in Excel: {len(excel_items)}")
                print(f"Matched in DB under Group '003': {matched}")
                
                if not_found:
                    print(f"\nItems in Excel NOT FOUND in DB: {len(not_found)}")
                    for item in not_found[:5]:
                        print(" -", item)
                        
                if wrong_group:
                    print(f"\nItems in Excel but in a different group: {len(wrong_group)}")
                    for item in wrong_group[:5]:
                        print(" -", item)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    check_excel_items()
