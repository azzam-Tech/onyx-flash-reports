import oracledb
import os
import openpyxl

os.environ["PATH"] = r"C:\oracle\instantclient\instantclient_23_0;" + os.environ.get("PATH", "")
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient\instantclient_23_0")

missing_codes = [
    '1S-32SRET', '323-SRET', '2S-40SRET', '2S-43SRET', '2K4S-50SRET', '3K4S-50SRET', '2KQ4S-50SRET', 
    '2K4S-55SRET', '3K4S-55SRET', '2KQ4S-55SRET', '3S-65SRET', '3KWQ4S-86SRET', 'DF129SRCF', 'DF-142SRCF', 
    'DF259SRCF', 'DF389SRCF', 'TTW-K-5SRWM', 'TT-5SRZWM', 'TTW-K-7SRWM', 'TT-10SRWM', 'TTW-K-13SRWM', 
    'TTW-K-18SRWM', 'TWS-8SRWM', 'TAS-K-8SRWM', 'TASS-9K-D3K-SRWM', 'TAS-9K-D3K-SRWM', 'TWS-12SRWM', 
    'AT-14SRWM', 'TAS-K-15SRWM', 'TAS-K-18SRWM', 'TASS-K-18SRWM', 'FW-8SRWM', 'FAS-K-12SRWM', 'LG-25SREVC', 
    'LB-21SREVC', 'LG-21SREVC', 'SB-100SRW', 'RC-Wg-95SRW', 'HIKT-50S4KW3', '.FREWM-12K.', 'FA-M90DG.'
]

def normalize(code):
    cleaned = code.replace('-', '').replace('.', '').replace('_', '').replace(' ', '').upper()
    return ''.join(sorted(cleaned))

def update_matched_items():
    try:
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
            try:
                prices_map[code] = float(new_price)
            except ValueError:
                continue

        # 2. Match Codes
        conn = oracledb.connect(user='ULT', password='ULT2017', dsn='100.100.1.100:1521/ORCL')
        cur = conn.cursor()
        
        cur.execute("SELECT I_CODE, I_NAME FROM IAS20261.IAS_ITM_MST")
        all_items = cur.fetchall()
        
        db_map = {}
        for row in all_items:
            i_code = row[0]
            if i_code:
                norm_code = normalize(i_code)
                if norm_code not in db_map:
                    db_map[norm_code] = []
                db_map[norm_code].append((i_code, row[1]))
                
        matches = []
        for m_code in missing_codes:
            norm_m = normalize(m_code)
            if norm_m in db_map:
                match_code, match_name = db_map[norm_m][0]
                matches.append((m_code, match_code))
                
        # 3. Update DB
        updated_count = 0
        for scrambled, correct in matches:
            if scrambled not in prices_map:
                print(f"Price not found in Excel for: {scrambled}")
                continue
                
            new_price = prices_map[scrambled]
            
            cur.execute("SELECT I_PRICE FROM IAS20261.IAS_ITEM_PRICE WHERE I_CODE = :1 AND LEV_NO = 2", (correct,))
            res = cur.fetchone()
            
            if not res:
                print(f"Not found in IAS_ITEM_PRICE: {correct}")
                continue
                
            old_price = res[0]
            
            if old_price == new_price:
                # Already updated / same price
                continue
                
            # History
            cur.execute("""
                INSERT INTO IAS20261.IAS_ITEM_PRICE_HISTORY 
                (I_CODE, LEV_NO, PREV_I_PRICE, I_PRICE, AUD_DATE, AUD_U_ID)
                VALUES (:1, 2, :2, :3, SYSDATE, 999)
            """, (correct, old_price, new_price))
            
            # Update
            cur.execute("""
                UPDATE IAS20261.IAS_ITEM_PRICE
                SET I_PRICE = :1, UP_DATE = SYSDATE, UP_U_ID = 999
                WHERE I_CODE = :2 AND LEV_NO = 2
            """, (new_price, correct))
            
            updated_count += 1
            print(f"Updated {correct} (from '{scrambled}') retail price from {old_price} to {new_price}")
            
        conn.commit()
        cur.close()
        conn.close()
        
        print(f"\nSuccessfully updated {updated_count} fuzzy-matched items.")
        
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == '__main__':
    update_matched_items()
