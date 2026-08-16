import oracledb
import os
import openpyxl

os.environ["PATH"] = r"C:\oracle\instantclient\instantclient_23_0;" + os.environ.get("PATH", "")
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient\instantclient_23_0")

def update_last_three():
    try:
        mapping = {
            'TWS-8SRWM': 'SRWM-8TW.',
            'TWS-12SRWM': 'SRWM-12TW.',
            'HIKT-50S4KW3': 'HIKT-50S3'
        }
        
        # 1. Read Prices from Excel
        file_path = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\pricing\تحديث الاسعار.xlsx"
        wb = openpyxl.load_workbook(file_path, data_only=True)
        sheet = wb.active
        
        prices_map = {}
        for row in sheet.iter_rows(min_row=2, values_only=True):
            if not row or not row[0] or not row[2]:
                continue
            code = str(row[0]).strip()
            new_price = row[2]
            if code in mapping:
                try:
                    prices_map[mapping[code]] = float(new_price)
                except ValueError:
                    continue

        # 2. Update DB
        conn = oracledb.connect(user='ULT', password='ULT2017', dsn='100.100.1.100:1521/ORCL')
        cur = conn.cursor()
        
        updated_count = 0
        for correct_code, new_price in prices_map.items():
            
            cur.execute("SELECT I_PRICE FROM IAS20261.IAS_ITEM_PRICE WHERE I_CODE = :1 AND LEV_NO = 2", (correct_code,))
            res = cur.fetchone()
            
            if not res:
                print(f"Not found in IAS_ITEM_PRICE: {correct_code}")
                continue
                
            old_price = res[0]
            
            if old_price == new_price:
                print(f"Already updated (identical price) for: {correct_code}")
                continue
                
            # History
            cur.execute("""
                INSERT INTO IAS20261.IAS_ITEM_PRICE_HISTORY 
                (I_CODE, LEV_NO, PREV_I_PRICE, I_PRICE, AUD_DATE, AUD_U_ID)
                VALUES (:1, 2, :2, :3, SYSDATE, 999)
            """, (correct_code, old_price, new_price))
            
            # Update
            cur.execute("""
                UPDATE IAS20261.IAS_ITEM_PRICE
                SET I_PRICE = :1, UP_DATE = SYSDATE, UP_U_ID = 999
                WHERE I_CODE = :2 AND LEV_NO = 2
            """, (new_price, correct_code))
            
            updated_count += 1
            print(f"Updated {correct_code} retail price from {old_price} to {new_price}")
            
        conn.commit()
        cur.close()
        conn.close()
        
        print(f"\nSuccessfully updated {updated_count} items.")
        
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == '__main__':
    update_last_three()
