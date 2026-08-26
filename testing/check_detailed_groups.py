import openpyxl
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_pooled_conn

def safe_str(val):
    if val is None: return ""
    return str(val).strip()

try:
    file_path = r"C:\Users\amarn\Downloads\الثلاجات_تصنيف_اونكس_برو.xlsx"
    wb = openpyxl.load_workbook(file_path, data_only=True)
    ws = wb.active
    
    i_codes = set()
    for row in ws.iter_rows(min_row=2, values_only=True):
        i_code = safe_str(row[5])
        if i_code:
            i_codes.add(i_code)
            
    with get_pooled_conn() as conn:
        with conn.cursor() as cur:
            i_codes_list = list(i_codes)
            
            # Use string formatting safely since we know these are just alphanumeric codes
            # Or use format like :1, :2
            binds = [f":{i+1}" for i in range(len(i_codes_list))]
            query = f"""
                SELECT I_CODE, GROUP_NO, ILEV_NO, DETAIL_NO 
                FROM IAS20261.IAS_ITM_MST 
                WHERE I_CODE IN ({','.join(binds)})
            """
            cur.execute(query, i_codes_list)
            
            items_with_detailed_group = []
            for r in cur.fetchall():
                if r[1] is not None or r[3] is not None:
                    items_with_detailed_group.append(r)
                    
            print(f"Total items checked: {len(i_codes_list)}")
            print(f"Items connected to GROUP_NO or DETAIL_NO: {len(items_with_detailed_group)}")
            
            if items_with_detailed_group:
                print("\nSample items with detailed groups:")
                for r in items_with_detailed_group[:5]:
                    print(r)
                    
            # Check detailed group tables
            cur.execute("""
                SELECT TABLE_NAME FROM ALL_TAB_COLUMNS 
                WHERE OWNER = 'IAS20261' AND COLUMN_NAME IN ('GROUP_NO', 'DETAIL_NO')
                AND TABLE_NAME LIKE 'IAS_%'
            """)
            tables = set(r[0] for r in cur.fetchall())
            print(f"\nTables containing GROUP_NO or DETAIL_NO: {tables}")
            
except Exception as e:
    print(f"Error: {e}")
