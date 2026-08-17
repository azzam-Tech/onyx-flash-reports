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
    # Remove hyphens, dots, spaces, underscores
    cleaned = code.replace('-', '').replace('.', '').replace('_', '').replace(' ', '').upper()
    # Sort characters to allow anagram matching
    return ''.join(sorted(cleaned))

def match_items():
    try:
        conn = oracledb.connect(user='RPT_USER', password='ULT2016', dsn='100.100.1.100:1521/ORCL')
        cur = conn.cursor()
        
        # Fetch all items
        cur.execute("SELECT I_CODE, I_NAME FROM IAS_ITM_MST")
        all_items = cur.fetchall()
        
        # Precompute normalized DB codes
        db_map = {}
        for row in all_items:
            i_code = row[0]
            if i_code:
                norm_code = normalize(i_code)
                if norm_code not in db_map:
                    db_map[norm_code] = []
                db_map[norm_code].append((i_code, row[1]))
                
        matches = []
        unmatched = []
        
        for m_code in missing_codes:
            norm_m = normalize(m_code)
            if norm_m in db_map:
                # We found one or more matches! (pick the first for excel)
                match_code, match_name = db_map[norm_m][0]
                matches.append((m_code, match_code, match_name))
            else:
                unmatched.append(m_code)
                
        cur.close()
        conn.close()
        
        # Create Excel file
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "الأصناف المطابقة"
        
        # Headers
        ws.append(["الكود الملخبط (من الإكسيل)", "الكود الصحيح (قاعدة البيانات)", "اسم الصنف في النظام"])
        
        for m in matches:
            ws.append([m[0], m[1], m[2]])
            
        excel_path = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\pricing\الأصناف_المطابقة.xlsx"
        wb.save(excel_path)
        print(f"Excel file created successfully at: {excel_path}")
        
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == '__main__':
    match_items()
