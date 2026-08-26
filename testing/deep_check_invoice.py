import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def deep_check():
    bill_no = '26314600409'
    with get_conn() as con:
        with con.cursor() as cur:
            # Check IAS_BILL_MST
            cur.execute("SELECT BILL_NO, BILL_DOC_TYPE, DOC_HASH, WEB_SRVC_UUID FROM IAS_BILL_MST WHERE BILL_NO = :1", [bill_no])
            res = cur.fetchall()
            print("--- IAS_BILL_MST ---")
            for r in res:
                print(f"Doc Type: {r[1]}, Hash: {'Yes' if r[2] and r[2].strip() else 'No'}, UUID: {'Yes' if r[3] and r[3].strip() else 'No'}")
                
            # Find any table with BILL_NO column
            cur.execute("""
                SELECT table_name 
                FROM all_tab_columns 
                WHERE column_name = 'BILL_NO' 
                  AND table_name LIKE '%BILL_MST%'
            """)
            tables = cur.fetchall()
            print("\n--- Searching other BILL_MST tables ---")
            for t in tables:
                tname = t[0]
                if tname != 'IAS_BILL_MST':
                    try:
                        cur.execute(f"SELECT BILL_NO FROM {tname} WHERE BILL_NO = :1", [bill_no])
                        if cur.fetchall():
                            print(f"Found {bill_no} in table: {tname}")
                    except Exception:
                        pass
                        
            # Check ZATCA Sync Tables for this specific bill
            print("\n--- Searching ZATCA Sync Tables ---")
            try:
                cur.execute("SELECT DOC_TYPE, DOC_NO, SYNC_FLG, SYNC_RSLT FROM GNR_EXTRNL_DOC_SYNC WHERE DOC_NO = :1", [bill_no])
                res = cur.fetchall()
                if res:
                    for r in res:
                        print(f"GNR_EXTRNL_DOC_SYNC -> Type: {r[0]}, Doc: {r[1]}, Sync_FLG: {r[2]}, Rslt: {r[3]}")
                else:
                    print("Not found in GNR_EXTRNL_DOC_SYNC")
            except Exception as e:
                print(f"Error querying GNR_EXTRNL_DOC_SYNC: {e}")

if __name__ == '__main__':
    deep_check()
