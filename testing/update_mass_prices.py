import oracledb
import os
import openpyxl

os.environ["PATH"] = r"C:\oracle\instantclient\instantclient_23_0;" + os.environ.get("PATH", "")
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient\instantclient_23_0")

file_path = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\pricing\تحديث الاسعار.xlsx"

def get_identical_prices():
    try:
        wb = openpyxl.load_workbook(file_path, data_only=True)
        sheet = wb.active
        
        conn = oracledb.connect(user='ULT', password='ULT2017', dsn='100.100.1.100:1521/ORCL')
        cur = conn.cursor()
        
        identical_items = []
        
        for row in sheet.iter_rows(min_row=2, values_only=True):
            if not row or not row[0] or not row[2]:
                continue
                
            code = str(row[0]).strip()
            new_price = row[2]
            
            try:
                new_price = float(new_price)
            except ValueError:
                continue
                
            if code.startswith('.'):
                code = code[1:] + '.'
                
            cur.execute("SELECT I_PRICE FROM IAS_ITEM_PRICE WHERE I_CODE = :1 AND LEV_NO = 2", (code,))
            res = cur.fetchone()
            
            if not res:
                continue
                
            old_price = res[0]
            
            if old_price == new_price:
                identical_items.append((code, old_price))
            
        cur.close()
        conn.close()
        
        print(f"\nItems skipped because prices are already identical (Total: {len(identical_items)}):")
        for item, price in identical_items:
            print(f"- {item} (Price: {price})")
            
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == '__main__':
    get_identical_prices()
